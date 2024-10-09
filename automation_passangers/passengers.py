'''
Class and methods to manage the passengers and store their information in an object
'''
class Passengers:
    def __init__(self) -> None:
        #A list with the amount of passangers going to each destination, currently in the blackbox
        destinations = [0,0,0,0,0] #[Red, Green, Blue, Yellow, Purple]
        COLORS = ["RED", "GREEN", "BLUE", "YELLOW", "PURPLE"]

    def infoPassengers(self) -> list:
        #send "INFO:S\n"
        #returns "OK:#red:#green:#blue:#yellow:#purple\n"
        #Transform into an list, same format as destinations
        pass

    def take(self):
        """
        Takes the amount of passengers currently in the stop, and does the commands to take them into the black box,
        color by color, while adding them to the list destinations (in memory), 
        """
        destinationsCurrent = self.infoPassengers()
        for i in destinationsCurrent:
            if i != 0:
                #Send "TAKE:{self.COLORS[destinationCurrent.index(i)]}:{i}". Same indexes for color values and the corresponding passangers
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