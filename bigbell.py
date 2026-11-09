class BigBell:
    def __init__(self):
        self.is_ding = True

    def sound(self):
        if self.is_ding:
            print("ding")
            self.is_ding = False
        else:
            print("dong")
            self.is_ding = True

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
