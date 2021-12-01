import threading
import time
import os
import logging
from logging import handlers
import json
import requests
from readConfig import ReadConfig


# other configuration
RC = ReadConfig()

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',backCount=100,fmt='%(asctime)s - %(threadName)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.RotatingFileHandler(filename=filename,maxBytes=20000000,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)

logPath = RC.get_log() + time.strftime('%Y-%m-%d-%H-%M-%S') + "/"
if not os.path.exists(logPath):
    os.makedirs(logPath)   
log = Logger(logPath + "LongRun_AutoChange_Multi_log.log", level='info')


class Send():
    def __init__(self):

        self.ip = RC.get_http()
        log.logger.info("Server IP is: %s", self.ip)

        self.graphUuid,self.graphLabel,self.rackIds = RC.get_wgs()
        self.username,self.password = RC.get_login()
        
        self.url = "http://" + self.ip  +":7777"
        self.urlTask = self.url+"/api/schedule/tb-task/dispatch"

        self.robotMovepost = self.strTolist(RC.get_task("Movepost"))
        log.logger.info("Move target candidate: %s", str(self.robotMovepost))

        self.moveTask = {"type":0,"taskTemplateCode":"T0001","agvId":"","agvUuid":"","graphUuid":self.graphUuid,
                      "graphLabel":self.graphLabel,"points":""}

        self.headers = {'Content-Type': 'application/json', 'Authorization': self.get_authorization()}
        self.robotlist = self.queryAGVList()

    def get_authorization(self):

        ret = requests.post(url= self.url +"/api/v1/admins/login",
                            data=json.dumps({"password": self.password, "username": self.username}),
                            timeout=1, headers={'Content-Type': 'application/json'})
        return json.loads(ret.text)["data"]["token"]
    
    def strTolist(self,string):
        return string.split(",")

    def judge(self):  
        # check token
        response = requests.get(self.url + "/api/v1/agvs/all", headers=self.headers)
        
        if "token已过期" in response.text or "token已失效" in response.text or "token不存在" in response.text:
            log.logger.info("Generate new token............")
            log.logger.info("New token is: %s", response.text)
            self.headers = {'Content-Type': 'application/json', 'Authorization': self.get_authorization()}     

    def build_starts(self):
        starts_list = []
        for j in range(0, 10, 2):
            for i in range(20):
                starts_list.append(self.axis_to_label(i + 2, j + 7))
        return starts_list

    def build_targets(self):
        targets_list = []
        for j in range(0, 10, 2):
            for i in range(20):
                targets_list.append(self.axis_to_label(i + 2, j + 8))
        return targets_list


    def axis_to_label(self,x,y):
        label_type = 'KK'
        labelX = round(float(x) * 1000)
        labelY = round(float(y) * 1000)
        label = str(labelX).rjust(6, '0') + label_type + str(labelY).rjust(6, '0')
        return label


    def build_move_case(self):
        task_list = dict()
        start_list = self.build_starts()
        target_list = self.build_targets()
        for i in range(100):
            task_list.update({str(7001 + i):{'start':start_list[i], "target":target_list[i]}} )
        return task_list

    def sendtask2TS_Move(self, robotName, point):
        self.judge()
        #运动
        self.moveTask["agvId"] = robotName
        self.moveTask["agvUuid"] = robotName
        self.moveTask["points"] = point
        log.logger.info(">>> Current Move Task is: AGV %s ---> %s", robotName, str(self.moveTask["points"]))
        requests.post(url=self.urlTask, data=json.dumps(self.moveTask), headers=self.headers)
        time.sleep(2) 

    # 获取小车列表
    def queryAGVList(self):
        getchargUrl = self.url + "/api/v1/agvs/all"
        res = requests.get(url=getchargUrl, headers=self.headers)
        dict_robots = json.loads(res.text)

        robot_list = []
        for robot in dict_robots:
            robot_list.append(robot)
        robot_list.sort()
        log.logger.info("List of robots are: %s", str(robot_list))
        return robot_list

    def longTest1(self, robotName, task_list):
        loopNum = 0
        while 1:
            log.logger.info("Running test in Robot %s, loop %s ...", 
                robotName, loopNum)
            start_point = task_list.get(robotName).get('start')
            target_point = task_list.get(robotName).get('target')
            next_point = ''
            if loopNum % 2 == 0:
                next_point = target_point
            elif loopNum % 2 == 1:
                next_point = start_point
            else:
                log.logger.error('error target!')
            self.sendtask2TS_Move(robotName, next_point)
            loopNum += 1
            time.sleep(10)

def move_Long():
    send = Send()
    task_list = send.build_move_case()
    robot_list = send.robotlist
    thread_list = []
    for robot in robot_list:
        temp = Send()
        t = threading.Thread(target=temp.longTest1, args=(robot, task_list,), name="Thread-" + robot)
        thread_list.append(t)
    
    for t in thread_list:
        t.setDaemon(True)  # 设置守护线程，保证主线程结束以后，子线程也结束
        t.start()
        time.sleep(0.1)

    for t in thread_list:
        t.join() 
        
if __name__ == '__main__':
    move_Long()
