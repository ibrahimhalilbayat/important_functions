import os 
import can 

os.system('sudo ip link set can0 up type can bitrate 250000')
bus = can.Bus(channel='can0', interface='socketcan')

while True:
    try:
        message = bus.recv()
        if str(message.arbitration_id) == 1234:

            print("MESSAGE: ", list(message.data), message.data)
    except Exception as e:
        print("an exception occured: ", e)