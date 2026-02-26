inFileName = open("1.28/sales.txt","r",encoding="utf-8")
outFileName = open("summary.txt","w",encoding="utf-8")

sum = 0;
count = 0;
line = inFileName.readline()
while line != "":                     #더이상 읽을게 없을떄 까지 반복
    value = int(line)
    sum += value
    count += 1        #1씩 증가
    line = inFileName.readline()

outFileName.write(f"총 매출 = {sum}\n")
outFileName.write(f"평균 일 매출 = {sum/count}\n")

inFileName.close()
outFileName.close()