from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("./index.html")

@app.route("/<string:page_name>")
def view_page(page_name):
    return render_template(page_name+".html")

def write_to_file_txt(data):
    try:
        with open ("database.txt", "a") as my_file:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            my_file.write(f"\n{email}, {subject}, {message}")
    except:
        return "Something went wrong"

def write_to_file_csv(data):
    with open ("db.csv", "a", newline='', encoding='utf-8') as my_csv_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(my_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def form_submitted():
    if request.method == "POST":
        try:
            database = request.form.to_dict()
            write_to_file_csv(database)
            return redirect("/thank_you")
        except:
            return "Unable to save data."
    else:
        return "Something went wrong."


app.run(debug=True)