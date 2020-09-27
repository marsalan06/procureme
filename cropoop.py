from flask import Flask, render_template, url_for,request,redirect,send_from_directory, session, Response
from flask_avatars import Avatars
app=Flask(__name__)
app.secret_key="cropper_tool"
avatars=Avatars(app)
import os
basedir="C:/Users/arsal/Desktop/anaconda/procure_me/static/images"
app.config['AVATARS_SAVE_PATH'] = os.path.join(basedir, 'avatars').replace("\\",'/')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# serve avatar image
@app.route('/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory(app.config['AVATARS_SAVE_PATH'], filename)

#https://flask-avatars.readthedocs.io/en/latest/
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        raw_filename = avatars.save_avatar(f)
        session['raw_filename'] = raw_filename  # you will need to store this filename in database in reality
        return redirect(url_for('crop'))
    return render_template('upload.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    if request.method == 'POST':
        x = request.form.get('x')
        y = request.form.get('y')
        w = request.form.get('w')
        h = request.form.get('h')
        #filenames = avatars.crop_avatar(session['raw_filename'], x, y, w, h)
        filenames = avatars.crop_avatar(session['raw_filename'], x, y, w, h)
        #url_s = url_for('get_avatar', filename=filenames[0])
        #url_m = url_for('get_avatar', filename=filenames[1])
        url_l = url_for('get_avatar', filename=filenames[0])
        return render_template('done.html',url_l=url_l)
    return render_template('croper.html')

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Expires'] = '-1'
    return response

if __name__=="__main__":
    app.run(host='192.168.43.46',debug=True)