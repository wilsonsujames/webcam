from flask import Flask, render_template, Response, jsonify
from camera import VideoCamera
from cv2 import cv2 as cv2 

app = Flask(__name__)

video_stream = VideoCamera()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        


@app.route('/')
def index():
    

    return render_template('index.html')



@app.route('/video_feed')
def video_feed():
    print(type(gen(video_stream)))
    print(gen(video_stream))
    

    return Response(gen(video_stream),
                mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")