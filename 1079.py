qntTestes = int(input())

for x in range(qntTestes):
    def mediaPonderada():
        inputNum = input().split(" ")
        media = ((float(inputNum[0]) * 2) + (float(inputNum[1]) * 3) + (float(inputNum[2]) * 5)) / 10
        return media
    print("{:.1f}".format(mediaPonderada()))
    x += 1
