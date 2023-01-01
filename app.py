#git commit -am "inicio"
#git push -u origin master
# pip install pymongo[srv]
# pip install flask_cors
# pip install pandas   
# pip install scikit-learn
#  pip install numpy       
#  pip install flask       

# from typing import Collection

from ast import If
from flask import Flask, request, render_template, Response                #MICRO FRAMEWORK PARA USAR PYTHON NA WEB;
#import pandas as pd    
#import numpy as np                                


from flask_cors import CORS, cross_origin     #pip install -U flask-cors
import datetime                                       #PARA TRABALHAR COM DATAS
from datetime import timedelta                         #PARA TRABALHAR COM DATAS
import os                                            # para eu só precisar python app.py
#from sklearn import  linear_model #, model_selection   # PARA GERAR O MODELO
                              # PARA GERAR O MODELO
import json

#import pickle                                                    #PARA TRABALHAR COM O MODELO
import pymongo                                                #PARA TRABALHAR COM  MONGODB   ; pip install pymongo  ;pip install "pymongo[srv]"

app = Flask(__name__)

cors = CORS(app)                                #pip install -U flask-cors
app.config['CORS_HEADERS'] = 'Content-Type'    #pip install -U flask-cors



############################################################################################################################################
############################################################################################################################################
@app.route("/")
def home():
    
    return render_template("app.html")




ANO=2022




###############################################DADOS PARA O GRÁFICO 1 #######################################################################################
###############################################DADOS PARA O GRÁFICO 1 #######################################################################################
###############################################DADOS PARA O GRÁFICO 1 #######################################################################################
import pymongo                     #PARA USAR BANCO DE DADOS MONGO  
import datetime                    #PARA TRABALHAR COM DATAS
from datetime import timedelta
cluster=pymongo.MongoClient('mongodb+srv://lavajato:eqB0nB5CjYSzNVMB@cluster0.0geealu.mongodb.net/?retryWrites=true&w=majority')   #acessando o mongo;
db=cluster["test"]
collection=db['vendas']




melhoressemana=[[0,0,0,0,0,0,0],[],[],[],[],[],[],[]]
melhoressemanadia=[0,0,0,0,0,0,0]
y = []
X=[]
p=0
mes=8
dia=8
while (datetime.datetime(ANO, mes, dia, 4, 00, 00, 000000)+ timedelta(days=p)<datetime.datetime.now()+ timedelta(days=0)):  # 22 FOI ATÉ 28/03/2022  #24 vai ter o fim de março
           resulta=collection.aggregate( [  {"$match": { "dataDaVenda":{   "$gte":datetime.datetime(ANO, mes, dia, 4, 00, 00, 000000)+ timedelta(days=p),"$lt": datetime.datetime(ANO, mes, dia, 4, 00, 00, 000000)+ timedelta(days=p+1)}, "estado":{"$eq":1}} },{  "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )    

           aux=0
           for resul in resulta:            
              y.append(resul["RCB"])
              X.append(0)
              aux=1
           
           if (aux==0):
              y.append(0)
              X.append(0)

 ############################################### GERA MATRIZ COM TODOS AS SEMANAS #######################################################################################  
           if (p%7==0):
              melhoressemana[1].append(y[p])  

              #####################PARA OBTER A SEMANA DO RECORDE NAQUELE DIA DA SEMANA###################
              if(max(melhoressemana[1])> melhoressemanadia[0]):
                 melhoressemanadia[0] = max(melhoressemana[1])
                 melhoressemana[0][0]= p
               #####################PARA OBTER A SEMANA DO RECORDE NAQUELE DIA DA SEMANA###################
           if (p%7==1):
              melhoressemana[2].append(y[p])  
              if(max(melhoressemana[2])> melhoressemanadia[1]):
                 melhoressemanadia[1] = max(melhoressemana[2])
                 melhoressemana[0][1]= p
           if (p%7==2):
              melhoressemana[3].append(y[p])  
              if(max(melhoressemana[3])> melhoressemanadia[2]):
                 melhoressemanadia[2] = max(melhoressemana[3])
                 melhoressemana[0][2]= p
           if (p%7==3):
              melhoressemana[4].append(y[p])  
              if(max(melhoressemana[4])> melhoressemanadia[3]):
                 melhoressemanadia[3] = max(melhoressemana[4])
                 melhoressemana[0][3]= p
           if (p%7==4):
              melhoressemana[5].append(y[p])
              if(max(melhoressemana[5])> melhoressemanadia[4]):
                 melhoressemanadia[4] = max(melhoressemana[5])
                 melhoressemana[0][4]= p  
           if (p%7==5):
              melhoressemana[6].append(y[p])
              if(max(melhoressemana[6])> melhoressemanadia[5]):
                 melhoressemanadia[5] = max(melhoressemana[6])
                 melhoressemana[0][5]= p  
           if (p%7==6):
              melhoressemana[7].append(y[p])
              if(max(melhoressemana[7])> melhoressemanadia[6]):
                 melhoressemanadia[6] = max(melhoressemana[7])
                 melhoressemana[0][6]= p     
 ############################################### GERA MATRIZ COM TODOS AS SEMANAS #######################################################################################             

           p=p+1       
print("ffffffffffff",melhoressemana[0][0]/7+1, melhoressemana[0][1]//7+1, melhoressemana[0][2]//7+1, melhoressemana[0][3]//7+1 , melhoressemana[0][4]//7+1 , melhoressemana[0][5]//7+1 , melhoressemana[0][6]//7+1  )  
###############################################DADOS PARA O GRÁFICO 1 #######################################################################################
###############################################DADOS PARA O GRÁFICO 1 #######################################################################################
###############################################DADOS PARA O GRÁFICO 1 #######################################################################################
for i in range(len(X)):
    X[i]=i+1


###############################################DADOS PARA O GRÁFICO 2 #######################################################################################
###############################################DADOS PARA O GRÁFICO 2 #######################################################################################
###############################################DADOS PARA O GRÁFICO 2 #######################################################################################

yy = []
XX=[.5,1.5,2.5,3.5,4.5,5.5]


resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datetime.datetime(ANO, 8, 1, 4, 00, 00, 000000),"$lt": datetime.datetime(ANO, 9, 1, 4, 00, 00, 000000) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
for resul in resulta:            
            yy.append(resul["RCB"])


resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datetime.datetime(ANO, 9, 1, 4, 00, 00, 000000),"$lt": datetime.datetime(ANO, 10, 1, 4, 00, 00, 000000) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
for resul in resulta:            
            yy.append(resul["RCB"])


resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datetime.datetime(ANO, 10, 1, 4, 00, 00, 000000),"$lt": datetime.datetime(ANO, 11, 1, 4, 00, 00, 000000) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
for resul in resulta:            
            yy.append(resul["RCB"])



resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datetime.datetime(ANO, 11, 1, 4, 00, 00, 000000),"$lt": datetime.datetime(ANO, 12, 1, 4, 00, 00, 000000) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
for resul in resulta:            
            yy.append(resul["RCB"])


resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datetime.datetime(ANO, 12, 1, 4, 00, 00, 000000),"$lt": datetime.datetime(2023, 1, 1, 4, 00, 00, 000000) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
for resul in resulta:            
            yy.append(resul["RCB"])     

resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datetime.datetime(2023, 1, 1, 4, 00, 00, 000000),"$lt": datetime.datetime(2023, 2, 1, 4, 00, 00, 000000) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
for resul in resulta:            
            yy.append(resul["RCB"])                     
###############################################DADOS PARA O GRÁFICO 2 #######################################################################################
###############################################DADOS PARA O GRÁFICO 2 #######################################################################################
###############################################DADOS PARA O GRÁFICO 2 #######################################################################################




###############################################DADOS PARA O GRÁFICO 3 #######################################################################################
###############################################DADOS PARA O GRÁFICO 3 #######################################################################################
###############################################DADOS PARA O GRÁFICO 3 #######################################################################################

XXX=[]

for AUX in range(1,(datetime.date.today().month+(datetime.date.today().year-1)*12)-(2021*12+7) +1):
    XXX.append(AUX-.5)
    print("fff",AUX)


yyy = []

for MES in range(8,13):
    data1=datetime.datetime(ANO, MES, 1, 4, 00, 00, 000000)
    
    if(MES+1==13):
         data2=datetime.datetime(2023, 1, 1, 4, 00, 00, 000000)
    else:
         data2=datetime.datetime(ANO, MES+1, 1, 4, 00, 00, 000000)
    resulta=collection.aggregate(  [{"$match": { "dataDaVenda":{   "$gte": data1 ,"$lt":  data2   } , "estado":{"$eq":1}}   },{ "$project": {"quantidadeporvenda": { "$sum":"$itens.quantidade"}   }  }]   )
   
   
    total=0
    for resul in resulta:  
            total+=resul["quantidadeporvenda"]
    yyy.append(total)




data1=datetime.datetime(2023, 1, 1, 4, 00, 00, 000000)
data2=datetime.datetime(2023, 2, 1, 4, 00, 00, 000000)
resulta=collection.aggregate(  [{"$match": { "dataDaVenda":{   "$gte": data1 ,"$lt":  data2   } , "estado":{"$eq":1}}   },{ "$project": {"quantidadeporvenda": { "$sum":"$itens.quantidade"}   }  }]   )

total=0
for resul in resulta:  
    total+=resul["quantidadeporvenda"]
    yyy.append(total)



###############################################DADOS PARA O GRÁFICO 3 #######################################################################################
###############################################DADOS PARA O GRÁFICO 3 #######################################################################################
###############################################DADOS PARA O GRÁFICO 3 #######################################################################################








###############################################DADOS PARA O GRÁFICO 4 #######################################################################################
###############################################DADOS PARA O GRÁFICO 4 #######################################################################################
###############################################DADOS PARA O GRÁFICO 4 #######################################################################################

datainicial= datetime.datetime(ANO, 8, 8, 4, 00, 00, 000000)
yyyy = []
XXXX=[]



i=0
while ( datainicial+ timedelta(days=(i*7))<= datetime.datetime.today()+ timedelta(days=0)  ) :
  resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datainicial+ timedelta(days=(i*7)),"$lte": datainicial+ timedelta(days=(i*7+7)) } , "estado":{"$eq":1}}   },{       "$group": {"_id": "null"  ,     "RCB":{ "$sum":"$total" } }     }     ] )
  aux=0
  for resul in resulta:            
            yyyy.append(resul["RCB"])
            aux=aux+1
  if (aux==0):
              yyyy.append(0)         
  i=i+1
  XXXX.append(i)











###############################################DADOS PARA O GRÁFICO 4 #######################################################################################
###############################################DADOS PARA O GRÁFICO 4 #######################################################################################
###############################################DADOS PARA O GRÁFICO 4 #######################################################################################


###############################################DADOS PARA O GRÁFICO 5 #######################################################################################
###############################################DADOS PARA O GRÁFICO 5 #######################################################################################
###############################################DADOS PARA O GRÁFICO 5 #######################################################################################

datainicial= datetime.datetime(ANO, 8, 8, 4, 00, 00, 000000)
yyyyy = []
XXXXX=[]

i=0
while ( datainicial+ timedelta(days=(i*7))<= datetime.datetime.today()+ timedelta(days=0) ) :
  resulta=collection.aggregate( [   {"$match": { "dataDaVenda":{   "$gte": datainicial+ timedelta(days=(i*7)),"$lt": datainicial+ timedelta(days=(i*7+7)) } , "estado":{"$eq":1}}   },{ "$project": {"quantidadeporvenda": { "$sum":"$itens.quantidade"}   }  }]  )
  total=0
  for resul in resulta:            
            total+=resul["quantidadeporvenda"]
           
  yyyyy.append(total)
  i=i+1
  XXXXX.append(i)

###############################################DADOS PARA O GRÁFICO 5 #######################################################################################
###############################################DADOS PARA O GRÁFICO 5 #######################################################################################
###############################################DADOS PARA O GRÁFICO 5 #######################################################################################




###############################################DADOS PARA O GRÁFICO 6 #######################################################################################
###############################################DADOS PARA O GRÁFICO 6 #######################################################################################
###############################################DADOS PARA O GRÁFICO 6 #######################################################################################
collection=db['clientes']


datainicial= datetime.datetime(ANO, 10, 10, 4, 00, 00, 000000)
y6 = []
X6=[]


i=0
k=10
while ( datainicial+ timedelta(days=(i*7))<= datetime.datetime.today()+ timedelta(days=0) ) :
  resulta=collection.aggregate( [   {"$match": { "dataDoCadastro":{   "$gte": datainicial+ timedelta(days=(i*7)),"$lt": datainicial+ timedelta(days=(i*7+7)) } , "estado":{"$eq":1}}   }, {"$count":"quantidadeclientes"}   ]  )
  total=0
  for resul in resulta:            
            total+=resul["quantidadeclientes"]
         

  y6.append(total)
  i=i+1
  X6.append(k)
  k=k+1
###############################################DADOS PARA O GRÁFICO 6 #######################################################################################
###############################################DADOS PARA O GRÁFICO 6 #######################################################################################
###############################################DADOS PARA O GRÁFICO 6 #######################################################################################





###############################################DADOS PARA O GRÁFICO 7 PIZZA#######################################################################################
###############################################DADOS PARA O GRÁFICO 7 PIZZA#######################################################################################
###############################################DADOS PARA O GRÁFICO 7 PIZZA#######################################################################################

collection=db['livrocaixas']

# AQUI MUDA AS TABELAS E PIZZA
datainicial= datetime.datetime(2023, 1, 1, 4, 00, 00, 000000)
datafinal= datetime.datetime(2023, 2, 1, 23, 00, 00, 000000)

y7 = []

resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"LAVADOR"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)



resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"VIGIA"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)


resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"DIVERSAS"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)



#  POR CAUSA DO CAIXA
y7.append(0)  


resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"PRODUTO"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)


resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"EQUIPAMENTO"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)


resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"ESTRUTURA"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)



resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"tipo":{"$eq":"ADMINISTRATIVO"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y7.append(total)


###############################################DADOS PARA O GRÁFICO 7 #######################################################################################
###############################################DADOS PARA O GRÁFICO 7 #######################################################################################
###############################################DADOS PARA O GRÁFICO 7 #######################################################################################



print("fffffffffffffffffeeeeeeee", y7)







###############################################DADOS PARA O GRÁFICO 8 PIZZA#######################################################################################
###############################################DADOS PARA O GRÁFICO 8 PIZZA#######################################################################################
###############################################DADOS PARA O GRÁFICO 8 PIZZA#######################################################################################

collection=db['livrocaixas']



y8 = []



resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"descricao":{"$eq":"LAV-LUIS"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y8.append(total)



resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"descricao":{"$eq":"LAV-JUNIOR"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y8.append(total)


resulta=collection.aggregate([  {"$match":{"estado":{"$eq":1},"descricao":{"$eq":"LAV-JEFFERSON"},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
total=0
for resul in resulta:            
            total+=resul["TOTALIZAÇÃO"]   
y8.append(total)





###############################################DADOS PARA O GRÁFICO 8 PIZZA#######################################################################################
###############################################DADOS PARA O GRÁFICO 8 PIZZA#######################################################################################
###############################################DADOS PARA O GRÁFICO 8 PIZZA#######################################################################################






###############################################DADOS PARA O GRÁFICO 9 TABELA COM RECEITA E SERVIÇOS POR LAVADOR#######################################################################################
###############################################DADOS PARA O GRÁFICO 9 TABELA COM RECEITA E SERVIÇOS POR LAVADOR#######################################################################################
###############################################DADOS PARA O GRÁFICO 9 TABELA COM RECEITA E SERVIÇOS POR LAVADOR#######################################################################################




collection=db['vendas']

resulta=collection.aggregate([ {"$match": { "dataDaVenda":{   "$gte":datainicial,"$lt": datafinal}, "estado":{"$eq":1}} },   { "$group": {        "_id": {"lavador":"$vendedor"}  ,     "receita":{ "$sum":"$total" }   , "servicos":{"$sum":1}     }     }  ,  { "$sort":{"servicos":-1} }     ])
 
 
total_Lavador=[]
total_Servicos=[]
total_Receita=[]
total_Recebimento=[]
total_Percentual=[]

TOTAL_REC=0
TOTAL_SER=0
TOTAL_RCBI=0
I=2
for resul in resulta:        
            total_Lavador.append(resul['_id']['lavador'] ) 
            total_Servicos.append(int(resul['servicos']))
            total_Receita.append(int(resul['receita']))
            

            collection=db['livrocaixas']
            resulta2=collection.aggregate([  {"$match":{"estado":{"$eq":1},"descricao":{"$eq":'LAV-'+resul['_id']['lavador']},  "data":{   "$gte": datainicial,"$lt": datafinal  }     }         } , { "$group": {        "_id": {"LAVADOR":"$tipo"}  ,     "TOTALIZAÇÃO":{ "$sum":"$valor" } }     }     ])
            total=0
            for resul2 in resulta2:            
                total+=resul2["TOTALIZAÇÃO"] 
            total_Recebimento.append(int(total))







            total_Percentual.append(        (int(( int(total)/ int(resul['receita'])      )*10000)/100)  )   
            TOTAL_REC = TOTAL_REC + int(resul['receita'])
            TOTAL_SER=  TOTAL_SER+int(resul['servicos'])
            TOTAL_RCBI=  TOTAL_RCBI+int(y8[I])
            I=I-1
total_Lavador.append('TOTAL')
total_Servicos.append(TOTAL_SER)
total_Receita.append(TOTAL_REC)
total_Recebimento.append(TOTAL_RCBI)
total_Percentual.append(0 )
print("total", total)

###############################################DADOS PARA O GRÁFICO 9 TABELA COM RECEITA E SERVIÇOS POR LAVADOR#######################################################################################
###############################################DADOS PARA O GRÁFICO 9 TABELA COM RECEITA E SERVIÇOS POR LAVADOR#######################################################################################
###############################################DADOS PARA O GRÁFICO 9 TABELA COM RECEITA E SERVIÇOS POR LAVADOR#######################################################################################




###############################################DADOS PARA O GRÁFICO 10 TABELA COM QUANTIDADE POR SERVIÇO#######################################################################################
###############################################DADOS PARA O GRÁFICO 10 TABELA COM QUANTIDADE POR SERVIÇO#######################################################################################
###############################################DADOS PARA O GRÁFICO 10 TABELA COM QUANTIDADE POR SERVIÇO#######################################################################################


descricao=[]
quantidade=[]

resulta=db.vendas.aggregate([  {"$match":  { "dataDaVenda":{   "$gte": datainicial,"$lt": datafinal } , "estado":{"$eq":1}} },   { "$group": { "_id": {"descricao":"$itens.descricao"},"count":{ "$sum":1 } }     } , {"$sort": { "count": -1 } }   ])
TOTAL_QUANTIDADE=0
for resul in resulta:        
      

            if(len(resul['_id']['descricao'])>1):
            #     # print("MULTIPLO", resul['_id']['codigo'] , "quantidade:",resul['count']   )
                descricao.append(resul['_id']['descricao'])  
                quantidade.append(resul['count'])
                TOTAL_QUANTIDADE=  TOTAL_QUANTIDADE+resul['count']
            else:
                # print("ÚNICO", resul['_id']['codigo'][0] , "quantidade:",resul['count']   )   
                descricao.append(resul['_id']['descricao'][0])  
                quantidade.append(resul['count'])  
                TOTAL_QUANTIDADE=  TOTAL_QUANTIDADE+resul['count']

            


descricao.append('TOTAL')
quantidade.append(TOTAL_QUANTIDADE)  
###############################################DADOS PARA O GRÁFICO 10 TABELA COM QUANTIDADE POR SERVIÇO#######################################################################################
###############################################DADOS PARA O GRÁFICO 10 TABELA COM QUANTIDADE POR SERVIÇO#######################################################################################
###############################################DADOS PARA O GRÁFICO 10 TABELA COM QUANTIDADE POR SERVIÇO#######################################################################################



























###############################################PREDIÇÃO ######################################################################################################
###############################################PREDIÇÃO ######################################################################################################
###############################################PREDIÇÃO ######################################################################################################

MESESDOANO=['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']


from bokeh.plotting import figure, show,  output_file, save

from bokeh.layouts import row
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot


################################BOTANDO NO FORMATO DA PREDIÇÃO######################################
import pandas as pd 
from sklearn import  linear_model

PONTOSTODOSDIA= pd.DataFrame(X)
PONTOSTODOSVALOR= pd.DataFrame(y)
PONTOSTODOSDIA=PONTOSTODOSDIA.values.reshape(-1,1)

import numpy as np
for i in range(len(PONTOSTODOSDIA)):
    PONTOSTODOSDIA[i]=i+1
################################BOTANDO NO FORMATO DA PREDIÇÃO######################################



####################################################SEPARANDO TREINO E TESTE#####################################
X_train=PONTOSTODOSDIA
y_train=PONTOSTODOSVALOR
X_test=PONTOSTODOSDIA
y_test=PONTOSTODOSVALOR

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
####################################################SEPARANDO TREINO E TESTE#####################################

###############################################TEXTO#####################################################################
import calendar
monthRange = calendar.monthrange(2022,12)      ############  MUDANÇA DE  MÊS


OQUEVAIVENDERNORESTANTEDOMESDEABRIL=0
for i in range((monthRange[1]-datetime.date.today().day)):
    OQUEVAIVENDERNORESTANTEDOMESDEABRIL=OQUEVAIVENDERNORESTANTEDOMESDEABRIL+model.predict([[i+1+PONTOSTODOSDIA.shape[0]]])[0]




###############################################PREDIÇÃO ######################################################################################################
###############################################PREDIÇÃO ######################################################################################################
###############################################PREDIÇÃO ######################################################################################################








#############################################################GRÁFICO 1 E CABEÇALHO############################################
#############################################################GRÁFICO 1 E CABEÇALHO############################################
#############################################################GRÁFICO 1 E CABEÇALHO############################################
MESESDOANO=['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']

from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label
from pandas.core.frame import DataFrame
from bokeh.models import Title
nome=[]
i=0
while i<len(X):
   nome.append(str(y[i]))
   i=i+1

source = DataFrame(
    dict(
        off_rating=X,
        def_rating=y,
        names=nome
    )
)

s1 = figure(min_width=850, min_height=100, title = "RECEITA X DIA"+" "+ str(datetime.date.today().day)+"/"+ str(datetime.date.today().month)+"/"+ str(datetime.date.today().year) +"--"+ str(int(str(datetime.datetime.today().hour-3))-1)+"h"+":"+str(datetime.datetime.today().minute)+"min"+"---DIAS: "+str(len(PONTOSTODOSVALOR)))
s1.vbar(X,top = y, width= .8, alpha=.5, color="green")
s1.xaxis.axis_label = "DIA"
s1.yaxis.axis_label = "RECEITA"


# style the headline
s1.title.text_font_size = "30px"
s1.title.align = "center"
s1.title.background_fill_color = "darkgrey"
s1.title.text_color = "blue"


s1.yaxis.axis_label_text_color = "green"
s1.yaxis.axis_label_text_font_size = "30px"

s1.xaxis.axis_label_text_color = "green"
s1.xaxis.axis_label_text_font_size = "30px"

labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='10pt', x_offset=-10, y_offset=5, source=ColumnDataSource(source))
s1.add_layout(labels)

#############################################################PARA OBTER A QUANTIDADE DE CLIENTES############################################

collection=db['vendas']
resulta=collection.aggregate([ {"$match": {  "estado":{"$eq":1} } },    { "$group": {        "_id": {"placa":"$cliente"}  ,     "receita":{ "$sum":"$total" }   , "servicos":{"$sum":1}             }     },  { "$sort":{"servicos":-1} }       ])
total1=0
for resul in resulta:        
            if (resul['servicos'] >1):
                total1=total1+1



collection=db['clientes']
total2=collection.count_documents({"estado":{"$eq":1}})

#############################################################PARA OBTER A QUANTIDADE DE CLIENTES############################################



 

s1.add_layout(Title(text=str(  "SEG: %.2f "%  max(melhoressemana[1])+      "(%.0f) "%  (melhoressemana[0][0]/7+1)+ "-TER: %.2f "% max(melhoressemana[2])+ "(%.0f) "%  (melhoressemana[0][1]//7+1)+ "-QUA: %.2f "% max(melhoressemana[3])+ "(%.0f) "%  (melhoressemana[0][2]//7+1)+ "-QUI: %.2f "% max(melhoressemana[4])+ "(%.0f) "%  (melhoressemana[0][3]//7+1)+ "-SEX: %.2f "% max(melhoressemana[5])+ "(%.0f) "%  (melhoressemana[0][4]//7+1)+ "-SÁB: %.2f "% max(melhoressemana[6])+ "(%.0f) "%  (melhoressemana[0][5]//7+1)+ "-DOM: %.2f "% max(melhoressemana[7])+ "(%.0f) "%  (melhoressemana[0][6]//7+1) ), text_font_style="bold", text_font_size="10pt", align='center', text_color='blue'), 'above')



s1.add_layout(Title(text=str(  "PLACAS COM LAVAGENS>=2:   %.2f "% total1+"----------CLIENTES: %.2f "% total2 +"----------SEMANA ATUAL: %.0f "% (p//7+1) ), text_font_style="bold", text_font_size="10pt", align='center', text_color='red'), 'above')


s1.add_layout(Title(text=str(  "SOMA ATÉ HOJE:%.2f "% PONTOSTODOSVALOR.sum()+       "----------"+MESESDOANO[datetime.datetime.now().month-1] +      ": %.2f "%(PONTOSTODOSVALOR[146:].sum())+"-------------DIAS RESTANTES: %.0f "%(monthRange[1]-datetime.date.today().day)   ), text_font_style="bold", text_font_size="10pt", align='center', text_color='red'), 'above')


s1.add_layout(Title(text=str(  " 1: %.2f"%(model.predict([[1+PONTOSTODOSDIA.shape[0]]])[0][0]) ) 
                                                       +str( " 2: %.2f"%(model.predict([[2+PONTOSTODOSDIA.shape[0]]])[0][0]) )
                                                       +str( " 3: %.2f"%(model.predict([[3+PONTOSTODOSDIA.shape[0]]])[0][0]) )
                                                       +str( " 4: %.2f"%(model.predict([[4+PONTOSTODOSDIA.shape[0]]])[0][0]) )
                                                       +str( " 5: %.2f"%(model.predict([[5+PONTOSTODOSDIA.shape[0]]])[0][0]) )
                                                       +str( " 6: %.2f"%(model.predict([[6+PONTOSTODOSDIA.shape[0]]])[0][0]) )
                                                       +str( " 7: %.2f"%(model.predict([[7+PONTOSTODOSDIA.shape[0]]])[0][0])       ) 
                                                       
                                                       , text_font_style="bold", text_font_size="10pt", align='center'), 'above')


s1.add_layout(Title(text=str(  "\nPRED. DIAS RESTANTES: %.2f "%OQUEVAIVENDERNORESTANTEDOMESDEABRIL +  "---RECEITA MENSAL: %.2f "%(OQUEVAIVENDERNORESTANTEDOMESDEABRIL+PONTOSTODOSVALOR[146:].sum()) +
                                                       
                                                       "---PROX. 7 DIAS: %.2f"%(   model.predict([[1+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[2+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[3+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[4+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[5+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[6+PONTOSTODOSDIA.shape[0]]])[0][0]  +model.predict([[7+PONTOSTODOSDIA.shape[0]]])[0][0]    )
                                                       
                                                       
                                                          ) 
                                                       
                                                       , text_font_style="bold", text_font_size="10pt", align='center'), 'above')

#############################################################GRÁFICO 1 E CABEÇALHO############################################
#############################################################GRÁFICO 1 E CABEÇALHO############################################
#############################################################GRÁFICO 1 E CABEÇALHO############################################










#############################################################GRÁFICO 2###########################################################
#############################################################GRÁFICO 2###########################################################
#############################################################GRÁFICO 2###########################################################
# barras verticais
# plot.vbar para traçar barras verticais

#fill_color = ["yellow", "pink", "blue"]#, "green", "purple"]

from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label
from pandas.core.frame import DataFrame

nome=[]
i=0
while i<len(XX):
   print("vvvvvvv",i,XX,yy)
   nome.append(str(yy[i]))
   i=i+1
print("vvvvvvvhhhhhh",i,XX,yy)
source = DataFrame(
    dict(
        off_rating=XX,
        def_rating=yy,
        names=nome
    )
)

s2 = figure(x_range=['AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO','JANEIRO'], min_width=850, min_height=300, title = "RECEITA X MÊS")
s2.vbar(XX,top = yy, width= .8, alpha=.5)
s2.xaxis.axis_label = "MÊS"
s2.yaxis.axis_label = "RECEITA"

s2.yaxis.axis_label_text_color = "green"
s2.yaxis.axis_label_text_font_size = "30px"
s2.title.background_fill_color = "darkgrey"

s2.xaxis.axis_label_text_color = "green"
s2.xaxis.axis_label_text_font_size = "30px"


labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='15pt', x_offset=-10, y_offset=5, source=ColumnDataSource(source))
s2.add_layout(labels)


s2.title.text_font_size = "30px"
s2.title.align = "center"

s2.title.text_color = "blue"

#############################################################GRÁFICO 2###########################################################
#############################################################GRÁFICO 2###########################################################
#############################################################GRÁFICO 2###########################################################








######################################################sssssssssss333333333333333333333333333333333#######################################

from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label
from pandas.core.frame import DataFrame

nome=[]
i=0
while i<len(XXX):
   
   nome.append(str(yyy[i]))
   i=i+1





source = DataFrame(
    dict(
        off_rating=XXX,
        def_rating=yyy,
        names=nome
    )
)

s3 = figure(x_range=['AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO','JANEIRO'] ,  min_width=850, min_height=300, title = "SERVIÇOS X MÊS" )
s3.vbar(XXX,top = yyy, width= .8, alpha=.5, color="green")
s3.xaxis.axis_label = "MÊS"
s3.yaxis.axis_label = "SERVIÇOS"

labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='15pt', x_offset=-10, y_offset=5, source=ColumnDataSource(source))


s3.add_layout(labels)

s3.title.background_fill_color = "darkgrey"
s3.title.text_font_size = "30px"
s3.title.align = "center"
s3.title.text_color = "blue"


s3.yaxis.axis_label_text_color = "green"
s3.yaxis.axis_label_text_font_size = "30px"

s3.xaxis.axis_label_text_color = "green"
s3.xaxis.axis_label_text_font_size = "30px"
######################################################sssssssssss3333333333333333333333333333333333333333#######################################










######################################################sssssssssss444444444444444444444444444444444444444#######################################

from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label
from pandas.core.frame import DataFrame


nome=[]
i=0
while i<len(XXXX):
   nome.append(str(yyyy[i]))
   i=i+1


source = DataFrame(
    dict(
        off_rating=XXXX,
        def_rating=yyyy,
        names=nome
    )
)



s4 = figure(min_width=850, min_height=300, title = "RECEITA X SEMANA")
s4.vbar(XXXX,top =yyyy, width= .8, alpha=.5,color="purple")
s4.xaxis.axis_label = "SEMANA"
s4.yaxis.axis_label = "RECEITA"

labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='15pt', x_offset=-10, y_offset=5, source=ColumnDataSource(source))
s4.add_layout(labels)


s4.title.background_fill_color = "darkgrey"
s4.title.text_font_size = "30px"
s4.title.align = "center"
s4.title.text_color = "blue"

s4.yaxis.axis_label_text_color = "green"
s4.yaxis.axis_label_text_font_size = "30px"

s4.xaxis.axis_label_text_color = "green"
s4.xaxis.axis_label_text_font_size = "30px"
######################################################sssssssssss444444444444444444444444444444444444444#######################################



















######################################################sssssssssss5555555555555555555555555555555555555555#######################################


from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label

from pandas.core.frame import DataFrame



nome=[]
i=0
while i<len(XXXXX):
   nome.append(str(yyyyy[i]))
   i=i+1


source = DataFrame(
    dict(
        off_rating=XXXXX,
        def_rating=yyyyy,
        names=nome
    )
)




s5 = figure(min_width=850, min_height=300, title = "SERVIÇOS X SEMANA")
s5.vbar(XXXXX,top =yyyyy, width= .8, alpha=.5,color="blue")
s5.xaxis.axis_label = "SEMANA"
s5.yaxis.axis_label = "SERVIÇOS"

labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='15pt', x_offset=-10, y_offset=5, source=ColumnDataSource(source))
s5.add_layout(labels)


s5.title.background_fill_color = "darkgrey"
s5.title.text_font_size = "30px"
s5.title.align = "center"


s5.title.text_color = "blue"


s5.yaxis.axis_label_text_color = "green"
s5.yaxis.axis_label_text_font_size = "30px"

s5.xaxis.axis_label_text_color = "green"
s5.xaxis.axis_label_text_font_size = "30px"

######################################################sssssssssss555555555555555555555555555555#######################################







######################################################sssssssssss66666666666666666666666666666666666666#######################################
from bokeh.plotting import figure, output_file, show,ColumnDataSource
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label

from pandas.core.frame import DataFrame



nome=[]
i=0
while i<len(X6):
   nome.append(str(y6[i]))
   i=i+1


source = DataFrame(
    dict(
        off_rating=X6,
        def_rating=y6,
        names=nome
    )
)




s6 = figure( min_width=850, min_height=300, title = "NOVOS CLIENTES X SEMANA-10/10/22")
s6.vbar(X6,top =y6, width= .8, alpha=.5)
s6.xaxis.axis_label = "SEMANA"
s6.yaxis.axis_label = "NOVOS CLIENTES"

labels = LabelSet(x='off_rating', y='def_rating', text='names',text_font_size='15pt', x_offset=-10, y_offset=5, source=ColumnDataSource(source))
s6.add_layout(labels)


s6.title.background_fill_color = "darkgrey"
s6.title.text_font_size = "30px"
s6.title.align = "center"
s6.title.text_color = "blue"

s6.yaxis.axis_label_text_color = "green"
s6.yaxis.axis_label_text_font_size = "30px"

s6.xaxis.axis_label_text_color = "green"
s6.xaxis.axis_label_text_font_size = "30px"

######################################################sssssssssss66666666666666666666666666666666666666666666666#######################################




######################################################sssssssssss777777777777777777777777777777777777777777777777######################################

# 54 primeiro de outubro
# 85 1/11/22
# 115 1/12/22
# 146 1/1/23

y7[3]=PONTOSTODOSVALOR[146:].sum()[0]-(y7[0]+y7[1]+y7[2]+y7[4]+y7[5]+y7[6]+y7[7])
if(y7[3]<0):
    y7[3]=0



from math import pi

import pandas as pd

from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

x = {
    'LAVADOR': y7[0],
    'VIGIA': y7[1],
    'DIVERSAS': y7[2],
    'CAIXA': y7[3],
    'PRODUTO': y7[4],
    'EQUIPAMENTO': y7[5],
    'ESTRUTURA': y7[6],
    'ADMINISTRATIVO': y7[7],
   
}


data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]

s7 = figure(width=300, height=150, title="DISTRIBUIÇÃO DA RECEITA: "+str(sum(y7))+"\n                      DEZEMBRO"   , toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

s7.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)





s7.axis.axis_label = None
s7.axis.visible = False
s7.grid.grid_line_color = None


s7.title.background_fill_color = "darkgrey"
s7.title.text_font_size = "30px"
s7.title.align = "center"

s7.title.text_color = "blue"

# change border and background of legend
s7.legend.border_line_width = 3
s7.legend.border_line_color = "navy"
s7.legend.border_line_alpha = 0.8
s7.legend.background_fill_color = "navy"
s7.legend.background_fill_alpha = 0.2




s7.yaxis.axis_label_text_color = "green"
s7.yaxis.axis_label_text_font_size = "30px"

s7.xaxis.axis_label_text_color = "green"
s7.xaxis.axis_label_text_font_size = "30px"

if(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7]>0):
  s7.add_layout(Title(text=str(  "LAVADOR:%.2f "% (int(y7[0]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%" + "VIGIA:%.2f "% (int(y7[1]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%" + "DIVERSAS:%.2f "% (int(y7[2]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%" + "CAIXA:%.2f "% (int(y7[3]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%" + "PRODUTO:%.2f "% (int(y7[4]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%"
     + "EQUIPAMENTO:%.2f "% (int(y7[5]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%"+ "ESTRUTURA:%.2f "% (int(y7[6]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%"+ "ADMINISTRATIVO:%.2f "% (int(y7[7]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4]+y7[5]+y7[6]+y7[7])*10000)/100)+"%"  )     
                             

                                                                  , text_font_style="bold", text_font_size="10pt", align='center', text_color='red'), 'above')

######################################################sssssssssss777777777777777777777777777777777777777777777777######################################


######################################################sssssssssss888888888888888888888888888887######################################

#  + "DIVERSAS:%.2f "% int(y8[2]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4])*100)+"%"  
# + "CAIXA:%.2f "% int(y8[3]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4])*100)+"%"    + "PRODUTO:%.2f "% int(y8[3]/(y7[0]+y7[1]+y7[2]+y7[3]+y7[4])*100)+"%" 

from math import pi

import pandas as pd

from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

x = {
     'LUIS': y8[0],
    'JUNIOR': y8[1],
    'JEFFERSON': y8[2],
  

   
}


data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() *2*pi
data['color'] = Category20c[len(x)]

s8 = figure(width=300,height=150, title="PAGAMENTOS AOS LAVADORES: "+str(sum(y8))+"\n                           NOVEMBRO"                   , toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

s8.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)


s8.axis.axis_label = None
s8.axis.visible = False
s8.grid.grid_line_color = None


s8.title.background_fill_color = "darkgrey"
s8.title.text_font_size = "30px"
s8.title.align = "center"

s8.title.text_color = "blue"

# change border and background of legend
s8.legend.border_line_width = 3
s8.legend.border_line_color = "navy"
s8.legend.border_line_alpha = 0.8
s8.legend.background_fill_color = "navy"
s8.legend.background_fill_alpha = 0.2


if(y8[0]+y8[1]+y8[2]>0):
  s8.add_layout(Title(text=str(  "LUIS:%.2f "% (int(y8[0]/(y8[0]+y8[1]+y8[2])*10000)/100) +"%"+ "(%.2f "%(int(y8[0]))+")---"                  + "JUNIOR:%.2f "% (int(y8[1]/(y8[0]+y8[1]+y8[2])*10000)/100)+"%" + "(%.2f "%(int(y8[1]))+")---"    + "JEFFERSON:%.2f "% (int(y8[2]/(y8[0]+y8[1]+y8[2])*10000)/100)+"%"  + "(%.2f "%(int(y8[2]))+")    "                                                            ), text_font_style="bold", text_font_size="10pt", align='center', text_color='red'), 'above')


#s8.add_layout(Title(     text=str(  "LUIS:%.2f "% str( int(y8[0]/(y8[0]+y8[1])*100)+ "----------GABRIEL: %.2f "%str( int(y8[1]/(y8[0]+y8[1])*100))   )    )  , text_font_style="bold", text_font_size="10pt", align='center', text_color='red'), 'above')

######################################################sssssssssss888888888888888888888888888######################################





######################################################sssssssssss99999999999999999999999999999999999######################################
######################################################sssssssssss99999999999999999999999999999999999######################################
######################################################sssssssssss99999999999999999999999999999999999######################################

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, TableColumn, DataTable
from bokeh.io import show
import pandas as pd

df = pd.DataFrame({
    'lavador':total_Lavador,
    'Servicos': total_Servicos,
    'Receita': total_Receita,
    'Recebimento': total_Recebimento,
    'Porcentagem': total_Percentual,

  

})
  
source = ColumnDataSource(df)

columns = [
    TableColumn(field='lavador', title='LAVADOR'),
    TableColumn(field='Servicos', title='SERVIÇOS'),
    TableColumn(field='Receita', title='RECEITA'),
    TableColumn(field='Recebimento', title='RECEBIMENTO'),
    TableColumn(field='Porcentagem', title='PERCENTUAL'),
    ]


s9 = DataTable(source=source, columns=columns)

######################################################sssssssssss99999999999999999999999999999999999######################################
######################################################sssssssssss99999999999999999999999999999999999######################################
######################################################sssssssssss99999999999999999999999999999999999######################################


######################################################sssssssssss10101010101010101010101010101010######################################
######################################################sssssssssss10101010101010101010101010101010######################################
######################################################sssssssssss10101010101010101010101010101010######################################

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, TableColumn, DataTable
from bokeh.io import show
import pandas as pd


percentual=[]
for resul in quantidade:
    percentual.append(int((resul/quantidade[len(quantidade)-1])*10000)/100)

df = pd.DataFrame({
    'descricao':descricao,
    'Servicos': quantidade,
    'Percentual': percentual,
})
source = ColumnDataSource(df)

columns = [
    TableColumn(field='descricao', title='DESCRIÇÃO'),
    TableColumn(field='Servicos', title='QUANTIDADE'),
    TableColumn(field='Percentual', title='PERCENTUAL'),
    ]

s10 = DataTable(source=source, columns=columns)




# s9.add_layout(Title(text=str(  "LUIS:%.2f "% (int(y8[0]/(y8[0]+y8[1]+y8[2])*10000)/100)+"%    "   + "GABRIEL:%.2f "% (int(y8[1]/(y8[0]+y8[1]+y8[2])*10000)/100)+"%    "     + "JEFFERSON:%.2f "% (int(y8[2]/(y8[0]+y8[1]+y8[2])*10000)/100)+"%"                                                              ), text_font_style="bold", text_font_size="10pt", align='center', text_color='red'), 'above')



######################################################sssssssssss10101010101010101010101010101010######################################
######################################################sssssssssss10101010101010101010101010101010######################################
######################################################sssssssssss10101010101010101010101010101010######################################






######################################################sssssssssss11 11 11 11 11 11 11 11 11 11 11 11 11 11 ######################################
######################################################sssssssssss11 11 11 11 11 11 11 11 11 11 11 11 11 11 ######################################
######################################################sssssssssss11 11 11 11 11 11 11 11 11 11 11 11 11 11 ######################################

# from datetime import date

# from bokeh.io import show
# from bokeh.models import CustomJS, DateRangeSlider

# date_range_slider = DateRangeSlider(value=(date(2016, 1, 1), date(2016, 12, 31)),
#                                     start=date(2022, 1, 1), end=date(2022, 12, 31))
# date_range_slider.js_on_change("value", CustomJS(code="""
#     console.log('date_range_slider: value=' + this.value, this.toString())
# """))

# show(date_range_slider)


######################################################sssssssssss11 11 11 11 11 11 11 11 11 11 11 11 11 11 ######################################
######################################################sssssssssss11 11 11 11 11 11 11 11 11 11 11 11 11 11 ######################################
######################################################sssssssssss11 11 11 11 11 11 11 11 11 11 11 11 11 11 ######################################





output_file("templates/app.html", title="DASHBOARD")

save(gridplot([[s1,s6],[s2,s3],[s4,s5],[s7,s8],[s9,s10]], sizing_mode="scale_width"))



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



# s1.title.background_fill_color = "darkgrey"
# s1.title.text_color = "white"






# put the results in a row that automatically adjusts
# to the browser window's width

#show(row(children=[s1, s2, s3, s4,s5], sizing_mode="scale_width"))



#save(row(children=[s1, s2, s3, s4,s5], sizing_mode="scale_width"))





# from bokeh.layouts import column

 
# from bokeh.io import show
# from bokeh.models import Paragraph


# p0=Paragraph(text="""                                                                                                                       DASHBOARD""",
# width=900, height=30)

# p1 = Paragraph(text=str(  "PRED. DIAS RESTANTES: %.2f "%OQUEVAIVENDERNORESTANTEDOMESDEABRIL +  "---RECEITA MENSAL: %.2f "%(OQUEVAIVENDERNORESTANTEDOMESDEABRIL+PONTOSTODOSVALOR[54:].sum()) +
                                                       
#                                                        "---PROX. 7 DIAS: %.2f"%(   model.predict([[1+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[2+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[3+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[4+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[5+PONTOSTODOSDIA.shape[0]]])[0][0] +model.predict([[6+PONTOSTODOSDIA.shape[0]]])[0][0]  +model.predict([[7+PONTOSTODOSDIA.shape[0]]])[0][0]    )
                                                       
                                                       
#                                                           ) ,
# width=900, height=30)

# p2 = Paragraph(text=str(  " 1: %.2f"%(model.predict([[1+PONTOSTODOSDIA.shape[0]]])[0][0]) ) 
#                                                        +str( " 2: %.2f"%(model.predict([[2+PONTOSTODOSDIA.shape[0]]])[0][0]) )
#                                                        +str( " 3: %.2f"%(model.predict([[3+PONTOSTODOSDIA.shape[0]]])[0][0]) )
#                                                        +str( " 4: %.2f"%(model.predict([[4+PONTOSTODOSDIA.shape[0]]])[0][0]) )
#                                                        +str( " 5: %.2f"%(model.predict([[5+PONTOSTODOSDIA.shape[0]]])[0][0]) )
#                                                        +str( " 6: %.2f"%(model.predict([[6+PONTOSTODOSDIA.shape[0]]])[0][0]) )
#                                                        +str( " 7: %.2f"%(model.predict([[7+PONTOSTODOSDIA.shape[0]]])[0][0])       ) ,
# width=900, height=30)

# p3 = Paragraph(text=str(  "SOMA ATÉ HOJE:%.2f "% PONTOSTODOSVALOR.sum()+"----------TOTAL OUTUBRO: %.2f "%(PONTOSTODOSVALOR[54:].sum())+"-------------DIAS RESTANTES: %.0f "%(monthRange[1]-datetime.date.today().day)   ),
# width=900, height=30)
#save(gridplot([[s1,s2],[s3,s4],[s5,s6],[s7,s8]], sizing_mode="scale_width"))



# save(gridplot([[p],[column(p,s1),s2],[s3,s4],[s5,s6]], sizing_mode="scale_width"))








