#!/usr/bin/env python3
# Name: Shweta Jones(shsujone)
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)

class OrfFinder:
    def __init__(self, seq):
        self.seq = seq #saves sequence as self to be accessed in other methods
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} ##https://codereview.stackexchange.com/questions/151329/reverse-complement-of-a-dna-string - allows to determine the complementary reverse strand for given sequence 
        self.revSeq = ''.join([complement[base] for base in seq[::-1]]) #saves sequence as self to be accessed later
    
    def frameOne (self):
        """This method uses the initial sequence to determine the ORF in the +1 coding frame"""
        finalList = [] #creates empty list
        j = 0 #sets j to 0
        i = 0 #sets i to 0
        startVal = 0 #sets startVal to 0
        for i in range(0,len(self.seq),3): #for loop iterates through length of sequence and goes every three positions
            sectList = [] #creates empty list 
            frame = "+1" #frame is set to string +!
            if ((self.seq[i:i+3]== "ATG")
                or (self.seq[i:i+3]== "TTG") 
                or (self.seq[i:i+3]== "GTG")) : #https://stackoverflow.com/questions/13114246/how-to-find-a-open-reading-frame-in-python - Looks for any of the start codons
                startVal = 1 #sets startVal to one to show that start codon is present
                pos1 = i #start posiotn is set to i value which is the start codon position
                j = i #j or the positon where end codon could be is set to the position of i to make sure it doesn't iterated over code again
                pos2 = 0 #end position is set to 0 
                for j in range (j, len(self.seq), 3): #iterates through sequence to find end codon
                    if ((self.seq[j:j+3]== "TAA") 
                        or (self.seq[j:j+3]== "TAG") 
                        or (self.seq[j:j+3]== "TGA")) : #Looks for end codon
                        pos2 = j+3 #end position is set to end position +3 to include the entire end codon
                if pos2 == 0 : #In the situation where there is no end codon if loop runs
                    pos2 = len(self.seq) #end position is set to length of the sequence to account for downstream end codons
                orfLength = pos2 - pos1 #orf length is detemrined through end and start position
                sectList.append(frame) #frame is added to list
                sectList.append(str(pos1+1) + "..") #position one is added to list 
                sectList.append(pos2) #position 2 is added to list
                sectList.append(orfLength) #length of ORF is added to list
                finalList.append(sectList) #this list is added to finalList 
        if startVal == 0:
            sectList = [] #creates empty list
            pos1 = 0 #start position is set to 0
            k = 0 #k, or end codon iteration value is set to 0
            pos2 = 0 #end position is set to 0
            for k in range (k, len(self.seq), 3): #iterates through sequence to find end codon
                if ((self.seq[k:k+3]== "TAA") 
                    or (self.seq[k:k+3]== "TAG")
                    or (self.seq[k:k+3]== "TGA")) : #Looks for end codon
                    pos2 = k +3 #end position is set to end position +3 to include the entire end codon
            if pos2 == 0 : #Start and no end
                pos2 = len(self.seq) #end position is set to length of the sequence to account for downstream end codons
            orfLength = pos2 - pos1 #orf length is detemrined through end and start position
            sectList.append(frame) #frame is added to list
            sectList.append(str(pos1+1) + "..") #position one is added to list 
            sectList.append(pos2) #position 2 is added to list
            sectList.append(orfLength) #length of ORF is added to list
            finalList.append(sectList) #this list is added to finalList
        return (finalList) #finalList is returned
    
    def frameTwo (self):
        finalList = [] #creates empty list
        j = 0 #sets j to 0
        i = 0 #sets i to 0
        startVal = 0 #sets startVal to 0
        for i in range(1,len(self.seq),3): #for loop iterates through length of sequence and goes every three positions
            sectList = [] #creates empty list
            frame = "+2" #sets frame to string +2
            if ((self.seq[i:i+3] == "ATG") 
                or (self.seq[i:i+3] == "TTG") 
                or (self.seq[i:i+3] == "GTG")) : #Looks for start codon
                startVal = 1 #sets startVal to one to show that start codon is present
                pos1 = i
                j = i #j or the positon where end codon could be is set to the position of i to make sure it doesn't iterated over code again
                pos2 = 0 #sets end position to 0
                for j in range (j, len(self.seq), 3): #iterates through sequence to find end codon
                    if ((self.seq[j:j+3] == "TAA") 
                        or (self.seq[j:j+3] == "TAG") 
                        or (self.seq[j:j+3] == "TGA")) : #Looks for end codon
                        pos2 = j+3 #end position is set to end position +3 to include the entire end codon
                if pos2 == 0 : #Start and no end
                    pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
                orfLength = pos2 - pos1 #orf length is detemrined through end and start position
                sectList.append(frame) #frame is added to list
                sectList.append(str(pos1+1) + "..") #position one is added to list 
                sectList.append(pos2) #position 2 is added to list
                sectList.append(orfLength) #length of ORF is added to list
                finalList.append(sectList) #this list is added to finalList
        if startVal == 0:
            sectList = [] #creates empty list
            pos1 = 0 #sets end position to 0
            k = 1 #k value, which is end codon iteration is set to 1
            pos2 = 0 #end position is set to 0
            for k in range (k, len(self.seq), 3): #iterates through sequence to find end codon
                if ((self.seq[k:k+3] == "TAA")
                    or (self.seq[k:k+3] == "TAG")
                    or (self.seq[k:k+3] == "TGA")) : #Looks for end codon
                    pos2 = k + 3 #end position is set to end position +3 to include the entire end codon
            if pos2 == 0 : #Start and no end
                pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
            orfLength = pos2 - pos1 #orf length is detemrined through end and start position
            sectList.append(frame) #frame is added to list
            sectList.append(str(pos1+1) + "..") #position one is added to list 
            sectList.append(pos2) #position 2 is added to list
            sectList.append(orfLength) #length of ORF is added to list
            finalList.append(sectList) #this list is added to finalList
        return (finalList) #finalList is returned
    
    def frameThree (self):
        finalList = [] #creates empty list
        j = 0 #sets j to 0
        i = 0 #sets i to 0
        startVal = 0 #sets startVal to 0
        for i in range(2,len(self.seq),3): #for loop iterates through length of sequence and goes every three positions
            sectList = [] #creates empty list
            frame = "+3" #sets frame to string +3
            if ((self.seq[i:i+3] == "ATG") 
                or (self.seq[i:i+3] == "TTG") 
                or (self.seq[i:i+3] == "GTG")) : #Looks for start codon
                startVal = 1 #sets startVal to one to show that start codon is present
                pos1 = i #start position is set to the position of the i value which finds the start codon position
                j = i #j or the positon where end codon could be is set to the position of i to make sure it doesn't iterated over code again
                pos2 = 0 #end position is set to 0
                for j in range (j, len(self.seq), 3): #iterates through sequence to find end codon
                    if ((self.seq[j:j+3] == "TAA") 
                        or (self.seq[j:j+3] == "TAG") 
                        or (self.seq[j:j+3] == "TGA")) : #Looks for end codon
                        pos2 = j + 3 #end position is set to end position +3 to include the entire end codon
                if pos2 == 0 : #Start and no end
                    pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
                orfLength = pos2 - pos1 #orf length is detemrined through end and start position
                sectList.append(frame) #frame is added to list
                sectList.append(str(pos1+1) + "..") #position one is added to list 
                sectList.append(pos2) #position 2 is added to list
                sectList.append(orfLength) #length of ORF is added to list
                finalList.append(sectList) #this list is added to finalList
        if startVal == 0:
            sectList = [] #creates empty list
            pos1 = 0 #start position is set to 0
            k = 2 #k value, which is end codon iteration is set to 2
            pos2 = 0 #end position is set to 0
            for k in range (k, len(self.seq), 3): #iterates through sequence to find end codon
                if ((self.seq[k:k+3] == "TAA")
                    or (self.seq[k:k+3] == "TAG")
                    or (self.seq[k:k+3] == "TGA")) : #Looks for end codon
                    pos2 = k + 3 #end position is set to end position +3 to include the entire end codon
            if pos2 == 0 : #Start and no end
                pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
            orfLength = pos2 - pos1 #orf length is detemrined through end and start position
            sectList.append(frame) #frame is added to list
            sectList.append(str(pos1+1) + "..") #position one is added to list 
            sectList.append(pos2) #position 2 is added to list
            sectList.append(orfLength) #length of ORF is added to list
            finalList.append(sectList) #this list is added to finalList
        return (finalList) #finalList is returned
    
    def frameMOne (self):
        finalList = [] #creates empty list
        j = 0 #sets j to 0
        i = 0 #sets i to 0
        startVal = 0 #sets startVal to 0
        for i in range(0,len(self.revSeq),3): #for loop iterates through length of sequence and goes every three positions
            sectList = [] #creates empty list
            frame = "-1" #sets frame to string -1
            if ((self.revSeq[i:i+3] == "ATG") 
                or (self.revSeq[i:i+3] == "TTG") 
                or (self.revSeq[i:i+3] == "GTG")) : #Looks for start codon
                startVal = 1 #sets startVal to one to show that start codon is present
                j = i #j or the positon where end codon could be is set to the position of i to make sure it doesn't iterated over code again
                pos2 = 0 #end position is set to 0
                for j in range (j, len(self.revSeq), 3): #iterates through sequence to find end codon
                    if ((self.revSeq[j:j+3] == "TAA") 
                        or (self.revSeq[j:j+3] == "TAG") 
                        or (self.revSeq[j:j+3] == "TGA")) : #Looks for end codon
                        pos2 = (len(self.seq))-(i) #sets end position to the length - start codon position
                        pos1 = (len(self.seq))-(j+3) #sets start position to the length - end codon position
                if pos2 == 0 : #Start and no end
                    pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
                    pos1 = (len(self.seq))-(j+3)
                orfLength = pos2 - pos1 #orf length is determined through end and start position
                sectList.append(frame) #frame is added to list
                sectList.append(str(pos1+1) + "..") #position one is added to list 
                sectList.append(pos2) #position 2 is added to list
                sectList.append(orfLength) #length of ORF is added to list
                finalList.append(sectList) #this list is added to finalList
        if startVal == 0:
            sectList = [] #creates empty list
            pos1 = 0 #start position is set to 0
            k = 0 #k value, which is end codon iteration is set to 0
            pos2 = 0 #end position is set to 0
            for k in range (k, len(self.revSeq), 3): #iterates through sequence to find end codon
                if ((self.revSeq[k:k+3] == "TAA")
                    or (self.revSeq[k:k+3] == "TAG")
                    or (self.revSeq[k:k+3] == "TGA")) : #Looks for end codon
                    pos2 = (len(self.revSeq)) #end postiton is set to the length of the sequence to account for downstream end codons
                    pos1 = (len(self.revSeq))-(k+3) #sets start position to the length - end codon position
            if pos2 == 0 : #No start and no end
                pos2 = len(self.revSeq) #end postiton is set to the length of the sequence to account for downstream end codons
            orfLength = pos2 - pos1 #orf length is determined through end and start position
            sectList.append(frame) #frame is added to list
            sectList.append(str(pos1+1) + "..") #position one is added to list 
            sectList.append(pos2) #position 2 is added to list
            sectList.append(orfLength) #length of ORF is added to list
            finalList.append(sectList) #this list is added to finalList
        return (finalList) #finalList is returned
    
    def frameMTwo (self):
        finalList = [] #creates empty list
        j = 0 #sets j to 0
        i = 0 #sets i to 0
        startVal = 0 #sets startVal to 0
        for i in range(1,len(self.revSeq),3): #for loop iterates through length of sequence and goes every three positions
            sectList = [] #creates empty list
            frame = "-2" #sets frame to string -2
            if ((self.revSeq[i:i+3] == "ATG") 
                or (self.revSeq[i:i+3] == "TTG") 
                or (self.revSeq[i:i+3] == "GTG")) : #Looks for start codon
                startVal = 1 #sets startVal to one to show that start codon is present
                j = i #j or the positon where end codon could be is set to the position of i to make sure it doesn't iterated over code again
                pos2 = 0 #end position is set to 0
                for j in range (j, len(self.revSeq), 3): #iterates through sequence to find end codon
                    if ((self.revSeq[j:j+3] == "TAA") 
                        or (self.revSeq[j:j+3] == "TAG") 
                        or (self.revSeq[j:j+3] == "TGA")) : #Looks for end codon
                        pos2 = (len(self.seq))-(i) #sets end position to the length - start codon position
                        pos1 = (len(self.seq))-(j+3) #sets start position to the length - end codon position
                if pos2 == 0 : #Start and no end
                    pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
                    pos1 = (len(self.seq))-(k+3)
                orfLength = pos2 - pos1 #orf length is determined through end and start position
                sectList.append(frame) #frame is added to list
                sectList.append(str(pos1+1) + "..") #position one is added to list 
                sectList.append(pos2) #position 2 is added to list
                sectList.append(orfLength) #length of ORF is added to list
                finalList.append(sectList) #this list is added to finalList
        if startVal == 0:
            sectList = [] #creates empty list
            pos1 = 0 #start position is set to 0
            k = 1 #k value, which is end codon iteration is set to 1
            pos2 = 0 #end position is set to 0
            for k in range (k, len(self.revSeq), 3): #iterates through sequence to find end codon
                if ((self.revSeq[k:k+3] == "TAA")
                    or (self.revSeq[k:k+3] == "TAG")
                    or (self.revSeq[k:k+3] == "TGA")) : #Looks for end codon
                    pos2 = len(self.revSeq) #end postiton is set to the length of the sequence to account for downstream end codons
                    pos1 = (len(self.revSeq))-(k+3) #sets start position to the length - end codon position
            if pos2 == 0 : #No start and no end
                pos2 = len(self.revSeq) #sets end position to the length of the sequence 
            orfLength = pos2 - pos1 #orf length is determined through end and start position
            sectList.append(frame) #frame is added to list
            sectList.append(str(pos1+1) + "..") #position one is added to list 
            sectList.append(pos2) #position 2 is added to list
            sectList.append(orfLength) #length of ORF is added to list
            finalList.append(sectList) #this list is added to finalList
        return (finalList) #finalList is returned
    
    def frameMThree (self):
        finalList = [] #creates empty list
        j = 0 #sets j to 0
        i = 0 #sets i to 0
        startVal = 0 #sets startVal to 0
        for i in range(2,len(self.revSeq),3): #for loop iterates through length of sequence and goes every three positions
            sectList = [] #creates empty list
            frame = "-3" #sets frame to string -3
            if ((self.revSeq[i:i+3] == "ATG") 
                or (self.revSeq[i:i+3] == "TTG") 
                or (self.revSeq[i:i+3] == "GTG")) : #Looks for start codon
                startVal = 1 #sets startVal to one to show that start codon is present
                j = i #j or the positon where end codon could be is set to the position of i to make sure it doesn't iterated over code again
                pos2 = 0 #end position is set to 0
                for j in range (j, len(self.revSeq), 3):  #iterates through sequence to find end codon
                    if ((self.revSeq[j:j+3] == "TAA") 
                        or (self.revSeq[j:j+3] == "TAG") 
                        or (self.revSeq[j:j+3] == "TGA")) : #Looks for end codon
                        pos2 = (len(self.seq))-(i) #sets end position to the length - start codon position
                        pos1 = (len(self.seq))-(j+3) #sets start position to the length - end codon position
                if pos2 == 0 : #Start and no end
                    pos2 = len(self.seq) #end postiton is set to the length of the sequence to account for downstream end codons
                    pos1 = (len(self.seq))-(j+3) #sets start position to the length - end codon position
                orfLength = pos2 - pos1 #orf length is detemrined through end and start position
                sectList.append(frame) #frame is added to list
                sectList.append(str(pos1+1) + "..") #position one is added to list 
                sectList.append(pos2) #position 2 is added to list
                sectList.append(orfLength) #length of ORF is added to list
                finalList.append(sectList) #this list is added to finalList
        if startVal == 0:
            sectList = [] #creates empty list
            pos1 = 0 #start position is set to 0
            k = 2 #k value, which is end codon iteration is set to 2
            pos2 = 0 #end position is set to 0
            for k in range (k, len(self.revSeq), 3): #iterates through sequence to find end codon
                if ((self.revSeq[k:k+3] == "TAA") 
                    or (self.revSeq[k:k+3] == "TAG")
                    or (self.revSeq[k:k+3] == "TGA")) : #Looks for end codon
                    pos2 = (len(self.revSeq)) #sets end position to the length of the sequence 
                    pos1 = (len(self.revSeq))-(k+3) #sets start position to the length - end codon position
                    orfLength = pos2 - pos1 #orf length is detemrined through end and start position
            if pos2 == 0 : #No start and no end
                pos2 = len(self.revSeq) #end postiton is set to the length of the sequence to account for downstream end codons
            orfLength = pos2 - pos1 #orf length is detemrined through end and start position
            sectList.append(frame) #frame is added to list
            sectList.append(str(pos1+1) + "..") #position one is added to list 
            sectList.append(pos2) #position 2 is added to list
            sectList.append(orfLength) #length of ORF is added to list
            finalList.append(sectList) #this list is added to finalList
        return (finalList) #finalList is returned
    
class NucParams:
    rnaCodonTable = {
    # U
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
    # C
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
    # A
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
    # G
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
    }
    dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}
    def __init__ (self, inString=''): 
        """This method creates an empty string and saves it as inString"""
        self.inString = inString #saves inString
        
    def addSequence (self, inSeq):
        """This adds the sequence determined by the fastareader with the inString and saves it"""
        self.inString = self.inString + inSeq #adds sequence calculated by fastareader to inString
        return self.inString
    
    def aaComposition(self):  
        """This takes the inString updated by the addSequence and divides it into codons and saves it into a list"""
        """This codon list it sent through the dictionary and the corresponding amino acids are placed into a string"""
        """A for loop goes through this string and keeps count of each amino acida dn returns this dictionary"""
        totalSeq = self.inString #saves inString string
        codonList = [] #creates empty list
        n=3
        codonList = [totalSeq[i:i+n] for i in range(0, len(totalSeq), n)] #breaks the string at every 3rd character
        aaList = [] #creates empty list
        for i in codonList: #for every codon 
            aa = NucParams.dnaCodonTable.get(i) #you search for the aa for each codon
            aaList.append(aa) #adds each aa to a list        
        aaString = "" #creates empty string
        aaString = aaString.join(aaList) #makes the aaList into a string and joins with the empty string we created
        aaComp = {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'L':0, 'K':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'Y':0, 'W':0} #creates a dictionary where all the aa are set to 0
        charDict = {} #creates empty dictionary
        for i in aaString: #this for loop looks at each aa in the string
            if i in charDict: #looks if the aa is already within the dictionary
                charDict[i] += 1 #adds one to the count if the aa already exists
            else: #if aa isn't present in the dictionary
                charDict[i] = 1 #it is assigned the value of one
        aaComp.update(charDict) #updates the dictionary where values are 0 with the values we calculated in the for loop
        return aaComp #returns the number of each aa within the user input
        
    def nucComposition(self): 
        """This takes the inString provided by the addSequence and created a for loop to have a dictionary count of each nucleotide within the string"""
        codonString = "" #creates empty string
        #codonString = codonString.join(self.codonList)
        codonString = (self.inString)
        nucComp = {'A':0, 'T':0, 'U':0, 'C':0, 'G':0, 'N':0} #creates a dictionary where all the nucleotides are set to 0
        nucDict = {} #creates empty dictionary
        for i in codonString : #this for loop looks at each nucleotide in the string
            if i in nucDict: #looks if the nucleotide is already within the dictionary
                nucDict[i] += 1 #adds one to the count if the nucleotide already exists
            else: #if nucleotide isn't present in the dictionary
                nucDict[i] = 1 #it is assigned the value of one
        nucComp.update(nucDict) #updates the dictionary where values are 0 with the values we calculated in the for loop
        #totalSum = sum(nucComp.values())
        return nucComp
    
    def codonComposition(self): 
        """This method takes the inString and replaces the T's with U's and the breaks the sequence into codons"""
        """This codon lis tis refined by removing the codons containing N"""
        """I created a dictionary with the keys within the rna codon table with the values =0 and then ran the updated codon list through a for loop to keep a dictionary with the count of each rna codon, which is then returned"""
        codonString = self.inString #joined the empty string with the list created in self and transformed that into a list
        rnaCodonString = codonString.replace('T', 'U') #converts all the T's within the string to U's
        rnaCodonList = [] #creates empty list
        n = 3 #made variable into three to later split every 3rd index
        rnaList = [rnaCodonString[i:i+n] for i in range(0, len(rnaCodonString), n)] #splits the string every 3rd value and places as strings into list of codons made of rna nucleotides
        rnaCodonList = [i for i in rnaList if not 'N' in i] #removes codons that contain N and stores into another list - https://stackoverflow.com/questions/3416401/removing-elements-from-a-list-containing-specific-characters   
        rnaDict = {} #creates empty dictionary
        keyList = [] #creates empty list
        for i in NucParams.rnaCodonTable.keys(): #saves the keys from the provided dictionary into a list - https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
            keyList.append(i) #adds the key values into the empty list called keyList
        rnaDict = {i:0 for i in keyList} #makes a dictionary where keys are the strings within keyList and the values are all 0 - https://stackoverflow.com/questions/3869487/how-do-i-create-a-dictionary-with-keys-from-a-list-and-values-defaulting-to-say
        rnaFreqDict = {} #creates empty dictionary
        for i in rnaCodonList: #this for loop looks at each codon from the user input
            if (i in rnaFreqDict): #looks if the codon is already within the dictionary
                rnaFreqDict[i] += 1 #adds one to the count if the codon already exists
            else: #if codon isn't present in the dictionary
                rnaFreqDict[i] = 1 #it is assigned the value of one
        rnaDict.update(rnaFreqDict) #updates the dictionary where values are 0 with the values we calculated in the for loop
        return rnaDict 
    
    def nucCount(self):
        """Took the inString and counte dthe number of nucleotides that make up the sequence"""
        """This value is then calculated and returned to determine Mb"""
        totalSeq = self.inString #saves the inStirng value as another string
        nucCount = float(len(totalSeq)) #determines length of sequence
        #return nucCount
        #nucCount = float (nucCount/1000000) #divdes by 1000000 to get Mb
        #nucCount = str(round(nucCount, 2)) #rounds to 2 floating integers
        return nucCount
        

class FastAreader :
    ''' 
    Define objects to read FastA files.
    
    instantiation: 
    thisReader = FastAreader ('testTiny.fa')
    usage:
    for head, seq in thisReader.readFasta():
        print (head,seq)
    '''
    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        ''' Handle file opens, allowing STDIN.'''
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)
        
    def readFasta (self):
        ''' Read an entire FastA record and return the sequence header/sequence'''
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
            
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
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

        
class ProteinParam :
    aa2mw = {
        'A': 89.093,  'G': 75.067,  'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225,  'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
        }

    mwH2O = 18.015
    aa2abs280= {'Y':1490, 'W': 5500, 'C': 125}

    aa2chargePos = {'K': 10.5, 'R':12.4, 'H':6}
    aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
    aaNterm = 9.69
    aaCterm = 2.34

    def __init__ (self, protein):
        """The input is the protein sequence given by the user, and the output is the initialized protein which is covereted to uppercase to allow the class to take in both upper and lowercase letters"""
        protein = protein.upper() #makes the protein sequence uppercase
        self.protein = protein

    def aaCount (self):
        """This uses the initial protein input and counts the number of amino acids within the protein"""
        charCount = 0 #makes the initial count of amino acids 0
        for char in self.protein: #for every char within the sequence, the count increases by 1
            charCount += 1 
        return charCount #returns to the main method
        
    def aaComposition (self) :
        """This method has an input of the protein sequence which is provided by the user, and the output is a dictionary containing the number of each amino acid"""
        mainDict = {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'L':0, 'K':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'Y':0, 'W':0} #makes a dictionary of amino acids where all have 0 of each
        charDict = {} #creates a empty dictionary 
        for i in self.protein: #https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
            if i in charDict: #looks if a amino acid is within the chardict, and if so it adds it to the count of that amino acid
                charDict[i] += 1
            else:
                charDict[i] = 1 #otherwise it leaves the count as one
        mainDict.update(charDict) #updates the main dictionary with the char dictionary
        return mainDict #returns this to the main method
    
    def molecularWeight (self):
        """The method uses the dictionary containing amino acid count along with the corresponding molecular weight to calculate the molecular weight of the initially inputted protein sequence"""
        finalMW = 0 #initializes the final molecular weight
        charDict = self.aaComposition() #stores the dictionary created in the aaComposition in another dictioary within this method
        for key in charDict: #for any amino acid within the dictionary the molecular weight is calculated and added to the final molecular weight
            mw = ProteinParam.aa2mw.get(key) #the molecular weight for each amino acid in the dictionary is found 
            subMW = mw - ProteinParam.mwH2O #the molecular weight of the water is the subtracted from the molecular weight of the amino acid
            multMW = charDict[key]*subMW #the resulting value is then multiplied with the number of the amino aicd
            finalMW += multMW #this is then added to the sum of the molecular weights
        finalMW = finalMW + ProteinParam.mwH2O #the total sum of molecular weights is added to the molecular weight of water
        return finalMW #this is returned to the main method

    def molarExtinction (self):
        """This method utilizes the dictionary of amino acids along with the number of each amino acid and the extinction coefficients of each amino acid to determine the molar extinction value"""
        mainDict = self.aaComposition() #copies the aacomposition dictionary into a dictionary within this method
        yTotal = (ProteinParam.aa2abs280['Y'])*(mainDict['Y']) #for each amino acid, the number of each amino acid is multiplied with the extinction coefficient of each amino acid (YWC)
        wTotal = (ProteinParam.aa2abs280['W'])*(mainDict['W'])
        cTotal = (ProteinParam.aa2abs280['C'])*(mainDict['C'])
        nTotal = yTotal + wTotal + cTotal #the values are added to determine the molar extinction
        return nTotal #this is returned to the main method

    def massExtinction (self):
        """massExtinction uses the molarExtincation method and its values along with the molecular weight to determine the massExtinction value"""
        myMW =  self.molecularWeight() #copies the molecular weight into a variable within this method
        return self.molarExtinction() / myMW if myMW else 0.00 #returns the mass extinction by dividing the molar extinction with the molar weight

    def _charge_ (self,ph):
        """This method uses the dictionary that contains the number of amino acids, the dictionary that contains the pKa value and the pH value given by the pI method to produce the netcharge"""
        """The netcharge is then sent back to the pI method"""
        mainDict = self.aaComposition() #copies the aacomposition dictionary into a dictionary within this method
        kTotal = mainDict['K'] * ((10**ProteinParam.aa2chargePos['K'])/((10**ProteinParam.aa2chargePos['K'])+10**(ph))) #the pH value comes pI method
        rTotal = mainDict['R'] * ((10**ProteinParam.aa2chargePos['R'])/((10**ProteinParam.aa2chargePos['R'])+10**(ph)))
        hTotal = mainDict['H'] * ((10**ProteinParam.aa2chargePos['H'])/((10**ProteinParam.aa2chargePos['H'])+10**(ph)))
        nthTotal = ((10**ProteinParam.aaNterm)/((10**ProteinParam.aaNterm)+10**(ph)))
        firstTotal = kTotal + rTotal + hTotal + nthTotal #sums up the positive charges
        
        dTotal = mainDict['D'] * ((10**(ph))/((10**ProteinParam.aa2chargeNeg['D'])+10**(ph)))
        eTotal = mainDict['E'] * ((10**(ph))/((10**ProteinParam.aa2chargeNeg['E'])+10**(ph)))
        cTotal = mainDict['C'] * ((10**(ph))/((10**ProteinParam.aa2chargeNeg['C'])+10**(ph)))
        yTotal = mainDict['Y'] * ((10**(ph))/((10**ProteinParam.aa2chargeNeg['Y'])+10**(ph)))
        cthTotal = ((10**ph)/((10**ProteinParam.aaCterm)+10**(ph)))
        lastTotal = dTotal + eTotal + cTotal + yTotal + cthTotal #sums up the negative charges 
                                             
        netCharge = firstTotal - lastTotal
        return netCharge #returns the netcharge to the pI method 
    
    
    def pI (self):
        """This punction has an input of amino acid codes and outputs the best pH to produce the most neutral net charge"""
        """This method gives the _charge_ function pH values and keeps track the pH that produces the net charge closest to 0"""
        bestCharge = 1000000 #I assigned the bestCharge as a random, but high value 
        bestpH = 0 #set a bestpH to a random number
        for x in range (0,1400+1): #runs through a set of numbers from 1-1400
            x = x/100 #this value is then divided by 100 so that the values sent to _charge_ method is to the hundredths place
            charge = self._charge_(x) #send the pH value to the _charge_ method, and amkes charge equal to it 
            charge = abs(charge) #ensures the charge is positive 
            if charge < bestCharge: #if the charge is less than than the bestCharge, or closer to 0 which is optimal than the bestCharge value becomes equal to the charge
                bestCharge = charge
                bestpH = x #the x value, or pH that produces the most neutrual net charge is saved as the bestpH
        return bestpH #returns the bestpH to the main method
