from flask import Flask, render_template, request, jsonify, Response
import cv2
import time
import argparse
import imutils

import sys

#import motor
#import automatique

app = Flask(__name__)
#Motor = motor.MotorDriver()


@app.route('/')
def index():
    return render_template('index.html')






def gen_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in a format suitable for Flask response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




"""

@app.route('/call_function/<int:func_number>', methods=['GET'])
def call_python_function(func_number):
    if func_number == 1:
        motor.forward(Motor)
        print("going forward")
    elif func_number == 2:
        motor.backward(Motor)
        print("going backward")
    elif func_number == 3:
        motor.left(Motor)
        print("going left")
    elif func_number == 4:
        motor.right(Motor)
        print("going right")
    elif func_number == 5:
        motor.stop(Motor)
        print("stopped")
    return "Function called"
@app.route('/update_data', methods=['POST'])
def update_data():
     data = request.get_json()
     x = data['x']
     y = data['y']
     speed = data['speed']
     angle = data['angle']

     # Call your Python function with x, y, speed, and angle
     result = your_python_function(x, y, speed, angle)

     # You can send a response back to the client if needed
     return jsonify({"result": result})


speedref, dirref = 0, 0
def your_python_function(x, y, speed, angle):
     dir_speed(speed,angle,dirref,speedref)
     # Your Python function logic here
     # Perform any necessary computations or operations with the received data
     result = f"Received data: x={x}, y={y}, speed={speed}, angle={angle}"
     return result
def direction(angle):
    # Define the intervals and corresponding cases
    intervals = [
        (0, 12), (12, 34), (34, 56), (56, 78),
        (78, 102), (102, 124), (124, 146), (146, 168),
        (168, 192), (192, 214), (214, 236), (236, 258),
        (258, 282), (282, 304), (304, 326), (326, 348)
    ]
    # Check if the angle is in the last interval
    if 348 <= angle <= 360:
        return 0
    # Check which interval the angle falls into
    for i, (start, end) in enumerate(intervals):
        if start <= angle < end:
            return i
    # If the angle is not in any interval, return -1 or handle as appropriate
    return -1



def dir_speed(speed,angle,dirref,speedref):
    dir=direction(angle)
    if speed < 10:
        motor.stop(Motor)
    else:
        if dir == dirref:
            if abs(speed-speedref)/speedref < 0.1:
                pass
        else:
            motor.toystick(Motor,dir,speed)
            dirref = dir
            speedref = speed

# passage en mode automatique


# detecter le balise


# recherche de balise
def recherche(aruco):
    while not detecter(aruco):
        basculer()


    while distance(aruco)<= 20 :
        avancer()
        if not detecter(aruco):
            recherche()
    demi_tour()


# scanner aruco -> pair/impair?


# demi-tour
"""
@app.route('/vitesse', methods=['GET', 'POST'])
def vitesse():
    result = None
    vitesse = None
    if request.method == 'POST':
        # request.form['vitesse'] retrieves the value associated with the field
        # <input type="number" id="vitesse_input" name="vitesse" required> 
        vitesse = int(request.form['vitesse'])
        vitesse_global = vitesse
    # render_template('index.html', vitesse=vitesse, result=result): 
    # This function call instructs Flask to render the HTML template named 'index.html'. 
    # It passes the variables vitesse and result to the template.
    return render_template('index.html', vitesse=vitesse)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
