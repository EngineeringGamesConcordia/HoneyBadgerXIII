#!/usr/bin/env python3
import serial
import time
import coms

if __name__ == "__main__":
    com = coms.SerialComs("/dev/ttyUSB0", 115200, timeout=1)

    while True:
        command = input("Enter command (send/take/istat/ibb/icolor/exit): ").strip().lower()
        # Hardcoded values for testing
        if command == "send":
            print(com.send("PURPLE", 1))
        elif command == "istat":
            print(com.info_station())
        elif command == "ibb":
            print(com.info_bb())
        elif command == "icolor":
            print(com.info_color())
        elif command == "take":
            print(com.take("PURPLE", 1))
        else:
            break
    com.close()
