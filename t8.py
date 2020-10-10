import os

app = Flask(__name__)

limite = 600
c = 1
p = 0

for numero in range(2, limite+1):
    for i in range(2,numero):
        if numero % i == 0: break
        c += 1
    else:
        print (numero,)
        p += 1

return ("\n\nEncontramos %d números primos hihi." %p)

if __name__ = "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

