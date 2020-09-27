from flask import Flask
from flask import redirect, url_for, render_template, request
from PIL import Image 
from flask import Response 
from watsonoop import Watson_identify
from searchoop import Search_google
app=Flask(__name__)
app.config['UPLOAD_FOLDER']="C:/Users/arsal/Desktop/anaconda/procure_me/static/images"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload",methods=["POST","GET"])
def upload_img():
    import os
    if request.method=="POST":
        # resp=Response()
        # resp.headers['X-UA-Compatible']='IE=Edge,chrome=1'
        # resp.headers['Cache-Control'] = 'public, max-age=0'
        #usr=request.form["nm"]
        #user=str(usr)+".jpg"
        pic=request.files['img']
        ff_n="t.jpg"
        F_name=os.path.join(app.config['UPLOAD_FOLDER'],ff_n)
        f_name=str(F_name).replace('\\','/')
        pic.save(f_name)   
        print(f_name)

        #if usr=="Arsalan" or usr=="arsalan":
        return render_template ("img_confirm.html")
    if request.method=="GET":
        return render_template("index.html")

@app.route("/identify",methods=["POST","GET"])
def identify():
    import os
    if request.method=="POST":
        ff_n="t.jpg"
        F_name=os.path.join(app.config['UPLOAD_FOLDER'],ff_n).replace('/',"\\")
        f_name=str(F_name)
        if os.path.exists(f_name):
            print("yes "+f_name+" exists!")
            y= Watson_identify(f_name)
            pre=y.watson_result()
            print(pre)
            dic={'"nuts':"nuts",'"screw':"screw",'"springs':"spring"}
            pr=dic.get(str(pre))
            print(pr)
            reslt= "The file is there and the result is "+str(pr)
            return render_template("watson_result.html",content=reslt), pr
        else:
            print("file "+f_name+" dosent exists :(")
            return "<h1> there is no file</h1>"

# @app.route("/crop")
# def admin():
#     return render_template("cropper2.html") 

@app.route("/lookitup",methods=['POST','GET'])
def lookitup():
    from urllib import parse
    import os
    p,q= identify()
    print(q)
    if request.method=="POST":
        domain=request.form["Domain"]
        Regin=request.form["Region"]
        Hits=request.form["Hits"]
        Site=request.form["Sitename"]
        #return f"<h1> {domain} {Regin} {Hits} {Site} </h1>"

    sr_result=Search_google(q,domain,Hits,Site,Regin)
    res=sr_result.perform_search()
    #res=parse.quote(res)
    print(res)
    return render_template("sr_result.html",content=res)

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Expires'] = '-1'
    return response

if __name__== "__main__":
    app.run(host='192.168.1.101',debug=True) #if phone 192.168.43.46, if home 192.168.1.102

