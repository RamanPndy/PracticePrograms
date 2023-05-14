def solution(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    
    if len(arr) == 2:
        return ((arr[0] == arr[1]) or (arr[0][:len(arr[0])-1] == arr[0][len(arr[0])-1:] + arr[1]) or ((arr[0] + arr[1][:1]) == arr[1][1:]))
        
    result = False
    first = arr[0]
    last = arr[-1]
    second = arr[1]
    secondLast = arr[-2]
    n = len(arr)
    
    if first == last:
        filtered = arr[1:n-1]
        result = result or solution(filtered)
        
    firstShort = first[len(first)-1]
    secondLong = first[len(first)-1] + second
    firstLong = first + second[len(second)-1]
    secondShort = second[1:]
    lastShort = last[1:]
    secondLastLong = secondLast + last[0]
    lastLong = secondLast[len(secondLast)-1 :] + last
    secondLastShort = secondLast[:len(secondLast)-1]
    
    if firstShort == last:
        filtered = arr[1:n-1]
        filtered.append(secondLong)
        result = result or solution(filtered)
        
    if firstShort == lastShort:
        filtered = arr[2:n-2]
        filtered.insert(0, secondLong)
        filtered.append(secondLastLong)
        result = result or solution(filtered)
        
    if firstShort == lastLong:
        filtered = arr[2:n-2]
        filtered.insert(0, secondLong)
        filtered.append(secondLastShort)
        result = result or solution(filtered)
        
    if first == lastShort:
        filtered = arr[1:n-2]
        filtered.append(secondLastLong)
        result = result or solution(filtered)
    
    if firstLong == last:
        filtered = arr[2:n-1]
        filtered.append(secondShort)
        result = result or solution(filtered)
        
    if firstLong == lastShort:
        filtered = arr[2:n-2]
        filtered.insert(0, secondShort)
        filtered.append(secondLastLong)
        result = result or solution(filtered)
        
    if firstLong == lastLong:
        filtered = arr[2:n-2]
        filtered.insert(0, secondShort)
        filtered.append(secondLastShort)
        result = result or solution(filtered)
        
    return result
