
# FIRST : set FLASK_APP=server.py #SET .PY TO BE LAUNCHED
# SECOND: set FLASK_ENV=development
# THIRD : set FLASK_DEBUG=1 #DEBUG AND RELOAD
# THEN  : py -m flask run         #START SERVER

# FLASK SERVER
from flask import Flask, render_template, request, redirect
import csv
# render_template : Send the html file, looks for a folder "templates"
# Static folder gets the css and js of my index
app = Flask(__name__)


@app.route("/<string:page_name>")  # Routes http://127.0.0.1:5000/any
def html_page(page_name):
    return render_template(page_name)


# Routes http://127.0.0.1:5000/
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            "Didnt save to database"
    else:
        return "Try again"


def write_to_file(data):  # TXT FILE
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", newline='', mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer = csv.writer(database2, delimiter=",",
                            quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])
