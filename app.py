# Импортируем необходимые модули
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from flask import *
import os

# Создаем экземпляр GoogleAuth и аутентифицируемся через командную строку
try:
    gauth = GoogleAuth()
    gauth.CommandLineAuth()

# Создаем экземпляр GoogleDrive, используя аутентификацию
    drive = GoogleDrive(gauth)
except:
    os.remove("credentials.json")
# Функция для загрузки файла на Google Drive
def upload_to_google_drive(file_path):
    
    # Создаем объект файла для загрузки
    file_drive = drive.CreateFile({'title': file_path.split("/")[-1]})
    
    # Устанавливаем контент файла
    file_drive.SetContentFile(file_path)

    # Загружаем файл и возвращаем результат загрузки
    return file_drive.Upload()


# Создаем экземпляр Flask приложения
app = Flask(__name__, template_folder='templates')

# Устанавливаем секретный ключ для защиты сессий
app.secret_key = 'whqwqwdq'

# Определяем маршруты приложения
@app.route("/")
@app.route("/upload")
def index():
    # Получаем информацию о User-Agent для определения типа устройства
    user_agent = request.headers.get('User-Agent')
    if 'Mobile' not in user_agent:
        # Если это не мобильное устройство, отображаем десктопную версию страницы
        return render_template('d_index.html')
    else:
        # Если это мобильное устройство, отображаем мобильную версию страницы
        return render_template('m_index.html')

@app.route("/about")
def about_us():
    # Получаем информацию о User-Agent для определения типа устройства
    user_agent = request.headers.get('User-Agent')
    if 'Mobile' not in user_agent:
        # Если это не мобильное устройство, отображаем десктопную версию страницы "О нас"
        return render_template('d_about_us.html')
    else:
        # Если это мобильное устройство, отображаем мобильную версию страницы "О нас"
        return render_template('m_about_us.html')

# Маршрут для загрузки файла на сервер
@app.route('/upload', methods=['POST']) 
def success(): 
    if request.method == 'POST': 
        # Получаем файл из запроса
        f = request.files['myfile'] 
        
        # Сохраняем файл на сервере
        f.save(f.filename) 
        
        # Загружаем файл на Google Drive
        upload_to_google_drive(f.filename)
        
        # Удаляем файл с сервера
        os.remove(f.filename)
        
        # Получаем информацию о User-Agent для определения типа устройства
        user_agent = request.headers.get('User-Agent')
        if 'Mobile' not in user_agent:
            # Если это не мобильное устройство, возвращаем десктопную версию главной страницы
            return render_template('d_index.html')
        else:
            # Если это мобильное устройство, возвращаем мобильную версию главной страницы
            return render_template('m_index.html')

# Запускаем Flask приложение
if __name__ == '__main__': 
    app.run(host='0.0.0.0')
