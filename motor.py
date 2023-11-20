from PCA9685 import PCA9685

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                print ("1")
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                print ("2")
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("3")
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                print ("4")
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


def forward(Motor):
    Motor.MotorRun(0, 'forward', 100)
    Motor.MotorRun(1, 'backward', 100)

def backward(Motor):
    Motor.MotorRun(0, 'backward', 100)
    Motor.MotorRun(1, 'forward', 100)

def left(Motor):
    Motor.MotorRun(0, 'forward', 100)
    Motor.MotorRun(1, 'forward', 100)

def right(Motor):
    Motor.MotorRun(0, 'backward', 100)
    Motor.MotorRun(1, 'backward', 100)   

def stop(Motor):
    Motor.MotorStop(0)
    Motor.MotorStop(1)
    

# coeff = 0.5
# def run_joystick(Motor,speedx,speedy):
#     if speedx > 0 :
#         if speedy > 0 :
#             Motor.MotorRun(1,'forward', 0.2 * speedx)
#             Motor.MotorRun(0,'backward', 0.2 * speedy)
#         else :
#             Motor.MotorRun(1,'backward', 0.2 * speedx)
#             Motor.MotorRun(0,'backward', 0.2 * abs(speedy))

#     else:
#         if speedy > 0 :
#             Motor.MotorRun(1,'forward', 0.2 * abs(speedx))
#             Motor.MotorRun(0,'forward', 0.2 * speedy)
#         else:
#             Motor.MotorRun(1,'backward', 0.2 * abs(speedx))
#             Motor.MotorRun(0,'forward', 0.2 * abs(speedy))


def toystick(Motor,dir,speed):
    match dir: 
        case 0: #[0,12] [348,360]
            Motor.MotorRun(0,'forward', speed)
            Motor.MotorRun(1,'backward', speed)
        case 1: #[12,34]
            Motor.MotorRun(0,'forward', speed)
            Motor.MotorRun(1,'forward', speed/4)            
        case 2: #[34,56]
            Motor.MotorRun(0,'forward', speed)
            Motor.MotorRun(1,'forward', speed/2)
        case 3: #[56,78]
            Motor.MotorRun(0,'forward', speed)
            Motor.MotorRun(1,'forward', speed*3/4)
        case 4: #[78,102]
            Motor.MotorRun(0,'forward', speed)
            Motor.MotorRun(1,'forward', speed)
        case 5: #[102,124]
            Motor.MotorRun(0,'forward', speed*3/4)
            Motor.MotorRun(1,'forward', speed)
        case 6: #[124,146]
            Motor.MotorRun(0,'forward', speed/2)
            Motor.MotorRun(1,'forward', speed)
        case 7: #[146,168]
            Motor.MotorRun(0,'forward', speed/4)
            Motor.MotorRun(1,'forward', speed)
        case 8: #[168,192]
            Motor.MotorRun(0,'backward', speed)
            Motor.MotorRun(1,'forward', speed)
        case 9: #[192,214]
            Motor.MotorRun(0,'backward', speed/4)
            Motor.MotorRun(1,'backward', speed)
        case 10: #[214,236]
            Motor.MotorRun(0,'backward', speed/2)
            Motor.MotorRun(1,'backward', speed)
        case 11: #[236,258]
            Motor.MotorRun(0,'backward', speed*3/4)
            Motor.MotorRun(1,'backward', speed)
        case 12: #[258,282]
            Motor.MotorRun(0,'backward', speed)
            Motor.MotorRun(1,'backward', speed)
        case 13: #[282,304]
            Motor.MotorRun(0,'backward', speed)
            Motor.MotorRun(1,'backward', speed*3/4)
        case 14: #[304,326]
            Motor.MotorRun(0,'backward', speed)
            Motor.MotorRun(1,'backward', speed/2)
        case 15: #[326,348]
            Motor.MotorRun(0,'backward', speed)
            Motor.MotorRun(1,'backward', speed/4)
        

        
