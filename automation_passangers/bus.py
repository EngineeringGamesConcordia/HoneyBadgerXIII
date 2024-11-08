'''
Class and methods to manage the passengers and the connections between the mini-robots and the stations
'''
from passengers import Passengers

class Bus:
    def __init__(self) -> None:
        passengerObj = Passengers()

    def infoStop(self):
        #We get the color of the current station with "INFO:C\n"
        color = self.passengerObj.com.info_color()
        #It returns in "OK:Color\n" format.
        #We check what color it has, and return that color.
        for i in self.passengerObj.COLORS:
            if i in color:
                return i
                break
        

    def connect(self):
        #TODO The function to connect the robot into the station
        pass
   
    def disconnect(self):
        #TODO The function to disconnect the robot from the station
        pass

    def runLoop(self):
        while True:
            #Need to artificially slow down the program?
            self.connect()
            self.passengerObj.take()
            self.passengerObj.send(self.infoStop())     #need for () in infoStop?
            self.disconnect()
            #Move to next station and keep the loop going
            #Probably a button input to start the loop and one to end it