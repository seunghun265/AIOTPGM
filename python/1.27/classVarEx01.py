class Televizion : 
    serialNumber = 0               #이것이 클래스 변수
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Televizion.serialNumber += 1                      # 객체 만들떄 마다 1씩 추가되서 출력됨
        self.number = Televizion.serialNumber
        
    def show(self):
        print(self.channel, self.volume, self.on, self.number)
        
tv1 = Televizion(12,15,True)
tv1.show()
tv2 = Televizion(24,14,True)
tv2.show()
tv3 = Televizion(23,14,False)
tv3.show()