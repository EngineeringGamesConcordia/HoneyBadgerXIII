'''
Class and methods to manage the passengers and store their information in an object
'''
from coms import SerialComs

class Passengers:
    def __init__(self) -> None:
        #A list with the amount of passangers going to each destination, currently in the blackbox
        destinations = [0,0,0,0,0] #[Red, Green, Blue, Yellow, Purple]
        COLORS = ["RED", "GREEN", "BLUE", "YELLOW", "PURPLE"]
        com = SerialComs("/dev/ttyUSB0", 115200, timeout=1)

    def infoPassengers(self) -> list:
        #send "INFO:S\n"
        message = self.com.info_station()
        #returns "OK:#red:#green:#blue:#yellow:#purple\n"
        #Transform into an list, same format as destinations
        passengerList = [message[3:4], message[5:6], message[7:8], message[9:10], message[11:12]]
        return passengerList

    def take(self):
        """
        Takes the amount of passengers currently in the stop, and does the commands to take them into the black box,
        color by color, while adding them to the list destinations (in memory), 
        """
        destinationsCurrent = self.infoPassengers()
        for i in destinationsCurrent:
            if i != 0:
                #Send "TAKE:{self.COLORS[destinationCurrent.index(i)]}:{i}". Same indexes for color values and the corresponding passangers
                self.com.take(self.COLORS[destinationsCurrent.index(i)], i)
                self.destinations[destinationsCurrent.index(i)] += i



    def send(self, currentStop : str):    #Method will be called in bus, who will check what stop we are at
        """
        This will be part of the main loop: Knowing what the current stop is, it will go through the list of destinations
        and do the commands to send the passangers into the corresponding color/station.
        It also resets the amount of passengers for that station to 0
        """
        for i in self.COLORS:
            if currentStop == i:
                #Send "SEND:{i}:{destiations[self.COLORS.index(i)]}\n". The index of current color is the same as the one for the destinations.
                self.com.send(i, self.destinations[self.COLORS.index(i)])
                self.destinations[i] = 0

        """     OLD CODE FOR EASE OF UNDERSTANDING
        if currentStop == "RED":
            #Send "SEND:RED:{destinations[0]}"
            pass
        if currentStop == "GREEN":
            #Send "SEND:GREEN:{destinations[1]}"
            pass
        if currentStop == "BLUE":
            #Send "SEND:BLUE:{destinations[2]}"
            pass
        if currentStop == "YELLOW":
            #Send "SEND:YELLOW:{destinations[3]}"
            pass
        if currentStop == "PURPLE":
            #Send "SEND:PURPLE:{destinations[4]}"
            pass
        """