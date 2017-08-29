import sys
import os

class Message:
    def __init__(self, text, uid, time):
        self.text = text
        self.uid = uid
        self.time = time

    def show(self):
        print "Message: ", self.text
        print "UserId: ", self.uid
        print "TimeStamp: ", self.time

    def get_UserId(self):
        return self.uid

    def getStr(self):
        return unicode(self.text) + "\n" + unicode(self.uid) + "\n" + unicode(self.time) + "\n"

