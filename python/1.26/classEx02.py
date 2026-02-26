class Television :
    def __init__(self,ch, vo, on):             #매개변수는 self. 안붙여도된다
         self.channel = ch          #속성3개, 멤버 변수
         self.volume = vo            
         self.on = on                 #객체 만들때마다 포함되는 변수 3개

    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self,channel):
        self.channel = channel
    def getChannel(self):
        return self.channel
    def setVolum(self, volum):
        self.volum = volum
    def getVolum(self):
        return self.volum
    def setOn(self,on):
        self.on = on
    def getOn(self):
        return self.on
        
        

tv1 = Television(9,10,True)
# tv1.channel = 10  # 바꾸고 싶을때 
tv2 = Television(6,15,True)
