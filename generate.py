import random,csv
from pathlib import Path
r=random.Random(31);root=Path(__file__).parent;(root/'data').mkdir(exist_ok=True)
with (root/'data/transactions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['id','customer','date','merchant','cents'])
 for i in range(1000):
  customer=r.randrange(60);merchant=r.choices(['Market','Metro','Stream','Cafe','Books','Travel'],weights=([8,3,1,4,2,1] if customer%3==0 else [3,6,3,1,2,5] if customer%3==1 else [2,2,7,6,4,1]))[0]
  w.writerow([f'T{i:05}',f'C{customer:03}',f'2026-{r.randint(1,6):02}-{r.randint(1,28):02}',merchant,r.randint(500,15000)*(4 if merchant=='Travel' else 1)])
