#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:40:29 2023

@author: edgibara
"""


from flask import Flask
import json
from flask import request
app= Flask(__name__)

@app.route('/myapi',methods=['POST','GET']) #Prepara o url localhost:5000/myapi com permissao pra post e get
def calc(): #Calcula usando valores dados pelo usr
    data=request.get_json() #Pega o json passado pelo curl
    n=data["val"] 
    a=fibonacci(int(n))
    b=fatorial(int(n))
    ans={"Fibonacci":str(a),"Fatorial":str(b)} #Crua um dict com os resultados
    json_string=json.dumps(ans) #Transforma o dict em uma string no formato para o json
    return json.loads(json_string) #Cria o json a partir da string e retorna
def fibonacci(n:int): #Calcula o numero n na seq de fibonacci. Mas, possui limitacao nos valores aceitos
    a1=1
    a2=1
    if n<=0 or n>30:
        raise(ValueError)
    if n==1:
        return a1
    if n==2:
        return a2
    if n>1:
        return fibonacci(n-1)+fibonacci(n-2)
def fatorial(n:int): # Calcula n! Mas, possui limitacao nos valores aceitos
    if n<0 or n>20:
        raise(ValueError)
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)

#Alternativa a "flask run" + "export FLASK_APP=app2" usada em testes
# if __name__ == '__main__':
#     app.run(debug=True)
