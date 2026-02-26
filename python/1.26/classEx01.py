class Counter:
    def __init__(self):            # constructor 생성자라고 한다, 대부분 변수의 값을 초기화함
        self.cnt = 0
        
    def increment(self):
        self.cnt += 1
        
c1 = Counter()  #클래스를 이용하여 객체를 만들 떄, 가장 먼저 실행되는 메소드는 __init__입니다.
c2 = Counter()
c1.cnt = 8
print(f"c1 객체의 cnt 변수의 값은{c1.cnt}입니다")
c1.increment()
print(f"c1 객체의 매소드인 increment()를 호출한 후 c1 객체의 cnt 변수의 값은 {c1.cnt}입니다.")
c2.cnt = 100
print(f"c2 객체의 cnt 변수의 값은 {c2.cnt}입니다.")
c2.increment()
print(f"c2 객체의 메소드인 increment()를 호출한 후 c2 객체의 cnt 변수의 갓은 {c2.cnt}입니다.")




