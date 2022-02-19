# Modules #
from ReadWriteMemory import ReadWriteMemory
import time
import keyboard
import math
import subprocess
from subprocess import call
from subprocess import *
import threading

# Install The Following Modules #
# time
# keyboard
# ReadWriteMemory
# math
# subprocess
# threading

def main():
    print("from ReadWriteMemory import ReadWriteMemory")
    print("rwm = ReadWriteMemory()")
    rwm = ReadWriteMemory()
    print("process = rwm.get_process_by_name('ZOMBI.exe')")
    process = rwm.get_process_by_name('ZOMBI.exe')
    process.open()
    print("Getting base Address: 0x400000 + 0x28AF5544")
    print("baseaddress = 0x400000+0x28AF5544")
    baseaddress = 0x400000+0x28AF5544
    print("Process Exeuction Completed!")
    Y_Axis = process.get_pointer(0x00DA4C68)
    X_Axis = process.get_pointer(0x00DA4C60)
    Z_Axis = process.get_pointer(0x00DA4C64)
    VN = process.get_pointer(0x004B5B23) # DO NOT CHANGE
    #Y_AxisR = process.read(Y_Axis)
    #X_AxisR = process.read(X_Axis)
    #Z_AxisR = process.read(Z_Axis)

    Y_AxisW = 250000
    Y_AxisE = -250000
    X_AxisW = 250000
    X_AxisE = -250000
    Z_AxisW = -250000
    Z_AxisE = 250000
    #process.write(VN, 2335719816)
    
    print("""
Keybinds:
Q - UP
E - DOWN

W - Forward
S - Backward
A - Left
D - Right
""")
    def key():
        while True:
            time.sleep(0.2)
            Y_AxisR = process.read(Y_Axis)
            X_AxisR = process.read(X_Axis)
            Z_AxisR = process.read(Z_Axis)
            true_float_up = Y_AxisR + Y_AxisW
            true_float_down = Y_AxisR + Y_AxisE
            true_float_left = X_AxisR + X_AxisW
            true_float_right = X_AxisR + X_AxisE
            true_float_forward = Z_AxisR + Z_AxisW
            true_float_backward = Z_AxisR + Z_AxisE
            a = 59.51364136
            if keyboard.is_pressed('q'):
                process.write(Y_Axis, int(true_float_up))
                #print(Y_AxisR + Y_AxisW)
            if keyboard.is_pressed('e'):
                process.write(Y_Axis, int(true_float_down))
                
                #print(Y_AxisR + Y_AxisW)
            if keyboard.is_pressed('a'):
                process.write(X_Axis, int(true_float_left))
                #print(Y_AxisR + Y_AxisW)
            if keyboard.is_pressed('d'):
                process.write(X_Axis, int(true_float_right))
                
                #print(Y_AxisR + Y_AxisW)
            if keyboard.is_pressed('w'):
                process.write(Z_Axis, int(true_float_forward))
                #print(Y_AxisR + Y_AxisW)
            if keyboard.is_pressed('s'):
                process.write(Z_Axis, int(true_float_backward))
                #print(Y_AxisR + Y_AxisW)
    key()

main()
    
