import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def ac3_defesa_cibernetica():

	maximo = 100

	a = 1
	b = 1
	num = 3

	primo = "2,"

	while b < maximo:
		testeprimo = 1
		for i in range(2, num):
			if num % i == 0:
				testeprimo = 0
				break
		if (testeprimo):
			primo = primo + src(num) + ","
			b += 1
