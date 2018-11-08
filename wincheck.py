def winnerCheck(fieldsSet):

    for i in range(len(fieldsSet)):
        for j in range(3):
            if fieldsSet[j*3+0]+fieldsSet[j*3+1]+fieldsSet[j*3+2] == 3:
                return 0
            elif fieldsSet[j*3+0]+fieldsSet[j*3+1]+fieldsSet[j*3+2] == -3:
                return 1
        for j in range(3):
            if fieldsSet[j+0]+fieldsSet[j+3]+fieldsSet[j+6] == 3:
                return 0
            elif fieldsSet[j+0]+fieldsSet[j+3]+fieldsSet[j+6] == -3:
                return 1
        if fieldsSet[0]+fieldsSet[4]+fieldsSet[8] == 3:
            return 0
        elif fieldsSet[0]+fieldsSet[4]+fieldsSet[8] == -3:
            return 1
        if fieldsSet[2]+fieldsSet[4]+fieldsSet[6] == 3:
            return 0
        elif fieldsSet[2]+fieldsSet[4]+fieldsSet[6] == -3:
            return 1
    return -1

def winnerOutput(retcd):

    if retcd == 0:
        print('○の勝ち')
    else:
        print('×の勝ち')
            