from flask import Flask, render_template, request, jsonify
from math import sqrt

app = Flask(__name__)

def equation(a, b, c):
    # D - discriminant
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        return [((-b) + sqrt(b ** 2 - 4*a*c)) / (2 * a), ((-b) - sqrt(b ** 2 - 4*a*c)) / (2 * a)]
    elif D == 0:
        return [str(-b/(2*a))]
    else:
        return ""

# Decorator to tell Flask what URL should trigger our function
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        f = request.form
        print(f)
        a = f.get("a")
        b = f.get("b")
        c = f.get("c")
        try:
            # Returns HTTP Response with a, b, c
            return jsonify(equation(float(a), float(b), float(c)))
        except:
            return jsonify(False)

app.run(host='localhost')