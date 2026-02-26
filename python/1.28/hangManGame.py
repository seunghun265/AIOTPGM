import random

guesses = ''
turns = 10

inFile = open("0128/word.txt","r", encoding="utf-8")
lines = inFile.readlines()
word = random.choice(lines).strip()

while turns >0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end="")
    else:
        print("_",end="")
        failed += 1
    if failed == 0:
        print("사용자 승리")
        break
    print("")
    guess = input("단어를 추측하세요")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("틀렸음")
        print(str(turns)+"기회가 남았음")
        if turns == 0:
            print(f"사용자 패배\n정답은 {word}입니다")
    
inFile.close()


