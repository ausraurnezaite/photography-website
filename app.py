from flask import Flask, flash, redirect, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "secret_key"

app.config["MAIL_DEFAULT_SENDER"] = 'nesamoniuemailas@gmail.com'
app.config["MAIL_USERNAME"] = 'nesamoniuemailas@gmail.com'
app.config["MAIL_PASSWORD"] = 'nesamoniupastas'
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True

mail = Mail(app)


@ app.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        if not name or not email or not message:
            flash("ALL FIELDS REQUIRED!")
        msg = Message("Name: " + name + " Email: " + email,
                      recipients=['nesamoniuemailas@gmail.com'])
        msg.body = message
        mail.send(msg)
        flash("I WILL GET BACK TO YOU SHORTLY!")
        return redirect("/contacts")
    else:
        return render_template("contacts.html")


@ app.route("/")
def index():
    return render_template("index.html")


@ app.route("/portraits")
def portraits():
    return render_template("portraits.html")


@ app.route("/landscapes")
def landscapes():
    return render_template("landscapes.html")
