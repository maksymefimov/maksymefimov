class Door:


    colour = 'white'

    def __init__(self, number, status,lock):
        self.number = number
        self.status = status
        self.lock = lock


class SecurityDoor(Door):


    def close_and_lock(self):
        self.status = 'closed'
        self.lock = True
        

    
