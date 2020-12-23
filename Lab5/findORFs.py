#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
# Name: Shweta Jones(shsujone)
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)
"""
PseudoCode for OrfFinder:
Init
    Saves the sequence as self
    Saves reverse complementary as self
Plus One Frame Method:
    For loop allows to iterate through sequence, goes every 3rd nucleotide from 0 till end of sequence
        If loop finds a start codon
            Sets position one to the i (which is start codon)
            For loop allows to iterate through sequence, goes every thrid nucleotide AFTER start codon
                If loop finds an end codon
                    Sets position of end to the j (which is end codon)
            If loop in the siutiation that there is a start codon but not end
                Sets position of the end to the length of the sequence to account for downstream codons
            Orf length is then calculated with start and end positions 
            List is created with frame, start position, end position, and orf length
    If loop in the situation that there is not start codon
        Position one is then 0 to account for possible upstream codons
        For loop iterates through sequence to end 
            If loop finds an end codon
                Sets end position to the position of the end codon
        If loop in the situaiton there is no end codon
            Position two is set to 0 to account for end codons downstream
        Now that you have both end and start position, orf length is calculated 
        List is created with frame, start position, end position, and orf length
    Final list is returned to main with all lists related to the plus one coding frame 
Plus Two Frame Method:
    For loop allows to iterate through sequence, goes every 3rd nucleotide from 1 till end of sequence
        If loop finds a start codon
            Sets position one to the i (which is start codon)
            For loop allows to iterate through sequence, goes every third nucleotide AFTER start codon
                If loop finds an end codon
                    Sets position of end to the j (which is end codon)
            If loop in the siutiation that there is a start codon but not end
                Sets position of the end to the length of the sequence to account for downstream codons
            Orf length is then calculated with start and end positions 
            List is created with frame, start position, end position, and orf length
    If loop in the situation that there is not start codon
        Position one is then 0 to account for possible upstream codons
        For loop iterates through sequence from 1 to end 
            If loop finds an end codon
                Sets end position to the position of the end codon
        If loop in the situaiton there is no end codon
            Position two is set to 0 to account for end codons downstream
        Now that you have both end and start position, orf length is calculated 
        List is created with frame, start position, end position, and orf length
    Final list is returned to main with all lists related to the plus two coding frame 
Plus Three Frame Method:
    For loop allows to iterate through sequence, goes every 3rd nucleotide from 2 till end of sequence
        If loop finds a start codon
            Sets position one to the i (which is start codon)
            For loop allows to iterate through sequence, goes every thrid nucleotide AFTER start codon
                If loop finds an end codon
                    Sets position of end to the j (which is end codon)
            If loop in the siutiation that there is a start codon but not end
                Sets position of the end to the length of the sequence to account for downstream codons
            Orf length is then calculated with start and end positions 
            List is created with frame, start position, end position, and orf length
    If loop in the situation that there is not start codon
        Position one is then 0 to account for possible upstream codons
        For loop iterates through sequence from 2 till end 
            If loop finds an end codon
                Sets end position to the position of the end codon
        If loop in the situaiton there is no end codon
            Position two is set to 0 to account for end codons downstream
        Now that you have both end and start position, orf length is calculated 
        List is created with frame, start position, end position, and orf length
    Final list is returned to main with all lists related to the plus three coding frame 
Minus One Frame Method:
    For loop allows to iterate through reversed complementary sequence, goes every 3rd nucleotide from 0 till end of sequence
        If loop finds a start codon
            For loop allows to iterate through reversed complementary sequence, goes every thrid nucleotide AFTER start codon
                If loop finds an end codon
                    Sets position of end to the length of sequence - the position of the start
                    Sets position one to the length of sequence - position of end 
            If loop in the siutiation that there is a start codon but not end
                Sets position of the end to the length of the sequence to account for downstream codons
                Sets position one to the length of sequence - position of end
            Orf length is then calculated with start and end positions 
            List is created with frame, start position, end position, and orf length
    If loop in the situation that there is not start codon
        Position one is then 0 to account for possible upstream codons
        For loop iterates through reversed complementary sequence 
            If loop finds an end codon
                Sets end position to the length of sequence 
                Sets positions one to the length - position of the end 
        If loop in the situaiton there is no end codon
            Position two is set to sequence length to account for end codons downstream
        Now that you have both end and start position, orf length is calculated 
        List is created with frame, start position, end position, and orf length
    Final list is returned to main with all lists related to the minus one coding frame 
Minus Two Frame Method:
    For loop allows to iterate through reversed complementary sequence, goes every 3rd nucleotide from 1 till end of sequence
        If loop finds a start codon
            For loop allows to iterate through reversed complementary sequence, goes every thrid nucleotide AFTER start codon
                If loop finds an end codon
                    Sets position of end to the length of sequence - the position of the start
                    Sets position one to the length of sequence - position of end 
            If loop in the siutiation that there is a start codon but not end
                Sets position of the end to the length of the sequence to account for downstream codons
                Sets position one to the length of sequence - position of end
            Orf length is then calculated with start and end positions 
            List is created with frame, start position, end position, and orf length
    If loop in the situation that there is not start codon
        Position one is then 0 to account for possible upstream codons
        For loop iterates through reversed complementary sequence 
            If loop finds an end codon
                Sets end position to the length of sequence 
                Sets positions one to the length - position of the end 
        If loop in the situaiton there is no end codon
            Position two is set to sequence length to account for end codons downstream
        Now that you have both end and start position, orf length is calculated 
        List is created with frame, start position, end position, and orf length
    Final list is returned to main with all lists related to the minus two coding frame 
Minus Three Frame Method:
    For loop allows to iterate through reversed complementary sequence, goes every 3rd nucleotide from 2 till end of sequence
        If loop finds a start codon
            For loop allows to iterate through reversed complementary sequence, goes every thrid nucleotide AFTER start codon
                If loop finds an end codon
                    Sets position of end to the length of sequence - the position of the start
                    Sets position one to the length of sequence - position of end 
            If loop in the siutiation that there is a start codon but not end
                Sets position of the end to the length of the sequence to account for downstream codons
                Sets position one to the length of sequence - position of end
            Orf length is then calculated with start and end positions 
            List is created with frame, start position, end position, and orf length
    If loop in the situation that there is not start codon
        Position one is then 0 to account for possible upstream codons
        For loop iterates through reversed complementary sequence 
            If loop finds an end codon
                Sets end position to the length of sequence 
                Sets positions one to the length - position of the end 
        If loop in the situaiton there is no end codon
            Position two is set to sequence length to account for end codons downstream
        Now that you have both end and start position, orf length is calculated 
        List is created with frame, start position, end position, and orf length
    Final list is returned to main with all lists related to the minus three coding frame     

PseudoCode for findORFS:
Main:
    Takes the file input and runs through FastReader which 
    For takes the sequence and sends to the ORFfinader class and processes the information
        Returned lists will be sort based on orfLength and then left most position of the gene 
        Sorted list is printed 

"""
import sequenceAnalysis
class CommandLine() :
    def __init__(self, inOpts=None) :   
        import argparse
        self.parser = argparse.ArgumentParser(description = 'Program prolog - a brief description of what this thing does', 
                                             epilog = 'Program epilog - some other stuff you feel compelled to say', 
                                             add_help = True, #default is True 
                                             prefix_chars = '-', 
                                             usage = '%(prog)s [options] -option1[default] <input >output'
                                             )
        self.parser.add_argument('-lG', '--longestGene', action = 'store', nargs='?', const=True, default=False, help='longest Gene in an ORF')
        self.parser.add_argument('-mG', '--minGene', type=int, choices= (100,200,300,500,1000), default=100, action = 'store', help='minimum Gene length')
        self.parser.add_argument('-s', '--start', action = 'append', default = ['ATG', 'TTG', 'GTG'],nargs='?', help='start Codon') #allows multiple list options
        self.parser.add_argument('-t', '--stop', action = 'append', default = ['TAG','TGA','TAA'],nargs='?', help='stop Codon') #allows multiple list options
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')  
        if inOpts is None :
            self.args = self.parser.parse_args()
        else :
            self.args = self.parser.parse_args(inOpts)

def main(inCL=None):  
    if inCL is None:
        myCommandLine = CommandLine()
    else :
        myCommandLine = CommandLine(inCL)
        
    myReader = sequenceAnalysis.FastAreader() #runs FastAreader
    for head, seq in myReader.readFasta() : #for loop enables to run for head sequence 
        finalList = [] #empty list is created
        print (head) #allows for title of the file to be printed
        myNuc = sequenceAnalysis.OrfFinder(seq) #sends the sequence through the OrfFinder class, and initilizes values
        test1 = myNuc.frameOne() #runs the plus one reading frame
        for i in test1: #for loop iterates through returned list and places list within finalList
            finalList.append(i)
        test2 = myNuc.frameTwo() #runs the plus two reading frame
        for i in test2: #for loop iterates through returned list and places list within finalList
            finalList.append(i)
        test3 = myNuc.frameThree() #runs the plus three reading frame
        for i in test3: #for loop iterates through returned list and places list within finalList
            finalList.append(i)
        test4 = myNuc.frameMOne() #runs the minus one reading frame
        for i in test4: #for loop iterates through returned list and places list within finalList
            finalList.append(i)
        test5 = myNuc.frameMTwo() #runs the minus two reading frame
        for i in test5: #for loop iterates through returned list and places list within finalList
            finalList.append(i)
        test6 = myNuc.frameMThree()  #runs the minus three reading frame
        for i in test6: #for loop iterates through returned list and places list within finalList
            finalList.append(i) 
        sortedList = sorted(finalList, key=lambda x: x[1]) #sorts list based on proximity to left position of the gene
        finaleList = sorted(sortedList, key=lambda x: x[3], reverse = True) #sorts list based on decreasing order of orfLength
        for s in finaleList: #for loop iterates through finalList and prints in strings 
            print(*s) 
    print (myCommandLine.args)

if __name__ == "__main__":
    main()
      

