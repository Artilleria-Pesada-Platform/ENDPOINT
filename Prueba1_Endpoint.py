from operator import truediv
from pickle import TRUE
from flask import Flask
from flask_restful import Resource,Api,reqparse
import pandas as pd
import ast

app=Flask(__name__)
api=Api(app)


#/dashboard data
dash_path='./dash.csv'

class Dashboard (Resource):
    def get(self):
        data=pd.read_csv(dash_path)
        data=data.to_dict()
        return{'data':data},200

   # def post(self):
   #     parser =reqparse.RequestParser()
   #     parser.add_argument('grafica',required=True,type=int)
    #    parser.add_argument('nombre',required=True,type=str)
     #   parser.add_argument('data',required=True,type=int)
      #  args=parser.parse_args()
       # return{
           #  'graf': args['grafica'],
        #     'nom': args['nombre'],
         #    'dat': args['data']
     
          #    },200
   
            
        
                


#api.com/users


api.add_resource(Dashboard,'/dash')

if __name__=="__main__":
    app.run(debug=TRUE)
