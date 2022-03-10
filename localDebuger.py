import os, sys
import time
import colorama

class __Colors__():
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    __ENDC__ = '\033[0m'
    ENDC = '#RESET$COLOR#'
    WHITE = ''
    LOG = ''
    HEADER = '\033[95m'
    TITLE = '\033[51m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'

class Debuger():
    def __init__(self, header):
        self.__header__ = header
        self.Colors = __Colors__
        colorama.init()
    def __SetLength__(self, value, length, fillChar):
        value = str(value)
        while (len(value) < length):
            value = fillChar + value
        return value
    def __LogTime__(self):
        lt = time.localtime()
        lts = self.__SetLength__(lt[3], 2, "0") + ":"
        lts += self.__SetLength__(lt[4], 2, "0") + ":"
        lts += self.__SetLength__(lt[5], 2, "0") + " "
        lts += self.__SetLength__(lt[2], 2, "0") + "."
        lts += self.__SetLength__(lt[1], 2, "0") + "."
        lts += self.__SetLength__(lt[0], 4, "0")
        return lts
    def __GetHeader__(self, _type):
        return "[" + str(self.__header__) + "]#[" + str(_type) + "]#[" + str(self.__LogTime__()) + "]> "
    def __GetSpaceHeader__(self, _type):
        return " " * len(self.__GetHeader__(_type))
    def __LogMsg__(self, msg, _type="LOG", empty=False, color=__Colors__.WHITE):
        if (empty):
            print(self.__GetSpaceHeader__(_type) + color + msg)
        else:
            print(self.__GetHeader__(_type) + color + msg)
    def __ConverColor__(self, msg, msgColor):
        msgColorText = ""
        print(msg)
        for i in msg.split(__Colors__.ENDC):
            print(i)
            msgColorText = i + __Colors__.__ENDC__ + msgColor
        return msgColorText[:-(len(__Colors__.__ENDC__) + len(msgColor))]
    def __GetMsg__(self, *msg, color=__Colors__.WHITE):
        msgs = []
        for i in msg:
            if (type(i) == TypeError):
                msgs += self.__ConverColor__(str(i.with_traceback()), color).split("\n") # Exceptions
            else:
                msgs += self.__ConverColor__(str(i), color).split("\n")
        return msgs
    def Log(self, *msg):
        empty = False
        for i in self.__GetMsg__(*msg, color=__Colors__.LOG):
            self.__LogMsg__(i + __Colors__.__ENDC__, _type="LOG", empty=empty, color=__Colors__.LOG)
            empty = True
    def LogError(self, *msg):
        empty = False
        for i in self.__GetMsg__(*msg, color=__Colors__.ERROR):
            self.__LogMsg__(i + __Colors__.__ENDC__, _type="ERR", empty=empty, color=__Colors__.ERROR)
            empty = True
    def LogWarning(self, *msg):
        empty = False
        for i in self.__GetMsg__(*msg, color=__Colors__.WARNING):
            self.__LogMsg__(i + __Colors__.__ENDC__, _type="WAR", empty=empty, color=__Colors__.WARNING)
            empty = True
if (__name__=="__main__"):
    print("Test")
    Debug = Debuger("LOG TEST")
    Debug.Log("Hello", "Hello World", "Error")
