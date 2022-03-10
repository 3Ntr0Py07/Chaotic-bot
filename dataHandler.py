"""
This Library contains the local data handling for the manual server device software
"""
#Julians Zugang
############################################################# Imports ##################################################################

# Global

__pipList__ = []
import os
while True:
    try:
        from abc import ABC, abstractmethod
        import json
        import shutil
        import sys
        import time
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

# Lokal

from localDebuger import Debuger

############################################################# Classes ##################################################################

class __HandlerClass__(ABC):
    @abstractmethod
    def __init__(self, _type):
        self._type_ = _type

    def __LoadData__(self, name, newEntry):
        __error = None
        __reulte = None
        Debug.Log("Loading " + str(self._type_) + "." + str(name) + " from config file.")
        try:
            d = open(JSON_PATH, "rb")
            dataDic = json.load(d)
            __reulte = dataDic[str(self._type_)][str(name)]
        except Exception as _err:
            __error = _err
            Debug.LogWarning("Loading " + str(self._type_) + "." + str(name) + " faild. ", str(_err))
            if (newEntry):
                Debug.Log(" => Creating new empty entry " + str(self._type_) + "." + str(name) + ".")
                self.__SaveData__(name, None)
        finally:
            d.close()
        if (__error != None):
            raise __error
        Debug.Log("Loading " + str(self._type_) + "." + str(name) + " from config file was succesfully.")
        return __reulte
    
    def __SaveData__(self, name, value):
        __error = False
        Debug.Log("Start Saving")
        Debug.Log(" => Loading " + str(self._type_) + "." + str(name) + " from config file.")
        try:
            d = open(JSON_PATH, "rb")
            dataDic = json.load(d)
            try:
                a = dataDic[str(self._type_)]
            except:
                dataDic[str(self._type_)] = {}
            dataDic[str(self._type_)][str(name)] = value
        except Exception as _err:
            __error = True
            Debug.LogError(" => Loading " + str(self._type_) + "." + str(name) + " faild. " + str(_err))
        finally:
            d.close()
        if (__error):
            return
        Debug.Log(" => Loading " + str(self._type_) + "." + str(name) + " from config file was succesfully.")
        Debug.Log(" => Saving " + str(self._type_) + "." + str(name) + " to config file.")
        try:
            d = open(JSON_PATH, "w")
            json.dump(dataDic, d)
            Debug.Log(" => Saving " + str(self._type_) + "." + str(name) + " to config file was succesfully.")
        except Exception as _err:
            Debug.LogError(" => Saving " + str(self._type_) + "." + str(name) + " faild. " + str(_err))
        finally:
            d.close()
        Debug.Log("End Saving")
    def Load(self, name, nullable=True, newEntry=False):
        if ((not nullable) and (newEntry)):
            raise ReferenceError("newEntry can not be True when nullable is False")
        try:
            return self.__LoadData__(name, newEntry)
        except KeyError as _err:
            if (nullable):
                return None
            else:
                raise _err
            
    def Save(self, name, value):
        return self.__SaveData__(name, value)

class __GitClass__(__HandlerClass__):
    #override
    def __init__(self):
        super().__init__("Git")

class __ChannelIDClass__(__HandlerClass__):
    #override
    def __init__(self):
        super().__init__("ChannelID")
        
class __TestClass__(__HandlerClass__):
    #override
    def __init__(self):
        super().__init__("Test")

############################################################# Functions ################################################################



def __Init__():
    Debug.Log("Start INIT")
    if (not os.path.exists(JSON_PATH)):
        Debug.Log(" => Create new config file at '" + str(os.path.abspath(JSON_PATH)) + "'.")
        __CreatJson__()
    Debug.Log(" => Create config backup.")
    try:
        shutil.copy(JSON_PATH, BACKUP_PATH)
        Debug.Log(" => Creating config backup was succesfully. ")
    except Exception as _err:
        Debug.LogError(" => Creating config backup faild. " + str(_err))
    Debug.Log(" => Load config file.")
    try:
        d = open(JSON_PATH, "rb")
        dataDic = json.load(d)
        Debug.Log(" => Loading config file was succesfully.")
    except Exception as _err:
        Debug.LogError(" => Loading config file faild. " + str(_err) + " Creat new.")
        __CreatJson__()
        dataDic = {}
    finally:
        d.close()
        Debug.Log("End INIT")
    
def __CreatJson__():
    try:
        d = open(JSON_PATH, "w")
        d.write("{}")
    finally:
        d.close()

############################################################# Run Init #################################################################

JSON_PATH = "config.json"
BACKUP_PATH = "config.json.backup"

Debug = Debuger("DATA HANDLER")

__Init__()

Git = __GitClass__()
ChancelIDs = __ChannelIDClass__()

if (__name__ == "__main__"):
    Test = __TestClass__()




