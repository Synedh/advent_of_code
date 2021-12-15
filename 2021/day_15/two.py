from copy import deepcopy

with open('input') as file:
    l = file.readlines()

DangerLevel = []
PathTotalDangerLevel = []
for k1 in range(5):
    for i in l:
        DangerLevel.append([])
        PathTotalDangerLevel.append([])
        for k2 in range(5):
            for j in i.strip():
                PathTotalDangerLevel[-1].append(10000000)
                DangerLevel[-1].append(int(j) + k1 + k2)
                while(DangerLevel[-1][-1] > 9):
                    DangerLevel[-1][-1] -= 9

TotalDangerLevelLast = []
PathTotalDangerLevel[0][0] = 0

while True:
    for i in range(len(PathTotalDangerLevel)):
        for j in range(len(PathTotalDangerLevel[-1])):
            if (i == 0 and j == 0):
                continue
            minimum = 1000000000
            if i > 0:
                minimum = min(PathTotalDangerLevel[i-1][j], minimum)
            if j > 0:
                minimum = min(PathTotalDangerLevel[i][j-1], minimum)
            if i < len(PathTotalDangerLevel) - 1:
                minimum = min(PathTotalDangerLevel[i+1][j], minimum)
            if j < len(PathTotalDangerLevel[-1]) - 1:
                minimum = min(PathTotalDangerLevel[i][j+1], minimum)
            PathTotalDangerLevel[i][j] = min(minimum + DangerLevel[i][j], PathTotalDangerLevel[i][j])
    if PathTotalDangerLevel == TotalDangerLevelLast:
        break
    TotalDangerLevelLast = deepcopy(PathTotalDangerLevel)
print(PathTotalDangerLevel[-1][-1])