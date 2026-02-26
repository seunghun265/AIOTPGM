base = int(input("사각형의 너비 입력 :"))
height = int(input("사각형의 높이 입력 :"))

area = base * height

print(f"높이가 {height}이고 밑변이 {base}인 직사각형의 면적은 {area}입니다.")
print("높이가", height,"이고 밑변이",base, "인 직사각형의 면적은",area,"입니다.")
print(f"높이가 {0}이고 밑변이 {1}인 직사각형의 면적은 {2}입니다.".format(height, base, area))
print("높이가 %d이고 밑변이 %d인 직사각형의 면적은 %d입니다." % (height, base, area))

print(f"높이가 {height}이고 밑변이 {base}인 직사각형의 면적은 {area} 입니다")
print("높이가", height,"이고 밑변이", base, "인 직사각형의 면적은", area, "입니다")
print(f"높이가{0}이고 밑변이{1}인 직사각형의 면적은{3}입니다.".format(height, base, area))
print("높이가 %d 이고 밑변이 %d인 직사각형의 면적은 %d 입니다" %(height,base,area))