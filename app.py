
from flask import Flask, request

token = "EAATIxNuC12oBAIYeKVagprW3X8xPjywkW1gezbCuPJ4kTBSsEso9DGlrvStpvKzZAb79WYEg3PRH7UbEudbag9RLyZAHOr222gNymIwLdk1ZCjwNjqs0X4JHAr586t9ZAUTDipH7KQEQW2OgDXIRGA5K6WwnP98E6462MIFkJgZDZD"
FB_VERIFY_TOKEN = "TESTE123"
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode())
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}}
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            print(traceback.format_exc())
    elif request.method == 'GET': # Para a verificação inicial
        if request.args.get('hub.verify_token') == FB_VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
    return "Nothing"



if __name__ == '__main__':
    app.run(debug=True)
