from datetime import datetime

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)  # Way to initiate flask instance

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "tupacshakur4566@gmail.com"
app.config["MAIL_PASSWORD"] = ""

db = SQLAlchemy(app)
mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])  # python decorator is a tool to modify class or a function in a certain way
# URL can handle both GET and Post request.
def index():
    # print(request.method)
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form['occupation']

        form = Form(first_name=first_name, last_name=last_name, email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = f"""
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                        }}
                        .container {{
                            max-width: 600px;
                            margin: 0 auto;
                        }}
                        .header {{
                            background-color: #f4f4f4;
                            padding: 20px;
                            text-align: center;
                        }}
                        .content {{
                            padding: 20px;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h2>New Form Submission</h2>
                        </div>
                        <div class="content">
                            <p>Dear {first_name},</p>
                            <p>Thank you for your submission. Here is the data:</p>
                            <ul>
                                <li><strong>Name:</strong> {first_name} {last_name}</li>
                                <li><strong>Date:</strong> {date}</li>
                                <li><strong>Occupation:</strong> {occupation}</li>
                            </ul>
                            <p>Thank you!</p>
                        </div>
                    </div>
                </body>
            </html>
    """

        message = Message(
            subject="New Form Submission",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email],
            html=message_body,
        )

        mail.send(message)

        flash(f"{first_name}, your form was successfully submitted!", "success")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
