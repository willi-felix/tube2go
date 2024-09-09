from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

# Trang chủ để người dùng nhập URL YouTube
@app.route('/')
def index():
    return render_template('index.html')

# Xử lý tải video hoặc âm thanh từ URL
@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format_type = request.form['format']
    
    yt = YouTube(url)
    
    if format_type == 'video':
        # Tải video với độ phân giải cao nhất
        stream = yt.streams.get_highest_resolution()
    else:
        # Tải chỉ âm thanh
        stream = yt.streams.filter(only_audio=True).first()
    
    # Tải file về máy chủ
    stream.download()

    # Đường dẫn tới file đã tải về
    file_path = stream.default_filename

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
