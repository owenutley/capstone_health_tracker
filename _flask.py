from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('home.html')
    
@app.route("/entry_view")
def other():
    return render_template('entry_view.html')

@app.route("/hello")
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)