#!/usr/bin/env python3 
# Name: Shweta Jones(shsujone)
# Group Members: none

import math
class Triad:
    def __init__(self,p,q,r) :
        """ Initializes the values of p,q,r and also the pqMid, prMid, and qrMid to be utilized in other methods"""
        self.p = p #saves the p from the main as a self
        self.q = q #saves the q from the main as a self
        self.r = r #saves the r from the main as a self
        
        a = (p[0]-q[0])**2 #these calculations subtract the p and q values and add them together and save them to use in other methods
        b = (p[1]-q[1])**2
        c = (p[2]-q[2])**2
        pqMid = a+b+c
        self.pqMid = pqMid #saves to be used in following methods
        
        a = (p[0]-r[0])**2 #these calculations subtract the p and r values and add them together and save them to use in other methods
        b = (p[1]-r[1])**2
        c = (p[2]-r[2])**2
        prMid = a+b+c
        self.prMid = prMid #saves to be used in following methods
        
        a = (q[0]-r[0])**2 #these calculations subtract the q and r values and add them together and save them to use in other methods
        b = (q[1]-r[1])**2
        c = (q[2]-r[2])**2
        qrMid = a+b+c
        self.qrMid = qrMid #saves to be used in following methods
        
    def dPQ (self):
        """ Provides the distance between point p and point q """
        pq = (math.sqrt(self.pqMid)) #calculates the pq distance using values from the init
        return pq #returns to main
        
    def dPR (self):
        """ Provides the distance between point p and point r """
        pr = (math.sqrt(self.prMid)) #calculates the pr distance using values from the init
        return pr #returns to main
    
    def dQR (self):
        """ Provides the distance between point q and point r """
        qr = (math.sqrt(self.qrMid)) #calculates the qr distance using values from the init
        return qr #returns to main
    
    def angleP (self) :
        """ Provides the angle made at point p by segments pq and pr (radians). """
        a = (self.q[0]-self.p[0])*(self.r[0]-self.p[0]) #The following three operations help calculate the numerator 
        b = (self.q[1]-self.p[1])*(self.r[1]-self.p[1])
        c = (self.q[2]-self.p[2])*(self.r[2]-self.p[2])
        num = a+b+c #summarizes all the values in the numerator of the equation
        pr = (math.sqrt(self.prMid)) #calculates pr length
        pq = (math.sqrt(self.pqMid)) #calculates pq method
        qpr = math.acos(num/(pr*pq)) #calculates the angle P in radians
        return qpr #returns to main
    
    def angleQ (self) :
        """ Provides the angle made at point q by segments qp and qr (radians). """
        a = (self.p[0]-self.q[0])*(self.r[0]-self.q[0]) #The following three operations help calculate the numerator 
        b = (self.p[1]-self.q[1])*(self.r[1]-self.q[1])
        c = (self.p[2]-self.q[2])*(self.r[2]-self.q[2])
        num = a+b+c #summarizes all the values in the numerator of the equation
        qr = (math.sqrt(self.qrMid)) #calculates qr length
        pq = (math.sqrt(self.pqMid)) #calculates pq method
        pqr = math.acos(num/(qr*pq)) #calculates the angle Q in radians
        return pqr #returns to main
           
    def angleR (self) :
        """ Provides the angle made at point r by segments rp and rq (radians). """
        a = (self.p[0]-self.r[0])*(self.q[0]-self.r[0]) #The following three operations help calculate the numerator 
        b = (self.p[1]-self.r[1])*(self.q[1]-self.r[1])
        c = (self.p[2]-self.r[2])*(self.q[2]-self.r[2])
        num = a+b+c #summarizes all the values in the numerator of the equation
        qr = (math.sqrt(self.qrMid)) #calculates qr length
        pr = (math.sqrt(self.prMid)) #calculates pr method
        prq = math.acos(num/(qr*pr)) #calculates the angle R in radians
        return prq #returns to main

def main():
    """The main emthods splits the user input into seperate lists and the runs the bond length and angle methods to print out the expected values"""
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
    pr = initial.dPR() #the length of pr is calculated by running the dPR method
    qr = initial.dQR() #the length of qr is calculated by running the dQR method   
    
    pqr = initial.angleQ() #the bond angle of pqr is calculated by running the angleQ method
    pqr = (pqr * 180)/math.pi #takes the calculated Q bond angle and converts the value to degrees
    
    qpr = initial.angleP() #the bond angle of qpr is calculated by running the angleP method
    qpr = (qpr * 180)/math.pi #takes the calculated P bond angle and converts the value to degrees
    
    prq = initial.angleR() #the bond angle of prq is calculated by running the angleR method
    prq = (prq * 180)/math.pi #takes the calculated R bond angle and converts the value to degrees
    
    print ("N-C bond length = " + ("%0.2f" % pq)) #the pq length is printed with the correct print statement and rounded to the correct value
    print ("N-Ca bond length = " + ("%0.2f" % qr)) #the qr length is printed with the correct print statement and rounded to the correct value
    print ("C-N-Ca bond angle = " + ("%0.1f" % pqr)) #the pqr angle is printed with the correct print statement and rounded to the correct value
    
main()