from flask import Flask,Response
from flask import redirect, url_for, render_template, request
from PIL import Image 
import os
app=Flask(__name__)
app.config['UPLOAD_FOLDER']="C:/Users/arsal/Desktop/anaconda/procure_me/static/images"

@app.route("/home/<name>")
def home(name):
    return render_template("index.html",content=name)
@app.route("/<name>")
def user (name):
    return f"Hello world! <h1> this is the home page of {name} </h1>"

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        usr=request.form["nm"]
        #user=str(usr)+".jpg"
        pic=request.files['img']
        ff_n="test.jpg"
        F_name=os.path.join(app.config['UPLOAD_FOLDER'],ff_n).replace('/',"\\")
        f_name=str(F_name)
        pic.save(f_name)   
        print(f_name)
        if usr=="Arsalan" or usr=="arsalan":
            return render_template("base.html")
            #return redirect(url_for("admin"))
        else: 
            return f"{user} you are not admin!"
    if request.method=="GET":
        return render_template("index.html",content=None)

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Admin Arsalan")) 


if __name__== "__main__":
    app.run(host='192.168.1.103',debug=True)

