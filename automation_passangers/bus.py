'''
Class and methods to manage the passengers and the connections between the mini-robots and the stations
'''
from passengers import Passengers

class Bus:
    def __init__(self) -> None:
        passengerObj = Passengers()

    def infoStop(self):
        #We get the color of the current station with "INFO:C\n"
        #It returns in "OK:Color\n" format.
        #Make it return as an string directly, example : "RED"
        pass

    def connect(self):
        #The function to connect the robot into the station
        pass
   
    def disconnect(self):
        #The function to disconnec the robot from the station
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