import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('selecao_volei.html')

@app.route('/selecao')
def index5():
    return render_template('selecao_volei.html')


@app.route('/api/retorno', methods=['POST'])
def retorno():
    json = request.get_json()
    nome = json['nome'].upper()
    time = json['time'].upper()
    combinacao = json['combo'].upper()
    return jsonify(nome=nome, time=time, combo=combinacao)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host='0.0.0.0', port=port)