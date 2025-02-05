import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Налаштування для збереження файлів у статичній папці
UPLOAD_FOLDER = 'static'  # Створюємо папку images в static

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Функція для перевірки дозволених розширень
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    # Отримуємо список фото з папки
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [file for file in files if allowed_file(file)]  # Фільтруємо дозволені файли
    return render_template('index.html', files=files)

# Маршрут для відображення фото
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
