import time
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
        po = 0
        for station in self.station:
            while po != self.station[station]:
                po += self.speed
                print(self.commercial[random.randrange(len(self.commercial))])
                time.sleep(1)
            print("%s 역에 도착했습니다."%(station))
            time.sleep(3)
