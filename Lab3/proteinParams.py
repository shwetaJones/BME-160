#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:19:03 2020

@author: shwetajones
"""


#!/usr/bin/env python3
# Name: Shweta Jones(shsujone)
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)

class ProteinParam :
# These tables are for calculating:
#     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
#     absorbance at 280 nm (aa2abs280)
#     pKa of positively charged Amino Acids (aa2chargePos)
#     pKa of negatively charged Amino acids (aa2chargeNeg)
#     and the constants aaNterm and aaCterm for pKa of the respective termini
#  Feel free to move these to appropriate methods as you like

# As written, these are accessed as class attributes, for example:
# ProteinParam.aa2mw['A'] or ProteinParam.mwH2O
    """All of these are different dictionaries which are supposed to be used by the methods within the class"""
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

# Please do not modify any of the following.  This will produce a standard output that can be parsed
    
import sys
def main():
    """The main method has an prompts the user to enter a protein sequence which is then used by the lines following"""
    inString = input('protein sequence?')
    while inString :
        myParamMaker = ProteinParam(inString)
        myAAnumber = myParamMaker.aaCount()
        print ("Number of Amino Acids: {aaNum}".format(aaNum = myAAnumber))
        print ("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
        print ("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
        print ("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
        print ("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
        print ("Amino acid composition:")
        myAAcomposition = myParamMaker.aaComposition()
        keys = list(myAAcomposition.keys())
        keys.sort()
        if myAAnumber == 0 : myAAnumber = 1  # handles the case where no AA are present 
        for key in keys :
            print ("\t{} = {:.2%}".format(key, myAAcomposition[key]/myAAnumber))
            
        inString = input('protein sequence?')

if __name__ == "__main__":
    main()