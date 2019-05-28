from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
        users = {
        "huy" : {
            "name" : "Nguyen Quang Huy",
            "age" : 29,
        },
        "tuananh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 22
    }
}



        return render_template('index.html',data = users, data2 = username)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
 
