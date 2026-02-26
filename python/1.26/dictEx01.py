# 1.연락처 추가
# 2.연락처 삭제
# 3.연락처 검색
# 4.연락처 출력
# 5.종료
# 메뉴항목을 선택하시오 : 1
# 이름: KIM
# 전화번호: 123 4567
# 1.연락처 추가
# 2.연락처 삭제
# 3.연락처 검색
# 4.연락처 출력
# 5.종료
# 메뉴항목을 선택하시오 : 4
# KIM의 번화번호 : 123 4567

def main = {}
    addressBook = {}
    while True:
        user = displayMenu();
    if user == 1 :
        name,number = getContact()
        addressBook[name]=number
    elif user == 2 :
        name,number = getContack()
        addressBook.pop(name)
    elif user == 3 :
        pass
    elif user == 4 :
        for key in sorted(addressBook):
            print(key,"의 전화번호", addressBook[key])
    else :
        break

def getContack():                                 #이름과 전화번호를 입력 받아서 반환시킨다
    name = input("이름: ")
    number = input("전화번호: ")
    return name,number                            #튜플로 반환

def displayMenu():
    print("1.연락처 주가")
    print("2.연락처 삭제")
    print("3.연락처 검색")
    print("4.연락처 출력")
    print("5.종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

main()