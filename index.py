
import os
from flask import Flask, request

token = "EAATIxNuC12oBAIYeKVagprW3X8xPjywkW1gezbCuPJ4kTBSsEso9DGlrvStpvKzZAb79WYEg3PRH7UbEudbag9RLyZAHOr222gNymIwLdk1ZCjwNjqs0X4JHAr586t9ZAUTDipH7KQEQW2OgDXIRGA5K6WwnP98E6462MIFkJgZDZD"
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def webhook():
    return 'Nothing'



if __name__ == '__main__':
    app.run(debug=True)
