from flask import Flask, render_template

app = Flask(__name__)

# Trasa główna "/" - dynamiczna strona główna
@app.route("/")
def home():
    return render_template("index.html")

# Trasa "/about" - strona informacyjna
@app.route("/about")
def about():
    return "To jest strona About!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
