from flask import Flask,render_template,request
from flask_mail import Mail, Message
import os


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config["MAIL_USE_SSL"] = False
app.config['MAIL_USERNAME'] = 'studentacademichelper@outlook.com'
app.config['MAIL_PASSWORD'] = 'Academichelper'
app.config['MAIL_DEFAULT_SENDER'] = ('Studentacademichelper', 'studentacademichelper@outlook.com')

mail = Mail(app)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/online-class',methods=['GET','POST'])
def online_class():
    return render_template('online_class.html')

@app.route('/online-course',methods=['GET','POST'])
def online_course():
    return render_template('/online_course.html')

@app.route('/online-exam',methods=['GET','POST'])
def online_exam():
    return render_template('/online_exam.html')

@app.route('/terms-conditions',methods=['GET','POST'])
def terms_conditions():
    return render_template('terms-conditions.html')


@app.route('/contact-us',methods=['GET','POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['contact_name']
        email = request.form['contact_email']
        number = request.form['contact_number']
        msgs = request.form['contact_msg']
        # print('----------------------------------------')
        # print(name)
        # print(email)
        # print(number)
        # print(msgs)
        # print('---------------------')
        try:
            msg = Message('Studentacademichelper', recipients =  [email,'studentacademichelper@outlook.com'])
            msg.html = " " +name +" <br> " + " phone :"+number+ "<br>" + msgs
            mail.send(msg)
            return render_template('thank-you.html')
        except Exception as e:
            return render_template('contact-us.html',response=str(e))
    else:
        return render_template('contact-us.html')

if __name__ == '__main__':
    app.run(debug=True)