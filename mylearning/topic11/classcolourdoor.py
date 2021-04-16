class ColourDoor:
    colour = 'white'
    def __init__(self,number,status = 'closed'):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'Opened'
    def close(self):
        self.status = 'Closed'
   
        
    
        
    
