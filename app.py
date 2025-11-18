from flask import Flask, render_template, request
from rag import answer_question

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        # TODO: Get query from form and get answer
        
        return render_template("index.html")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
