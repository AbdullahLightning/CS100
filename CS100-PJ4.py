import math
#group 6 ABDULLAH YILDIRIM AND PRAKASH JAVADALA
class Point:
   '''Represent a 2d point'''
   def __init__(self,customerX, customerY):
       self.x = customerX
       self.y = customerY
       

   def getCoordinates(self):
       ''' return the coordinates of this point as a tuple'''
       return(self.x, self.y)


    #add method changeCoordinates() that
    #changes coordinates of a point to a new
    #set of coordinates

   def changeCoordinates(self, newX, newY):
        ''' changes the coordinates of this point to
           the new values'''
        self.x = newX
        self.y = newY

     #add a method distanceTo() that returns
    #the distance between two Point objects

   def distanceTo(self, second):
        ''' calculate distance between two points'''
        d=math.sqrt((self.x - second.x)**2 + (self.y - second.y)**2)
        return d
        
