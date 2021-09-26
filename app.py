from flask import Flask, render_template, request

import model2

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def getresult():
    case_data = request.form['case_data']
    numbers = case_data.split(' ')
    data = []
    for i in range(len(numbers)):
        data.append(int(numbers[i]))
    result = model2.pred_values(data)
    return render_template("index.html", case_result=result)
#
# @app.route("/sub", methods=['POST'])
# def submit():
#     if request.method == "POST":
#         case_data = request.form["case_data"]
#     return render_template("submit.html", n=case_data)

if __name__ == "__main__":
    app.run(debug=True)
