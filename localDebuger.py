import os, sys

class Debuger():
    def __init__(self, header):
        self.__header__ = header
    def __LogTime__(self):
        return ""
    def __GetHeader__(self, _type):
        return "[" + str(self.header) + "]#[" + str(_type) + "]#[{" + str(self.__LogTime__()) + "}]> "
    def __GetSpaceHeader__(self, _type):
        return " " * len(self.Log__GetHeader__(_type))
    def __LogMsg__(self, msg, _type="LOG"):
        print(self.__GetHeader__(_type) + msg)
    def Log(msg*):
        pass #LOG
    def LogError(msg*):
        pass #ERR
    def LogWarning(msg*):
        pass #WAR
