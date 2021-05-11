class Door:


    def __init__(self, number, status):
        self.number = number
        self.status = status


    def open(self):
        self.status = "open"


    def close(self):
        self.status = "closed"


class SecurityDoor(Door):
    colour = "grey"

    def __init__(self, number, status, locked = False):
        super().__init__(number, status)
        self.locked = locked


    def open(self):
        if not self.locked:
            return
        super().open()

    def close_and_lock(self):
        super().close()
        self.locked = True
