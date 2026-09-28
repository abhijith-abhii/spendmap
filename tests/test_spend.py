import json,pytest,pandas as pd
from core import analyze,categorize

def test_category_reconciliation():
 d=analyze({});assert round(sum(x['value'] for x in d['bars'])*100)==d['details']['total_cents']
 assert sum(d['details']['cluster_counts'].values())==60

def test_override_changes_category():
 d=analyze({'rules':'{"Market":"Food"}'});assert any(x['label']=='Food' for x in d['bars'])
 assert all(x['label']!='Groceries' for x in d['bars'])
@pytest.mark.parametrize('p',[{'rules':'[]'},{'rules':'{'},{'clusters':1},{'clusters':99}])
def test_bad_parameters(p):
 with pytest.raises(ValueError):analyze(p)
