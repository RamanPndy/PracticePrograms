import math

def solution(n):
    maxLength = 0
    lastMax = maxLength
    numberOfDigit = 0
    while maxLength < n:
        lastMax = maxLength
        maxLength += math.pow(2, numberOfDigit) * numberOfDigit
        if maxLength >= n:
            break
        else:
            numberOfDigit += 1

    position = n - lastMax
    positionInNumber = numberOfDigit - position % numberOfDigit + 1 if position % numberOfDigit != 0 else 1
    numberPosition = math.ceil(position / numberOfDigit) - 1

    if numberPosition % math.pow(2, positionInNumber) < math.pow(2, positionInNumber - 1):
        return 'Hacker'
    else:
        return 'Earth'

T = int(raw_input())
for i in xrange(T):
	n = int(raw_input())
	print solution(n)