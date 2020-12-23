#!/usr/bin/env python3 
# Name: Shweta Jones(shsujone)
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)

short_AA = { #converts long AA to short AA
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
            }

long_AA = {value:key for key,value in short_AA.items()} #converts short AA to long AA

RNA_codon_table = { #This converts RNA to AA
# Second Base
# U             C             A             G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C 
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}
dnaCodonTable = {key.replace('U','T'):value for key, value in RNA_codon_table.items()} #This dictionary converts DNA to AA

def main():
    """The main method takes the user's code and finds its corresponding key or values within the given dictionaries, if this answer is not found, unknown is returned"""
    code = input ("Enter your code:")
    
    answerList = []
    answer = short_AA.get(code, "unknown") #looks within the short_AA dictionary else replaces with unknown, converts longer amino acid to short amino acid
    answer = answer.upper() #makes the output uppercase
    answerList.append(answer) #enters the answer into a list
    answer = long_AA.get(code, "unknown") #looks within the long_AA dictionary else replaces with unknown, converts short amino acid to long amino acid
    answer = answer.upper() #makes the output uppercase
    answerList.append(answer) #enters the answer into a list
    answer = RNA_codon_table.get(code, "unknown") #looks within the RNA_codon_table dictionary else replaces with unknown, converts RNA to amino acid
    answerList.append(answer) #enters the answer into a list
    answer = dnaCodonTable.get(code, "unknown") #looks within the DNA _codon_table dictionary else replaces with unknown, converts DNA to amino acid
    answer = answer.upper() #makes the output uppercase
    answerList.append(answer) #enters the answer into a list
    finalList = sorted(answerList) #sorts the list in alphabetical order and thus places the answer before the unknowns, https://kite.com/python/answers/how-to-sort-a-list-alphabetically-in-python
    revisedStr = " " #makes an empty string
    revisedStr = revisedStr.join(finalList) #allows for the list to be made into a string, https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    revisedStr = revisedStr.replace("UNKNOWN", "unknown") #replaces the UNKNOWN with unknown 
    final = revisedStr.split()[0]#prints out the first word in the list, https://kite.com/python/answers/how-to-get-the-first-word-in-a-string-in-python
    print(code + " = " + final) #prints out the code entered and the correpsonding AA, DNA, RNA, or unknown

main()