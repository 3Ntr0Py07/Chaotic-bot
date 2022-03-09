import os, sys

class Debuger():
    def __init__(self, header):
        self.__header__ = header
    def __LogTime__(self):
        return ""
    def __GetHeader__(self, _type):
        return "[" + str(self.__header__) + "]#[" + str(_type) + "]#[{" + str(self.__LogTime__()) + "}]> "
    def __GetSpaceHeader__(self, _type):
        return " " * len(self.__GetHeader__(_type))
    def __LogMsg__(self, msg, _type="LOG", empty=False):
        if (empty):
            print(self.__GetSpaceHeader__(_type) + msg)
        else:
            print(self.__GetHeader__(_type) + msg)
    def __GetMsg__(self, *msg):
        msgs = []
        for i in msg:
            if (type(msg) == Exception):
                msgs += str(i).split("\n") # Exceptions
            else:
                msgs += str(i).split("\n")
        return msgs
    def Log(self, *msg):
        empty = False
        for i in self.__GetMsg__(*msg):
            self.__LogMsg__(i, _type="LOG", empty=empty)
            empty = True
    def LogError(self, *msg):
        empty = False
        for i in self.__GetMsg__(*msg):
            self.__LogMsg__(i, _type="ERR", empty=empty)
            empty = True
    def LogWarning(self, *msg):
        empty = False
        for i in self.__GetMsg__(*msg):
            self.__LogMsg__(i, _type="WAR", empty=empty)
            empty = True
if (__name__=="__main__"):
    Debug = Debuger("LOG TEST")
    Debug.Log("Hello", "Hello World", "Error")
