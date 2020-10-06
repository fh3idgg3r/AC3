import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flash(__name__)

@app.route('/AC3')
def nao_entre_em_panico():

	primos = "Tudo vai dar errado"

	return primos

if __name__ == "__main__"
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)