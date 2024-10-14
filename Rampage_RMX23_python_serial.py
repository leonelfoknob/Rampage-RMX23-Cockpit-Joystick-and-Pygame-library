''' Rampage RMX23 Cockpit USB Vibrating Joystick using with pygame library'''

import pygame
import serial
import time

ser = serial.Serial('COM10', 9600)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Wait for serial connection to establish

pygame.init()
joysticks = {}
commands = {}

def joystick():
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
    for joystick in joysticks.values():
        axes = joystick.get_numaxes()

        axis0 = joystick.get_axis(0)
        axis1 = joystick.get_axis(1)
        axis2 = joystick.get_axis(2)
        axis3 = joystick.get_axis(3)

        hat0_0 = joystick.get_hat(0)[0]
        hat0_1 = joystick.get_hat(0)[1]

        button1 = joystick.get_button(0)
        button2 = joystick.get_button(1)
        button3 = joystick.get_button(2)
        button4 = joystick.get_button(3)
        button5 = joystick.get_button(4)
        button6 = joystick.get_button(5)
        button7 = joystick.get_button(6)
        button8 = joystick.get_button(7)
        button9 = joystick.get_button(8)
        button10 = joystick.get_button(9)
        button11 = joystick.get_button(10)
        button12 = joystick.get_button(11)

        commands[0] = axis0
        commands[1] = axis1
        commands[2] = axis2
        commands[3] = axis3
        commands[4] = hat0_0
        commands[5] = hat0_1
        commands[6] = button1
        commands[7] = button2
        commands[8] = button3
        commands[9] = button4
        commands[10] = button5
        commands[11] = button6
        commands[12] = button7
        commands[13] = button8
        commands[14] = button9
        commands[15] = button10
        commands[16] = button11
        commands[17] = button12

        return commands


while True:
    commands = joystick()

    if commands:
        # Convert commands dictionary to a comma-separated string
        command_str = ','.join([str(commands[key]) for key in commands]) + '\n'
        ser.write(command_str.encode())  # Send to Arduino
        time.sleep(0.1)  # Slow down the loop for stability
    # print any command from joystick
    '''print("Axis0 :" + str(commands[0]) + " Axis1 :"+str(commands[1]) + " Axis2 :" + str(commands[2]) 
          +" Axis3 :" + str(commands[3]) + " Hat0_0 :" + str(commands[4]) + " Hat0_1 :"+str(commands[5]) 
          + " But1 :" + str(commands[6]) +" But2 :" + str(commands[7]) +" But3 :" + str(commands[8])
          + " But4 :" + str(commands[9]) +" But5 :" + str(commands[10]) +" But6 :" + str(commands[11])
          + " But7 :" + str(commands[12]) +" But8 :" + str(commands[13]) +" But9 :" + str(commands[14])
          + " But10 :" + str(commands[15]) + " But11 :" + str(commands[16]) + " But12 :" + str(commands[17]))'''