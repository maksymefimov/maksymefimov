class Door:
    def __init__(self,number,status,lock):
        self.number = number
        self.status = status
        self.lock = lock
    def open(self):
        if self.lock == 'unlocked':
            self.status = 'Opened'
    def close(self):
        self.status = 'Closed'
    def onlock(self):
        self.lock = 'Locked'
    def unlock(self):
        self.lock = 'unlocked'
    @classmethod
    def knock(cls):
        print('knock')
    
        
        
    
        
    
