from operator import truediv
from pickle import TRUE
from flask import Flask
from flask_restful import Resource,Api,reqparse
import pandas as pd
import ast

from google.cloud import bigquery
from google.oauth2 import service_account
from pandas import DataFrame
import json

credentials = service_account.Credentials.from_service_account_file('./bbva-latam-hack22mex-5001-fdcefe2411a1.json')

project_id = 'bbva-latam-hack22mex-5001'
client = bigquery.Client(credentials= credentials,project=project_id)


app=Flask(__name__)
api=Api(app)


#/dashboard data
#dash_path='./dash.csv'
query_job = client.query("""
   SELECT *
   FROM  bbva-latam-hack22mex-5001.ATM.TABLA_TRANS_SEPT limit 10""")








class Dashboard (Resource):
    def get(self):
        results = query_job.result()
        df = results.to_dataframe() 
        resu=df.to_json(orient="split")
        parsed=json.loads(resu)
        return{'parsed':parsed},200

        



#api.com/users


api.add_resource(Dashboard,'/dash')

if __name__=="__main__":
    app.run(debug=TRUE)
