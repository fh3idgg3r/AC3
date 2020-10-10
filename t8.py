import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def ac3_defesa_cibernetica():

	primos = "tudo vai dar certo"
	return primos

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host = '192.168.56.1', port = port)
