STRING = input()
BUF = ''
FLAG = 0
EXIT_FLAG = 0
NUM = 0
while EXIT_FLAG == 0:
    BUF += STRING[NUM]
    NUM += 1
    if len(STRING) % len(BUF) == 0:
        COUNTER = 1
        ITERATION = 0
        while COUNTER <= len(STRING) // len(BUF):
            for Z in range(len(BUF)):
                if BUF[Z] == STRING[Z + ITERATION*len(BUF)]:
                    FLAG = 1
                else:
                    FLAG = 0
                    break
            Z = 0
            ITERATION += 1
            COUNTER += 1
            if FLAG == 0:
                break
        if FLAG == 1:
            break
print(ITERATION)
