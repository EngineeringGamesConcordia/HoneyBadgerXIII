from serial import Serial
import time
import re


class SerialComs:
    def __init__(self, port: str, baudrate: int, *args, **kwargs):
        self.ser = Serial(port, baudrate, *args, **kwargs)
        self.ser.reset_input_buffer()

    def _buffer_com(self, msg: str) -> str:
        self.ser.write(msg.encode("utf-8"))
        time.sleep(1)
        return self.ser.read(self.ser.in_waiting).decode("utf-8").strip()

    def take(self, color: str, number: int) -> None:
        msg = f"TAKE:{color}:{number}\n"
        # TODO Add handling for TAKE command
        return self._buffer_com(msg)

    def send(self, color: str, number: int) -> None:
        msg = f"SEND:{color}:{number}\n"
        # TODO Add handling for SEND command
        return self._buffer_com(msg)

    def info_station(self) -> str:
        return self._buffer_com(f"INFO:S\n")

    def info_bb(self) -> str:
        return self._buffer_com(f"INFO:B\n")

    def info_color(self) -> str:
        return self._buffer_com(f"INFO:C\n")

    def secret(self, secret_msg: str) -> None:
        # TODO find out what the msg is
        pass

    def close(self) -> None:
        self.ser.close()
