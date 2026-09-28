from pathlib import Path
import json,pandas as pd,numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
ROOT=Path(__file__).parent
DEFAULT={'Market':'Groceries','Metro':'Transport','Stream':'Entertainment','Cafe':'Dining'}
def categorize(df,rules):
 if not isinstance(rules,dict) or len(rules)>100 or any(not isinstance(k,str) or not isinstance(v,str) or not 1<=len(v)<=40 for k,v in rules.items()):raise ValueError('Rules must map merchant names to 1–40 character categories')
 if df.id.duplicated().any() or df.cents.isna().any() or (df.cents<0).any() or (df.cents%1!=0).any():raise ValueError('Duplicate transaction IDs or invalid cents')
 df=df.copy();df['category']=df.merchant.map(rules).fillna('Uncategorized');return df

def analyze(p):
 try:rules=json.loads(p.get('rules',json.dumps(DEFAULT)))
 except (json.JSONDecodeError,TypeError) as e:raise ValueError('Category rules must be valid JSON') from e
 k=int(p.get('clusters',3))
 df=categorize(pd.read_csv(ROOT/'data/transactions.csv'),rules)
 pivot=df.pivot_table(index='customer',columns='category',values='cents',aggfunc='sum',fill_value=0)
 if not 2<=k<=min(8,len(pivot)-1):raise ValueError('Choose 2–8 clusters, fewer than customers')
 # Cluster composition, not raw wealth: shares + transaction frequency; standardize afterward.
 shares=pivot.div(pivot.sum(axis=1),axis=0);shares['frequency']=df.groupby('customer').size()
 x=StandardScaler().fit_transform(shares);labels=KMeans(n_clusters=k,n_init=20,random_state=31).fit_predict(x)
 actual=len(set(labels));sil=float(silhouette_score(x,labels)) if 1<actual<len(x) else None
 pivot['cluster']=labels;summary=df.groupby('category').cents.sum()
 rows=[dict(customer=c,cluster=int(row['cluster']),total_usd=round(float(row.drop('cluster').sum())/100,2)) for c,row in pivot.iterrows()]
 return dict(metrics={'Total spending':f'${df.cents.sum()/100:,.2f}','Transactions':len(df),'Customers':len(pivot),'Silhouette':round(sil,3) if sil is not None else 'undefined'},bars=[dict(label=k,value=round(v/100,2)) for k,v in summary.items()],rows=rows,chart_title='Spending by your categories',details={'rules':rules,'cluster_counts':{str(k):int(v) for k,v in pd.Series(labels).value_counts().items()},'monthly_cents':{k:int(v) for k,v in df.groupby(df.date.str[:7]).cents.sum().items()},'total_cents':int(df.cents.sum()),'method':'category shares + transaction frequency; standardized KMeans; descriptive segments, not prediction'})
