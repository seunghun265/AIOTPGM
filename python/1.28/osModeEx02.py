import os

fileList = os.listdir()

for f in fileList:
    if os.path.isfile(f):   # ⭐ 핵심
        infile = open(f, "r", encoding="utf-8")
        for line in infile:
            e = line.strip()
            if "open" in e:
                print(f, ":", e)
        infile.close()
