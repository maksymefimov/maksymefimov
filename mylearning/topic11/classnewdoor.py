class Door:
    status = 'undefined ' 
    def __init__(self,number,status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'Opened'
    def close(self):
        self.status = 'Closed'
   
        
    
        
        
    
        
    
