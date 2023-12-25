import can





desired_ids = [167576099, 167576100]

can_filters = [{"can_id": can_id, "can_mask": 0x1FFFFFFF} for can_id in desired_ids]



try:
    # Try to create a Bus using the pcan bustype
    bus = can.interface.Bus(channel='PCAN_USBBUS1', bustype='pcan', bitrate=250000, receive_own_messages=True, can_filters=can_filters)
except Exception as e:
    print("An error has been occured: ", e)
    exit(1)

while True:
    try:
        message = bus.recv()
        print(f"Message: {list(message.data)} - Wind Speed: {wind_speed} - Wind Direction: {wind_direction}")
    except Exception as e:
        print("An exception has occured: ", e)
