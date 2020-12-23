#!/usr/bin/env python3 
# Name: Shweta Jones(shsujone)
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)

"""Parse sequence name information from single line of a FASTQ formatted file"""
class FastqString (str):
    """The class takes in the fastQ input and stores it as a str"""
    def parse(self):
        """The function takes in the input and outputs the information stored in the FastQ and prints out the parsed sequence"""
        print ("Instrument = " + self[self.find('@')+1:self.find(':')]) #prints out the information from the  to the first colon
        secondColon = self.find(':', self.find(':')+1) #finds the second instance of : - https://www.stackoftuts.com/python-3/python-find-nth-occurrence/
        print ("Run ID = " + self[self.find(':')+1:secondColon]) #print out the information from the first colon to second colon
        thirdColon = self.find(':', secondColon+1) #finds third instance of :
        print ("Flow Cell ID = " + self[secondColon+1:thirdColon]) #prints information between second to third colon
        fourthColon = self.find(':', thirdColon+1) #finds fourth instance of :
        print ("Flow Cell Lane = " + self[thirdColon+1:fourthColon]) #prints information between third to fourth colon
        fifthColon = self.find(':', fourthColon+1) #finds fifth instance of :
        print ("Tile Number = " + self[fourthColon+1:fifthColon]) #prints information between fourth and fifth colon
        sixthColon = self.find(':', fifthColon+1) #finds sixth instance of :
        print ("X-coord = " + self[fifthColon+1:sixthColon]) #prints information between fifth and sixth colon
        seventhColon = self.find(':', sixthColon+1) #finds the seventh of :
        print ("Y-coord = " + self[sixthColon+1:]) #prints information between sixth and the end of the sequence
        
def main():
    """The input for this function is the fastQ which is then sent to the class and then to the parse function"""
    fastQ = input ("What's the seqname line of a FASTQ file?") #saves the user's input into variable fastq
    data = FastqString(fastQ) #this data is sent to the Fastqstring class 
    answer = data.parse() #gives the str to the parse method in order to parse the fastQ seqname

main()

