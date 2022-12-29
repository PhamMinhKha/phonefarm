import ldhelper
import random
class Xuly:
    def __init__(self):
        self.data = None

    def themLDPlayer(self):
        ld = ldhelper.LdHelper("C:\LDPlayer\LDPlayer9")
        return ld.CreateLD(random.random())

