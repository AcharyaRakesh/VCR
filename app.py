from flask import Flask, render_template, Response, request, redirect, url_for, session,send_file
from vcr import VCR
import time
import shutil
import os
from werkzeug.utils import secure_filename



app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["GET", "POST"])

# <---------- VCR---------->#
@app.route("/vcr",methods=['POST'] )
def vcr():
    return render_template("vcr.html")

@app.route("/Vertual_CR",methods=['POST','GET'])
def Vertual_CR():
        reactent_A = request.form['reactentA']
        reactent_B = request.form['reactentB']
        test_text= reactent_A + "+" + reactent_B
        print(test_text)
        try:
           Result= VCR(test_text)

        except:
            Result="None"
        time.sleep(5)
        return render_template("vcr.html",Result=Result)



# <---------- VCR END ---------->#



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
