from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

# Trang chủ để người dùng nhập URL YouTube
@app.route('/')
def index():
    return render_template('index.html')

# Xử lý tải video từ URL
@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    
    # Tải video với độ phân giải cao nhất
    video = yt.streams.get_highest_resolution()
    video.download()

    # Đường dẫn tới video tải về
    video_path = video.default_filename
    
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
