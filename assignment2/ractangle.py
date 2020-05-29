class RECTANGLE:
    width = height = corner_x = corner_y = 0
    def __init__(self,w,h,x,y):
        self.width = w
        self.height = h
        self.corner_x = x
        self.corner_y = y
    def findCentre(self):
        return (self.corner_x+self.width/2,self.corner_y+self.height/2)
    def findArea(self):
        return (self.height*self.width)
    def findPerimeter(self):
        return (2*(self.height+self.width))
        
box = RECTANGLE(10,20,2,2)
print("Area=",box.findArea())
print("Perimeter=",box.findPerimeter())
print("Center=",box.findCentre())