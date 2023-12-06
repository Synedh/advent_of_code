time, distance =  [int(''.join(l.split()[1:])) for l in open('input')]
print(sum(i * (time - i) > distance for i in range(time)))
