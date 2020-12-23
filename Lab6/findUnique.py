#!/usr/bin/env python3 
# Name: Shweta Jones(shsujone) 
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)
import math
import sys
class FastAreader :
    def __init__ (self, fname=''):
        """ contructor: saves attribute fname """
        self.fname = fname        
    def doOpen (self):
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)     
    def readFasta (self): 
        header = ''
        sequence = ''
        with self.doOpen() as fileH:     
            header = ''
            sequence = ''
            line = fileH.readline()
            while not line.startswith('>') :
                if not line: # we are at EOF
                    return header, sequence
                line = fileH.readline()
            header = line[1:].rstrip()
            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()
        yield header,sequence
class Boom:
    def __init__(self, seq):
        badChars = ['-', '_' , '.'] #makes a list of chars that are to be removed 
        for i in badChars: #looks for each char within the seq
            seq = seq.replace(i, "") #replaces the char with a white space
        self.seq = seq #saves as self  
    def seqEdit(self):
        """This method is mainly for printing it out later so that the sequence does not contain chars that are invalid"""
        badChars = ['-', '_' , '.'] 
        for i in badChars:
            seq = self.seq.replace(i, "")
        return seq #returns this "valid" sequence   
    def powerSet(self,total):
        """Creates a powerset for the sequence that is run through"""
        allSet = []  #creates empty dictionary
        for counter in range(len(self.seq)): #allows to run till the end of the sequence
            for j in range(counter+1, len(self.seq)+1): #the +1 prevents a empty set ot be printed
                allSet.append(self.seq[counter:j]) #prints from counter till j from the original sequnce to avoid having powersets that are not found within the sequence
        return allSet #returns the powersets for the sequence  
    def uniqueSet (self, allSet, total):
        """Method produces a uniqueset from the powerset of the sequence"""
        allPowerSet = total.copy() #creates a copy of the total powersets so tha tit cannot be edited
        allPowerSet.remove(allSet) #removes the powerset of the sequence from the total powersets
        uniqueSet = set(allSet) - set().union(*allPowerSet) #the difference of the powersets of the sequence and the union of all the powersets determines the uniqeset for that sequence
        return uniqueSet #returns the unique set for that sequence 
    def essentialSet (self, uniqueSet):
        """Method returns the essential set given the unique set of the sequence"""
        nonEssent = [] #creates empty dictionary
        uniqueList = list(uniqueSet) #makes a list of the unique set
        compareList = list(uniqueSet) #makes a list which is a copy of the previous list
        for i in uniqueList: #this for loop produces a list of nonessential sequences
            compareList.remove(i)
            for j in compareList:
                if i in j:
                    if j not in nonEssent:
                        nonEssent.append(j)
            compareList.append(i)
        essentialSet = set(uniqueList) - set(nonEssent) #the essential set is produces by subtracting the uniquelist from the past method with the nonessential sequence list
        return essentialSet #returns the set of essential sequences
def main(inCL=None):
    myReader = FastAreader ()
    total = [] #creates empty list
    organizedAA = [] #creates empty list
    for head , seq in myReader.readFasta(): #the main point of this is to produce a large database of powersets, the total
        organizedAA.append((head[8:11], head, seq)) #creates dictionary made of the amino acid, header and sequence
        sequence = Boom(seq)
        indPow = sequence.powerSet(total)
        total.append(indPow) #adds the individual powersets to the total to create a large set of powersets
    organizedAA.sort() #organizes the dictionary based on the first entry, the amino acid
    for aa, head, seq in organizedAA: #This runs for each sequence which is organized based on amino acid
        print (head) #prints the header sequence
        sequence = Boom(seq)
        print (sequence.seqEdit()) #prints the edited form of the sequence 
        indPow = sequence.powerSet(total) #calcualtes the powerset of the sequence
        indUnq = sequence.uniqueSet(indPow, total) #calculates the uniqeset of the sequence based on total and individual powerset
        indEss = sequence.essentialSet(indUnq) #calcualtes the essentialset based on uniqueset
        posDict = {} #creates empty dictionary
        for i in indEss: #iterates through each essential sequence
            x = seq.find(i) #finds corresponding posiiton in sequence
            if x != -1: #if the sequence if found then it is added to dictionary
                posDict[x] = i
        counter = 0
        for key, value in sorted(posDict.items()):  # totalLst is the dictionary
            print("{0} {1}".format('.'*counter, value)) #allows to be formatted in expected manner
            counter += 1 #allows for the . to add for each sequence
if __name__ == "__main__":
    main()  
