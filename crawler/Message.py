import sys
import os

class Message:
    def __init__(self, text, uid, time, tag):
        self.text = text
        self.uid = uid
        self.time = time
        self.tag = tag

    def show(self):
        print "Tag: ", self.tag
        print "Message: ", self.text
        print "UserId: ", self.uid
        print "TimeStamp: ", self.time

    def getUID(self):
        return self.uid

    def getStr(self):
        return unicode(self.text) + "\n" + unicode(self.uid) + "\n" + unicode(self.time) + "\n"

