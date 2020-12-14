import time #사람들 탑승하는게 추가되어야 함
import random

class subway:
    def __init__(self):
        self.speed = 0
        self.station = {}
        self.commercial = []
    
    def set_all(self, speed, station, commercial):
        self.speed = speed
        self.station = station
        self.commercial = commercial

    def run_subway(self):
        
        while True:
            po = 0
            for station in self.station:
                while po != self.station[station]:
                    po += self.speed #현재 초속 50km 로 설정됨 시속 50km로 바꿔야 함
                    print(self.commercial[random.randrange(len(self.commercial))])
                    time.sleep(1)
                print("%s 역에 도착했습니다."%(station))
                time.sleep(1)
                print("내리실 문은 %s쪽 입니다."%(random.choice(["왼", "오른"])))
                time.sleep(1)
                print("This stop is %s station." %(station))
                time.sleep(1)
                print("The doors are on your %s." %(random.choice(["left", "right"])))
                time.sleep(3)
                print("문이 닫힙니다.")
                time.sleep(1)
                print("The doors are closing.")
                time.sleep(1)