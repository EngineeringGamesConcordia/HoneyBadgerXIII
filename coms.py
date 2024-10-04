import serial
import time


def take(ser: serial.Serial, color: str, number: int) -> None:
    msg = f"TAKE:{color}:{number}\n"
    ser.write(msg.encode("utf-8"))
    line = ser.readline().decode("utf-8").rstrip()
    print(line)
    # TODO Add handling for TAKE command
    time.sleep(1)


def send(ser: serial.Serial, color: str, number: int) -> None:
    msg = f"SEND:{color}:{number}\n"
    ser.write(msg.encode("utf-8"))
    line = ser.readline().decode("utf-8").rstrip()
    print(line)
    # TODO Add handling for SEND command
    time.sleep(1)


def info(ser: serial.Serial, station: str) -> str:
    msg = f"INFO:{station}\n"
    ser.write(msg.encode("utf-8"))
    msg = ser.readline().decode("utf-8").rstrip()
    print(msg)
    return msg


def secret(ser: serial.Serial, secret_msg: str) -> None:
    # TODO find out what the msg is
    pass
