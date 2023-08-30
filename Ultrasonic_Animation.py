import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import serial
import re

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

while True:

    received_data = serial_port1.readline()
    sensor_data = received_data.decode()
    numbers  = re.findall('\d+', sensor_data)
    sensor_data = [int(num) for num in numbers]
    print(sensor_data)

    x = [sensor_data[0], 0, -1 * sensor_data[2],0]
    y = [0, sensor_data[1], 0, -1 * sensor_data[0]]
    x_data=x
    y_data=y

    ax.clear()
    ax.scatter(x_data, y_data, zorder=3)
    ax.plot(0,0,marker="*",ms=100)

    tck, u = interpolate.splprep([x_data + [x_data[0]], y_data + [y_data[0]]], s=0, per=True)
    unew = np.linspace(0, 1, 100)
    ultrasonic_shape = interpolate.splev(unew, tck)

    ultrasonic_draw = ax.plot(ultrasonic_shape[0], ultrasonic_shape[1], color='red', lw=2)
    ax.fill(ultrasonic_shape[0], ultrasonic_shape[1], color='lightblue', alpha=0.3)

    ax.axis()

    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    fig.canvas.draw()
    fig.canvas.flush_events()