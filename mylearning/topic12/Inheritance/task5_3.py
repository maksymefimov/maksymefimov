class Door:


    colour = "white"

    def __init__(self, number, status,lock):
        self.number = number
        self.status = status
        self.lock = lock

    def close(self):
        self.status = "closed"
          


class SecurityDoor(Door):


    def __init__(self, number, status, lock, cam = False):
        self.number = number
        self.status = status
        self.lock = lock
        self.cam = cam
        
    def close_and_lock(self):
        self.status = "closed"
        self.lock = True
        
    def close(self,lock = False):
        self.status = "closed"
        self.lock = False

    def switch_cam_on_off(self,cam):
        if cam:
            self.cam = False
        else:
            self.cam = True
            
    
