#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sequenceAnalysis 
sequenceAnalysis.NucParams.rnaCodonTable

def main ():
    """This main uses the code within the sequenceAnalysis module to calculate the values"""
    """One outcome of this method is the sequence length and GC content"""
    """The second outcome of this method is a string that prints out codon, its corresponding aa, codon frequency, and codon count"""
    myReader = sequenceAnalysis.FastAreader() # make sure to change this to use stdin
    myNuc = sequenceAnalysis.NucParams() #saves myNuc as the value returned by NucParams
    for head, seq in myReader.readFasta() : #allows for all the individual sequences to get added together by running it through the FastAReader
        myNuc.addSequence(seq) 
    
    length = myNuc.nucCount() #runs the nucCount method
    length = float (length/1000000) #divdes by 1000000 to get Mb
    length = str(round(length, 2)) #rounds to 2 floating integers
    print ("sequence length = " + length + " Mb") #prints out the line
    print() #leaves an empty line
    
    nucCompDict = {} #creates an empty dict
    nucCompDict = myNuc.nucComposition() #saves the value returned by the nucComposition method into a dictionary
    total = float(sum(nucCompDict.values())) #sums the values from the dictionary as a float
    gNuc = nucCompDict.get("C") #gathers the number of C nucleotides within the sequence 
    cNuc = nucCompDict.get("G") #gathers the number of G nucleotides within the sequence
    gcNuc = float (gNuc + cNuc) #adds the g and c nucleotides and saves as float
    gcContent = (gcNuc/total)*100 #multiplies by 100 to save as percent
    gcContent = str(round(gcContent,1)) #rounds the gc content to 1 decimal place
    print ("GC content = " + gcContent + "%") #prints out the gc content 
    print() #leaves an empty line
    
    codAA = {} #creates an empty dict
    codAA = sequenceAnalysis.NucParams.rnaCodonTable #saves the rnaCodonTable into a dictionary
    aaCod = {} #creates an empty dict
    for key, value in codAA.items(): #flips the key and values so that it is ordered as AA:Codon, and stores into aaCod
        aaCod.setdefault(value, list()).append(key)  
    sortAA = {} #creates an empty dict
    for elem in sorted(aaCod.items()) : #sorts the amino acids in alphabetical order, and stores into sortAA
        sortAA[elem[0]] = elem[1]
    sorted_coddict = {} #creates an empty dict
    sorted_coddict = {i: sorted(j) for i, j in sortAA.items()} #sorts the codons under each aa and stores into sorted_coddict
    codList = list(sorted_coddict.values()) #places the sorted dictionary into a list
    flat_list = [] #creates empty list - https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    for sublist in codList: #currently the codList is a list of lists, so this for loop allows for it to be placed into one list
        for item in sublist:
            flat_list.append(item)
    
    codonCompDict = myNuc.codonComposition() #saves the dictionary returned by the codonComposition method into codonCompDict
    for item in flat_list: #prints the values for every codon from the sorted list of codons
        nuc = item #saves nuc as the codon
        aa = codAA.get(item) #saves aa as the amino acid that corresponds with the codon
        aaDict = myNuc.aaComposition() #saves the dictionary returned by the aaComposition method as aaDict
        aaVal = aaDict.get(aa) #gathers the number amino acids that code for that amino acid
        codonVal = codonCompDict.get(item) #gather the number of codons that code for that amino acid
        val = ((float(codonVal)/float(aaVal))*100) #determine the frequency 
        cod = codonCompDict.get(item) #saves cod as the number of that codon within the sequence
        print ('{:s} : {:s} {:5.1f} ({:6d})'.format(nuc, aa, val, cod)) #prints out the expected values

if __name__ == "__main__":
    main()


# In[2]:


instring = 'atcgdf'
n=3
codonList = [instring[i:i+n] for i in range(0, len(instring), n)]
print (codonList)


# In[3]:


rnaList = ['ATC', 'NAC']
rnaCodonList = [i for i in rnaList if not 'N' in i]
print (rnaCodonList)


# In[ ]:




