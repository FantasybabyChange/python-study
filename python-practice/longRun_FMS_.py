import threading
import time
import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket
import requests,json

task_next = -1
ip = "127.0.0.1"
async def startup(uri):
    global task_next
    global url
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        while True:
            mes = await converse.receive()
            d = json.loads(mes)
            #  TaskVO
            if d["className"] == "TaskVO":
                print('{time}-Client receive: {rec}'
                      .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
                print("****************************")
                task_next = d["object"]["status"]

def getTS():
    remote = "ws://" + ip + ":7888/websocket?msgType=ServerPush"
    try:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')

class Send():
    def __init__(self):
        global url
        self.lowPower = 0.4
        self.hightPower = 0.8
        self.robot = "3001"
        # full monkey
        self.graphUuid = "60a7b885-e2da-4221-ac60-3ff732c55c75"
        self.graphLabel = "fullMonkey"
        self.rackIds = "100001ID"
        self.username = "admin"
        self.password = "e10adc3949ba59abbe56e057f20f883e"

        self.url = "http://" + ip +":7777"
        self.urlTask = self.url+"/api/schedule/tb-task/dispatch"
        # dumps：将python对象解码为json数据
        # 字符串格式
        # 长运的任务,运动，搬运，运动，搬运

        self.task = [{"type":0,"taskTemplateCode":"T0001","agvId":self.robot,"agvUuid":self.robot,"graphUuid":self.graphUuid,
                      "graphLabel":self.graphLabel,"points":"003000KK007000"},
                     {"type":0,"taskTemplateCode":"T0002","agvId":self.robot,"agvUuid":self.robot,"graphUuid":self.graphUuid,
                      "graphLabel":self.graphLabel,"points":"004000KK006000,005000KK008000","rackIds":self.rackIds},
                     {"type":0,"taskTemplateCode":"T0001","agvId":self.robot,"agvUuid":self.robot,"graphUuid":self.graphUuid,
                      "graphLabel":self.graphLabel,"points":"005000KK007000"},
                     {"type": 0, "taskTemplateCode": "T0002", "agvId": self.robot, "agvUuid": self.robot,"graphUuid": self.graphUuid,
                      "graphLabel": self.graphLabel,"points": "005000KK008000,004000KK006000", "rackIds": self.rackIds}
        ]

        self.tack_charging = {"type":1,"taskTemplateCode":"T0006","agvId":self.robot,"agvUuid":self.robot,"graphUuid":self.graphUuid,
                              "graphLabel":self.graphLabel,"points":""}

        self.stop_charging = {"type":2,"taskTemplateCode":"T0005","agvId":self.robot,"agvUuid":self.robot,"graphUuid":self.graphUuid,
                              "graphLabel":self.graphLabel,"points":""}
        self.headers = {'Content-Type': 'application/json', 'Authorization': self.get_authorization()}

    def get_authorization(self):

        ret = requests.post(url= self.url +"/api/v1/admins/login",
                            data=json.dumps({"password": self.password, "username": self.username}),
                            timeout=1, headers={'Content-Type': 'application/json'})
        print(ret.text)
        return (json.loads(ret.text)["data"]["token"])

    def sendtask2TS(self):
        global task_next
        for num in range(len(self.task)):
            print("send_start--->",self.task[num])
            res_task = requests.post(url=self.urlTask, data=json.dumps(self.task[num]), headers=self.headers)
            print("res_task--->",res_task)
            #time.sleep(5)
            # 排队状态完成
            while(True):
                time.sleep(1)
                if (task_next == 2):
                    task_next =-1
                    break


    def getcharge(self):
        getchargUrl  = self.url + "/api/v1/agvs/%7BresourceUuid%7D/runtime?resourceUuid="+self.robot
        res = requests.get(url=getchargUrl, data=json.dumps(self.tack_charging),
                      headers=self.headers)
        d = json.loads(res.text)
        power = d["runtimeState"]["batteryStateInfo"]["stateOfCharge"]
        return power


    def charge(self):
        # 充电
        power = self.getcharge()
        if power < self.lowPower:
            res_task_charging = requests.post(url=self.urlTask, data=json.dumps(self.tack_charging),
                                              headers=self.headers)
            while( self.getcharge() < self.hightPower):
                time.sleep(60)
            res_task_stopCharge = requests.post(url=self.urlTask, data=json.dumps(self.stop_charging),
                                                headers=self.headers)

    def longTest(self):
        while(True):
            self.charge()
            self.sendtask2TS()


if __name__ == '__main__':
    t1 = threading.Thread(target=getTS)
    t1.start()
    send = Send()
    time.sleep(1)
    t2 = threading.Thread(target=send.longTest)
    t2.start()
