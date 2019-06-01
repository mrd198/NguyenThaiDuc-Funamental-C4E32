from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

data = [
    {'Username':'duc335','Password':'12051997'},
    {'Username':'mrd198','Password':'12051998'}
    ]
@app.route('/', methods = ['POST'])
def post():
    user = request.form.get('Username')
    mk = request.form.get('Password')
    for i in data:
      if user in i['Username'] and mk in i['Password']:
        return "Login Successful!"
      else:
        return "Login Failed!"
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html',dulieu = data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 