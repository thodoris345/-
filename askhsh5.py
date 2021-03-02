import random

SOS = []
ύψος = int(input("Εισάγετε το ύψος του ορθογωνίου: "))
πλάτος = int(input("Εισάγετε το πλάτος  του ορθογωνίου: "))


for k in range(100):
    line1 = []
    line1len = (ύψος*πλάτος)
    line1len2 = float(line1len)
    for i in range(line1len):
            if i > line1len2/2:
                line1.append("O")
            else:
                line1.append("S")
    random.shuffle(line1)
    line2 = []
    for y in range(ύψος):
        line2.append([])
        for x in range(πλάτος):
                line2[y].append(line1.pop(0))
    SOS.append(0)
    for x in range(πλάτος-2):
        for y in range(ύψος):
            if line2[y][x] == "S" and line2[y][x+1] == "O" and line2[y][x+2] == "S":
                SOS[k] += 1
    for x in range(πλάτος):
        for y in range(ύψος-2):
            if line2[y][x] == "S" and line2[y+1][x] == "O" and line2[y+2][x] == "S":
                SOS[k] += 1
    for x in range(πλάτος-2):
        for y in range(ύψος-2):
            if line2[y][x] == "S" and line2[y+1][x+1] == "O" and line2[y+2][x+2] == "S":
                SOS[k] += 1

sumSOS=0
for l in range(len(SOS)-1):
    sumSOS += SOS[l]
avgSOS = sumSOS/len(SOS)
print("Ο μέσος όρος των τριάδων SOS είναι: ", avgSOS)
