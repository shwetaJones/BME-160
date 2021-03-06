#!/usr/bin/env python3 
# Name: Shweta Jones(shsujone) 
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)

"""Read a DNA string from user input and returns a collapsed substring of embedded Ns to: {count}."""
class DNAstring (str):
    """The class takes in the DNA data and stores it"""
    def purify(self):
        """Return an upcased version of the string, collapsing a single run of Ns"""
        upperDNA = self.upper() #made the DNA all uppercase
        nFirst = upperDNA.find('N') #finds the first instance of N
        nCount = upperDNA.count('N') #counts the number of N's within the sequence
        if nCount == 0: #if the number of N's are 0, then the uppercase translated version of the DNA sequence is printed
            print (upperDNA)
        else: #if the number of N's are greater than 0, the substring with the N count replaces the N's
            print(upperDNA[:nFirst] +"{"+ str (nCount) +"}"+ upperDNA[(nFirst+nCount):] )#enables for the N's to be collapsed to the number of N's - https://www.pythoncentral.io/one-line-if-statement-in-python-ternary-conditional-operator/
    
def main():
    """Get user DNA data and clean it up"""
    data = input('DNA data?') #the user input is saved as data 
    thisDNA = DNAstring (data) #this data is saved as a string within the DNAstring class
    pureData = thisDNA.purify() #runs the str through the purify method which purifies the sequence
    
main()