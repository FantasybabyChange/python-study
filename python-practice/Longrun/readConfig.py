# coding=utf-8
import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "longRunConfig.ini")

class ReadConfig:
    def __init__(self):
        fd = open(configPath)

        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)


    def get_http(self):
        ip = self.cf.get("HTTP", "ip")
        return ip

    def get_log(self):
        value = self.cf.get("log", "logPath")
        return value

    def get_login(self):
        username = self.cf.get("Login","username")
        password = self.cf.get("Login","password")
        return username,password

    def get_wgs(self):
        graphUuid = self.cf.get("WGS","graphUuid")
        graphLabel  = self.cf.get("WGS","graphLabel")
        rackIds = self.cf.get("WGS","rackIds")
        return graphUuid,graphLabel,rackIds

    def get_task(self,name):
        value = self.cf.get("Task",name)
        return value

    def get_liftpost(self):
        liftpost = self.get_task("liftPost")
        return liftpost

    def get_robotlist(self):
        robotlist = self.get_task("robotlist")
        return robotlist

    def strTolist(self,string):
        return string.split(",")



if __name__ == '__main__':
    read = ReadConfig()
    #print(read.get_url())
