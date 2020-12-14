import subway #각 사람들의 일상을 엿볼 수 있도록
              #버스, 택시, 집 추가해야함

class people:
    speed = 4
    money = 0

class car:
    speed = 80



sb = subway.subway()

speed = 50
station = {"a" : 50, "b" : 150, "c" : 500, "d" : 1000, "e" : 1150}
commercial = ["행복을 이어주는 사람들 - 한국도로공사", "비비는 맛에 산다 - 팔도비빔면", "뭘 먹어도 맛있다 - BBQ", "물만큼은 삼다수로 산다 - 삼다수"]


sb.set_all(50, {"a" : 50, "b" : 150, "c" : 500, "d" : 1000, "e" : 1150}, ["행복을 이어주는 사람들 - 한국도로공사", "비비는 맛에 산다 - 팔도비빔면", "뭘 먹어도 맛있다 - BBQ", "물만큼은 삼다수로 산다 - 삼다수"])
sb.run_subway()