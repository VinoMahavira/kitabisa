import json
import pandas as pd
from sqlalchemy import create_engine  
 
f = open('source_json.json')
data = json.load(f)
df = pd.DataFrame(data)
df['batters'] = [d.get('batter') for d in df['batters']]
df['batters'] = list(map(lambda x: json.dumps(x), df['batters']))
df['topping'] = list(map(lambda x: json.dumps(x), df['topping']))
engine = create_engine('postgresql://localhost/macbookpro15')
 
df.to_sql('products', engine,if_exists='append',index=False)
