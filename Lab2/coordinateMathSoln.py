#!/usr/bin/env python3 
# Name: Shweta Jones(shsujone)
# Group Members: Pranav Muthuraman (pmuthura), Sahasra Shankar (sshanka8)

"""This programs takes the coordinates from the user to calculates and print out bond lengths and angles"""
import math
class Triad :
    """
    Calculate angles and distances among a triad of points.
        Author: David Bernick
        Date: March 21, 2013
        Points can be supplied in any dimensional space as long as they are consistent.
        Points are supplied as tupels in n-dimensions, and there should be three
        of those to make the triad. Each point is positionally named as p,q,r
        and the corresponding angles are then angleP, angleQ and angleR.
        Distances are given by dPQ(), dPR() and dQR()
    """
 
    def __init__(self,p,q,r) :
        """Constructs a Triad using the coordinates from the user""" 
        self.p = p #saves the p from the main as a self
        self.q = q #saves the q from the main as a self
        self.r = r #saves the r from the main as a self

    def d2 (self,a,b) : 
        """calculate squared distance of point a to b"""
        return float(sum((ia-ib)*(ia-ib)  for  ia,ib in zip (a,b))) #calculates the d2 to be used in other methods
    
    def dot (self,a,b) : 
        """dotProd of standard vectors a,b"""
        return float(sum(ia*ib for ia,ib in zip(a,b))) #calculates the dot product to be used in other methods
    
    def ndot (self,a,b,c) : 
        """dotProd of vec. a,c standardized to b"""
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c))) #calculates the ndot to be used in other methods
    
    def dPQ (self): 
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p,self.q)) #runs the calculation to determine the bond length of PQ
    
    def dPR (self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p,self.r)) #runs the calculation to determine the bond length of PR
    
    def dQR (self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q,self.r)) #runs the calculation to determine the bond length of QR
    
    def angleP (self) :
        """ Provides the angle made at point p by segments pq and pr (radians)"""
        return math.acos(self.ndot(self.q,self.p,self.r)/math.sqrt(self.d2(self.q,self.p)*self.d2(self.r,self.p))) #runs the calculation to determine the bond angle of P
    
    def angleQ (self) :
        """ Provides the angle made at point q by segments qp and qr (radians)"""
        return math.acos(self.ndot(self.p,self.q,self.r)/math.sqrt(self.d2(self.p,self.q)*self.d2(self.r,self.q))) #runs the calculation to determine the bond length of Q
 
    def angleR (self) :
        """ Provides the angle made at point r by segments rp and rq (radians)"""
        return math.acos(self.ndot(self.p,self.r,self.q)/math.sqrt(self.d2(self.p,self.r)*self.d2(self.q,self.r))) #runs the calculation to determine the bond length of R

def main():
    """The main method takes the coordinates given by the user and splits it into triads and send to the Triad class into order to determine bond lengths and angles and prints them out"""
    data = input("What are three sets of coordinates?") #I'm going to assume that the user will input the data in the order that is displayed in the example above
    pBeg = data.find ("(") #find the first instance of the (
    pEnd = data.find (")") #find the first instance of the )
    p = (data [pBeg+1:pEnd]) #makes p equal to the data between ()
    p = p.split(', ') #takes the data and saves all the ints sperated by the commas into p - https://kite.com/python/answers/how-to-split-a-string-into-integers-in-python
    pList = list(map(float, p)) #makes a list of the values within p
    
    qBeg = data.find ("(", pEnd+1) #find the first instance of the (
    qEnd = data.find(")", pEnd +1) #find the first instance of the )
    q = (data [qBeg+1:qEnd]) #makes q equal to the data between ()
    q = q.split(', ') #takes the data and saves all the ints sperated by the commas into q
    qList = list(map(float, q)) #makes a list of the values within q
    
    rBeg = data.find ("(", qEnd+1) #find the first instance of the (
    rEnd = data.find(")", qEnd +1) #find the first instance of the )
    r = (data [rBeg+1:rEnd]) #makes r equal to the data between ()
    r = r.split(', ') #takes the data and saves all the ints sperated by the commas into r
    rList = list(map(float, r)) #makes a list of the values within r
    
    initial = Triad (pList,qList,rList) #sends the lists of p,q,and r and sends it to the Triad class and it goes through the init method
    pq = initial.dPQ() #the length of pq is calculated by running the dPQ method
    qr = initial.dQR() #the length of qr is calculated by running the dPQ method   
    pqr = initial.angleQ() #the bond angle of pqr is calculated by running the angleQ method
    pqr = (pqr * 180)/math.pi #takes the calculated Q bond angle and converts the value to degrees - https://stackoverflow.com/questions/34259237/multiplying-a-number-with-pi-value-in-python
    
    print ("N-C bond length = " + ("%0.2f" % pq)) #the pq length is printed with the correct print statement and rounded to the correct value
    print ("N-Ca bond length = " + ("%0.2f" % qr)) #the qr length is printed with the correct print statement and rounded to the correct value
    print ("C-N-Ca bond angle = " + ("%0.1f" % pqr)) #the pqr angle is printed with the correct print statement and rounded to the correct value
    

main()
