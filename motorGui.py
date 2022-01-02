from tkinter import *
from tkinter import Tk
from motor_driver.canmotorlib import *
import time

'''

objective:
choose any python gui (like tkinter)
create graphical ui with 3 trackbars that can control the 3 motors.
also, in the gui print the current position of every motor. 

Here are the things to run after connecting the motor:
ip link show
sudo ip link set can0 type can bitrate 1000000
sudo ip link set up can0

'''
# Defines motor position (-720deg to 720deg)
def callbackPos(x):
    #motor.enable_motor()
    p,v,c = motor.send_deg_command(int(x), .8, 5, .5, 3)
    #motor.disable_motor()
    print("Position set to  " + str(x))

# Resets position
def callbackResetPos():
    #motor.enable_motor()
    #p,v,c = motor.send_deg_command(0, 0, 1, .1, 0)
    #motor.disable_motor()
    positionControler.set(0)
    print("Position Reset!")

if __name__ == "__main__":
    #Create a motor object
    motor = CanMotorController(can_socket='can0', motor_id=0x01, motor_type='AK80_6_V2', socket_timeout=0.5)
    #Get current position, velocity, and current
    position, velocity, current = motor.enable_motor()
    motor.set_zero_position()
    #p,v,c = motor.send_deg_command(360, 0, 1, .1, 0)
    print(position, velocity, current)
    start_time = time.time()
    while(time.time() - start_time < 5.0):
        pass
    #

    #initializes the GUI
    # .pack() = push to GUI
    root = Tk()
    root.geometry("500x500")
    root.title("Motor Controller")

    #create window
    #frame = Frame(root)
    #frame.pack()

    #Creates label
    var = StringVar()
    var.set("Motor 1 Position")
    label = Label(root, textvariable=var)
    label.place(x=45,y=80)

    #Creates Text box
    positionText = Button(root, text="Reset Position", command=callbackResetPos)
    positionText.place(x=300,y=310)


    #Creates speed controler
    positionControler = Scale(root, from_=-90, to=90, orient=HORIZONTAL, command=callbackPos)
    positionControler.place(x=45,y=100,relwidth=.8)

    #finalizes GUI
    root.mainloop()
    
    motor.disable_motor()
    print("quit")