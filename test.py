from motor_driver.canmotorlib import *
import time

#create motor obj
#choose any python gui (like tkinter)
#create graphical ui with 3 trackbars that can control the 3 motors.
#also, in the gui print the current position of every motor. 


if __name__ == "__main__":
    motor = CanMotorController(can_socket='can0', motor_id=0x01, motor_type='AK80_6_V2', socket_timeout=0.5)
    position, velocity, current = motor.enable_motor()
    p,v,c = motor.send_deg_command(360, 0, 1, .1, 0)
    print(position, velocity, current)
    start_time = time.time()
    while(time.time() - start_time < 5.0):
        pass
    motor.disable_motor()
