class Door:


    colour = 'white'

    def __init__(self, number, status,lock):
        self.number = number
        self.status = status
        self.lock = lock
    def close(self):
        self.status = "closed"
          


class SecurityDoor(Door):


    def close_and_lock(self):
        self.status = 'closed'
        self.lock = True
        
    def close(self,lock = False):
        self.status = "closed"
        self.lock = False
    
