class ToggleDoor:
    def __init__(self,number,status):
        self.number = number
        self.status = status
    def toggle(self):
        tog_dict = {'closed':'opened','opened':'closed'}
        self.status = tog_dict[self.status]
    
        
    
        
    
