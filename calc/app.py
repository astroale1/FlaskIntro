from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
        """Add a and b parameters."""

        a = request.args.get("a",type=int)
        b = request.args.get("b",type=int)

        result = add(a, b)
        return str(result)

@app.route('/sub')
def do_sub():
        "Substract b from a."

        a = request.args.get("a",type=int)
        b = request.args.get("b",type=int)

        result = sub(a,b)
        return str(result)

@app.route('/mult')
def do_mult():
        "Multiply a and b."

        a = request.args.get('a',type=int)
        b = request.args.get('b',type=int)

        result = mult(a,b)
        return str(result)

@app.route('/div')
def do_div():
        a = request.args.get('a',type=int)
        b = request.args.get('b',type=int)

        result = div(a,b)
        return str(result)

operators = {
        'add': add,
        'sub': sub,
        'mult' : mult,
        'div' : div,
}

@app.route('/math/<oper>')
def do_math(oper):
        
        a = request.args.get('a',type=int)
        b = request.args.get('b',type=int)

        result = operators[oper](a,b)
        return str(result)