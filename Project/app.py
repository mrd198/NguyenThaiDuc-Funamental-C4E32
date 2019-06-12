from flask import Flask, render_template,request,redirect,url_for,session
from app2 import get_all, insert_data_book
app = Flask(__name__)
app.secret_key = 'jjsdkfjkjdkfj515'


@app.route('/', methods = ['POST'])
def post_login():
    tk = request.form.get('name')
    mk = request.form.get('mk')
    if tk == "admin" and mk == "admin":
      session['name'] = request.form.get('name')
      return redirect(url_for("index2"))
    else:
      return "Login false"

@app.route('/book', methods = ['POST'])
def post():
    book_name = request.form.get('name')
    book_price = int(request.form.get('price'))
    insert_data_book(book_name,book_price)
    return redirect(url_for("index2"))

@app.route('/book')
def index2():
    if 'name' in session:
        return render_template("index2.html", dulieu = get_all())
    else:
        return redirect(url_for("index"))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 