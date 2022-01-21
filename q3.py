import requests
import pandas as pd
 
# Set the request parameters
url = 'https://{zendesk_domain}/api/v2/tickets.json'
user = '{zendesk_users}'
pwd = '{zendesk_pass}'
 
# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))
 
# Check for HTTP codes other than 200
if response.status_code != 200:
   print('Status:', response.status_code, 'Problem with the request. Exiting.')
   exit()
 
data = response.json()
print(type(data))
df = pd.DataFrame.from_dict(data)