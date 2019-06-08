from flask import Flask, render_template,request,redirect,url_for,session
from a2 import insert,get_all
app = Flask(__name__)


@app.route('/new_bike',methods = ['POST'])
def post():
    name = request.form.get("model")
    fee = request.form.get("daily")
    ima = request.form.get("image")
    yea = request.form.get("year")
    insert(name,fee,ima,yea)
    return redirect(url_for("index"))

@app.route('/new_bike')
def bike():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template("index2.html", data = get_all())
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 