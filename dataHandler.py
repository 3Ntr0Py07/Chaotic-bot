"""
This Library contains the local data handling for the manual server device software
"""

############################################################# Imports ##################################################################

from abc import ABC, abstractmethod
import json
import os
import shutil
import sys
import time

############################################################# Classes ##################################################################

class __HandlerClass__(ABC):
    @abstractmethod
    def __init__(self, _type):
        self._type_ = _type

    def __LoadData__(self, name, newEntry):
        __error = None
        __reulte = None
        __LogMsg__("Loading " + str(self._type_) + "." + str(name) + " from config file.")
        try:
            d = open(JSON_PATH, "rb")
            dataDic = json.load(d)
            __reulte = dataDic[str(self._type_)][str(name)]
        except Exception as _err:
            __error = _err
            __LogMsg__("Loading " + str(self._type_) + "." + str(name) + " faild. " + str(_err), "WAR")
            if (newEntry):
                __LogMsg__(" => Creating new empty entry " + str(self._type_) + "." + str(name) + ".")
                self.__SaveData__(name, None)
        finally:
            d.close()
        if (__error != None):
            raise __error
        __LogMsg__("Loading " + str(self._type_) + "." + str(name) + " from config file was succesfully.")
        return __reulte
    
    def __SaveData__(self, name, value):
        __error = False
        __LogMsg__("Start Saving")
        __LogMsg__(" => Loading " + str(self._type_) + "." + str(name) + " from config file.")
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
            __LogMsg__(" => Loading " + str(self._type_) + "." + str(name) + " faild. " + str(_err), "ERR")
        finally:
            d.close()
        if (__error):
            return
        __LogMsg__(" => Loading " + str(self._type_) + "." + str(name) + " from config file was succesfully.")
        __LogMsg__(" => Saving " + str(self._type_) + "." + str(name) + " to config file.")
        try:
            d = open(JSON_PATH, "w")
            json.dump(dataDic, d)
            __LogMsg__(" => Saving " + str(self._type_) + "." + str(name) + " to config file was succesfully.")
        except Exception as _err:
            __LogMsg__(" => Saving " + str(self._type_) + "." + str(name) + " faild. " + str(_err), "ERR")
        finally:
            d.close()
        __LogMsg__("End Saving")
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
    __LogMsg__("Start INIT")
    if (not os.path.exists(JSON_PATH)):
        __LogMsg__(" => Create new config file at '" + str(os.path.abspath(JSON_PATH)) + "'.")
        __CreatJson__()
    __LogMsg__(" => Create config backup.")
    try:
        shutil.copy(JSON_PATH, BACKUP_PATH)
        __LogMsg__(" => Creating config backup was succesfully. ")
    except Exception as _err:
        __LogMsg__(" => Creating config backup faild. " + str(_err), "ERR")
    __LogMsg__(" => Load config file.")
    try:
        d = open(JSON_PATH, "rb")
        dataDic = json.load(d)
        __LogMsg__(" => Loading config file was succesfully.")
    except Exception as _err:
        __LogMsg__(" => Loading config file faild. " + str(_err) + " Creat new.", "WAR")
        __CreatJson__()
        dataDic = {}
    finally:
        d.close()
        __LogMsg__("End INIT")
    
def __CreatJson__():
    try:
        d = open(JSON_PATH, "w")
        d.write("{}")
    finally:
        d.close()

############################################################# Run Init #################################################################

JSON_PATH = "config.json"
BACKUP_PATH = "config.json.backup"

__Init__()

Git = __GitClass__()
ChancelIDs = __ChannelIDClass__()

if (__name__ == "__main__"):
    Test = __TestClass__()




