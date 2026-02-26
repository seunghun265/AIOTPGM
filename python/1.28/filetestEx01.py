outfile = open("1.28/output.txt", "w")

for i in range(1,11):
    outfile.write(str(i)+"\n")
outfile.close()
    
infile = open("1.28/output.txt","r")
line = infile.readline()
while line !="":
    print(line)
    line = infile.readline()
infile.close()