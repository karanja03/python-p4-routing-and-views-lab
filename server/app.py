#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>Python Operations with Flask Routing and View<h1>'

@app.route('/<string:print/parameter>')
def print_string(parameter):
    return f'<h1>{parameter}<h1>'

@app.route('/<integer:/count/parameter>')
def count(parameter):
    for num in range(parameter):
     num =num+1
    return num

@app.route('/math/<num1><operation><num2>')
def math(num1, operation, num2):
   if (operation == '+'):
    result=(num1+num2)
   elif( operation =='-'):
      result=(num1-num2)
   elif( operation =='*'):
      result=(num1*num2 )
   elif( operation =='div'):
      result=(num1/num2 )
   elif( operation =='%'):
      result=(num1%num2 )



    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
