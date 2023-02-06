from flask import Flask, render_template,request
import json, requests
from pprint import pprint 
app=Flask(__name__)


@app.route('/')
def abrir_site():
    return render_template("site_nomes.html")
@app.route('/pesquisar',methods=['POST'])
def pesquisa():
    ultimo_valor=0
    pen_valor=0
    antipen_valor=0
    try:
        nome=request.form['nome']
        url =f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
        dados=requests.get(url)
        valores=json.loads(dados.content)

        ultimo_valor= valores[0]['res'][-1]['frequencia']
    
        pen_valor=valores[0]['res'][-2]['frequencia']
        
        antipen_valor=valores[0]['res'][-3]['frequencia']

        return render_template('site_nomes.html',z=ultimo_valor,y=pen_valor,x=antipen_valor)
    except:
        print("Data não encontrada")
        return render_template('site_nomes.html',z=ultimo_valor,y=pen_valor,x=antipen_valor)
app.run()
