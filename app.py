from flask import Flask, render_template

app = Flask(__name__)     # Way to initiate flask instance


@app.route("/")     # python decorator is a tool to modify class or a function in a certain way
def index():
    return render_template("index.html")


app.run(debug=True, port=5001)
