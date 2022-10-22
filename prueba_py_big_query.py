from google.cloud import bigquery
from google.oauth2 import service_account
from pandas import DataFrame

credentials = service_account.Credentials.from_service_account_file('./bbva-latam-hack22mex-5001-fdcefe2411a1.json')

project_id = 'bbva-latam-hack22mex-5001'
client = bigquery.Client(credentials= credentials,project=project_id)



query_job = client.query("""
   SELECT *
   FROM  bbva-latam-hack22mex-5001.ATM.TABLA_TRANS_SEPT  limit 100""")

results = query_job.result()
df = results.to_dataframe()
print(df)
