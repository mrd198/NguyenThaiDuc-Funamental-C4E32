from flask import Flask, render_template
app = Flask(__name__)


@app.route('/BMI/<int:w>/<int:h>')
def tinh_BMI(w,h):
    he = (h) * 0.01
    BMI = (w) / ((he) * (he))
    if BMI < 16:
        return "BMI:"+str(BMI)+"<br> Severely underweight"
    elif 16 <= BMI <= 18.5:
        return "BMI:"+str(BMI)+"<br> Underweight"
    elif 18.5 <= BMI <= 25:
        return "BMI:"+str(BMI)+"<br> Normal"
    elif 25 <= BMI <=30:
        return "BMI:"+str(BMI)+"<br> Overweight"
    else:
        return "BMI:"+str(BMI)+"<br> Obese"


# @app.route('/BMI/<int:w>/<int:h>')
# def tinh_BMI(w,h):
#     he = (h) * 0.01
#     BMI = (w) / ((he) * (he))
#     if BMI < 16:
#         kq = "Severely underweight"
#     elif 16 <= BMI <= 18.5:
#         kq = "Underweight"
#     elif 18.5 <= BMI <= 25:
#         kq = "Normal"
#     elif 25 <= BMI <=30:
#         kq = " Overweight"
#     else:
#         kq = "Obese"
#     return render_template('bai1.html',data = BMI,result = kq)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 