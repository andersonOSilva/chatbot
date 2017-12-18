
from flask import Flask, request

token = "EAATIxNuC12oBAIYeKVagprW3X8xPjywkW1gezbCuPJ4kTBSsEso9DGlrvStpvKzZAb79WYEg3PRH7UbEudbag9RLyZAHOr222gNymIwLdk1ZCjwNjqs0X4JHAr586t9ZAUTDipH7KQEQW2OgDXIRGA5K6WwnP98E6462MIFkJgZDZD"
FB_VERIFY_TOKEN = "TESTE123"
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        pass
    elif request.method == 'GET': # Para a verificação inicial
        if request.args.get('hub.verify_token') == FB_VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
    return "Nothing"



if __name__ == '__main__':
    app.run(debug=True)
