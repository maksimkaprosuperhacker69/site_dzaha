from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from flask import *
import os

"""
def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    # Сохраняем учетные данные в файл credentials.json
    gauth.SaveCredentialsFile("credentials.json")

    return gauth
"""
global gauth
gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")
global drive
drive = GoogleDrive(gauth)
def upload_to_google_drive(file_path):
    

    # Создаем объект файла для загрузки
    file_drive = drive.CreateFile({'title': file_path.split("/")[-1]})

    # Устанавливаем контент файла
    file_drive.SetContentFile(file_path)


    return file_drive.Upload()


app = Flask(__name__, template_folder='templates')
app.secret_key = 'whqwqwdq'

@app.route("/")
@app.route("/upload")
def index():
    user_agent = request.headers.get('User-Agent')
    if 'Mobile' not in user_agent:
        return render_template('d_index.html')
    else:
        return render_template('m_index.html')



@app.route("/about")
def about_us():
    user_agent = request.headers.get('User-Agent')
    if 'Mobile' not in user_agent:
        return render_template('d_about_us.html')
    else:
        return render_template('m_about_us.html')


@app.route('/upload', methods = ['POST']) 
def success(): 
 if request.method == 'POST': 
    f = request.files['myfile'] 
    f.save(f.filename) 
    upload_to_google_drive(f.filename)
        

 user_agent = request.headers.get('User-Agent')
 if 'Mobile' not in user_agent:
    os.remove(f.filename)
    return render_template('d_index.html')
 else:
    os.remove(f.filename)
    return render_template('m_index.html')


if __name__ == '__main__': 
    app.run(host='0.0.0.0')
