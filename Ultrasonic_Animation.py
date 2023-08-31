import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import serial
import re
import time
from Moving_Average import *

plt.ion()

serial_port1 = serial.Serial(
    port="COM14",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

fig, ax = plt.subplots(figsize=(15, 12))

x_data = []
y_data = []

S1_data_x=[0,0,0,0,0,0,0,0,0,0]
S2_data_y=[0,0,0,0,0,0,0,0,0,0]
S3_data_x=[0,0,0,0,0,0,0,0,0,0]
S4_data_y=[0,0,0,0,0,0,0,0,0,0]
while True:

    received_data = serial_port1.readline()
    sensor_data = received_data.decode()
    numbers  = re.findall('\d+', sensor_data)
    sensor_data = [int(num) for num in numbers]
    
    x_data = [sensor_data[0], 0, -1 * sensor_data[2],0]
    y_data = [0, sensor_data[1], 0, -1 * sensor_data[0]]
    # x_data=x                                                                                                                                                        
    # y_data=y
    
    S1_data_x.append(x_data[0])
    S1_data_x.pop(0)
    #y1=0
    
    #x2=0
    S2_data_y.append(y_data[1])
    S2_data_y.pop(0)
    
    S3_data_x.append(x_data[2])
    S3_data_x.pop(0)
    #y3=0

    #x4=0
    S4_data_y.append(y_data[0])
    S4_data_y.pop(0)
  
    x_data,y_data=MovingAverage(S1_data_x,S2_data_y,S3_data_x, S4_data_y)
    ax.clear()
    ax.scatter(x_data, y_data, zorder=3)
    ax.plot(0,0,marker="*",ms=50)
    print(x_data + [x_data[0]])
    print(y_data + [y_data[0]])
    tck, u = interpolate.splprep([x_data + [x_data[0]], y_data + [y_data[0]]], s=0)
    unew = np.linspace(0, 1, 1000)
    ultrasonic_shape = interpolate.splev(unew, tck)

    ultrasonic_draw = ax.plot(ultrasonic_shape[0], ultrasonic_shape[1], color='red', lw=2)
    ax.fill(ultrasonic_shape[0], ultrasonic_shape[1], color='lightblue', alpha=0.3)

    ax.axis()

    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    fig.canvas.draw()
    fig.canvas.flush_events()