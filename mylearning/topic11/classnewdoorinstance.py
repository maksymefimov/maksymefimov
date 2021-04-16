class Door:
    status = 'closed' 
    def __init__(self,number):
        self.number = number
    def open(self):
        self.status = 'Opened'
    def close(self):
        self.status = 'Closed'
    def toggle(self):
        tog_dict = {'closed':'opened','opened':'closed'}
        self.status = tog_dict[self.status]
        
        
    
        
    
