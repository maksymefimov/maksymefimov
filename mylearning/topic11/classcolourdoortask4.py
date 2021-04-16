


class ColourDoor:
    colour = 'white'
    def __init__(self,number,status = 'closed'):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'Opened'
    def close(self):
        self.status = 'Closed'
    def paint(self,colour):
        self.colour = colour
    @classmethod
    def paint(cls,colour):
        cls.colour = colour
       
       
        
        
    
        
    
