__pipList__ = []
import os
while True:
    try:
        import sys
        import time
        import colorama
    except ModuleNotFoundError as _err:
        if str(_err) in __pipList__:
            raise _err
        __pipList__.append(str(_err))
        libName = str(_err).split("'")[1]
        print("Install " + libName)
        os.system("pip install " + libName)
        os.system("pip install python-" + libName)
        continue
    break

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
    TRACEBACK = ERROR
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'

class Debuger():
    TRACEBACK_LINE_LENGTH = 8
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
        for i in msg.split(__Colors__.ENDC):
            msgColorText = i + __Colors__.__ENDC__ + msgColor
        return msgColorText[:-(len(__Colors__.__ENDC__) + len(msgColor))]
    def __GetLine__(self, file, line):
        fileLine = open(file).readlines()[line - 1]
        startLen = 0
        for i in fileLine:
            if (i in [" ", "\t"]):
                startLen += 1
            else:
                break
        return fileLine[startLen:-1]
    def __GetTraceback__(self, sht, traceback):
        print(sht + "\u2560\u2550\u2550[" + self.__SetLength__(traceback.tb_lineno, self.TRACEBACK_LINE_LENGTH, "0") + "]\u2550[" + str(traceback.tb_frame.f_code.co_filename) + "]\u2550[" + traceback.tb_frame.f_code.co_name + "]\u2550>", self.__GetLine__(traceback.tb_frame.f_code.co_filename, traceback.tb_lineno))
        if (traceback.tb_next != None):
            PrintTraceback(traceback.tb_next)
    def __LogException__(self, _type="ERR"):
        sh = self.__GetSpaceHeader__(_type)
        exc_info = sys.exc_info()
        print(__Colors__.TRACEBACK + sh + "Traceback (most recent call last):")
        sht = sh + (" " * 4)
        if (None in exc_info):
            print(sht + "\u2502")
            print(sht + "\u2514\u2500 N/A" + __Colors__.__ENDC__)
            return
        print(sht + "\u2551")
        traceback = exc_info[2]
        self.__GetTraceback__(sht, traceback)
        print(sht + "\u2551")
        print(sht + "\u255A\u2550 " + str(exc_info[0].__name__) + ":", str(exc_info[1]) + __Colors__.__ENDC__)
    def __GetMsg__(self, *msg, color=__Colors__.WHITE):
        msgs = []
        for i in msg:
            if (type(i) == TypeError):
                msgs += self.__ConverColor__(str(i.with_traceback()), color).split("\n") # Exceptions
            else:
                msgs += self.__ConverColor__(str(i), color).split("\n")
        return msgs
    def Log(self, *msg, addException=False):
        empty = False
        for i in self.__GetMsg__(*msg, color=__Colors__.LOG):
            self.__LogMsg__(i + __Colors__.__ENDC__, _type="LOG", empty=empty, color=__Colors__.LOG)
            empty = True
        if (addException):
            self.__LogException__("LOG")
    def LogError(self, *msg, addException=True):
        empty = False
        for i in self.__GetMsg__(*msg, color=__Colors__.ERROR):
            self.__LogMsg__(i + __Colors__.__ENDC__, _type="ERR", empty=empty, color=__Colors__.ERROR)
            empty = True
        if (addException):
            self.__LogException__("ERR")
    def LogWarning(self, *msg, addException=False):
        empty = False
        for i in self.__GetMsg__(*msg, color=__Colors__.WARNING):
            self.__LogMsg__(i + __Colors__.__ENDC__, _type="WAR", empty=empty, color=__Colors__.WARNING)
            empty = True
        if (addException):
            self.__LogException__("WAR")
if (__name__=="__main__"):
    print("Test")
    Debug = Debuger("LOG TEST")
    Debug.Log("Hello", "Hello World", "Error")
    try:
        a = 1/0
    except:
        Debug.LogError("Calculation faild!")
