# given a data table in the form of headers and data 
# lines are separated by \n and values are separated by ,
# return the max value given a column name example:
# id, name, age, room, dep
# 1,  Jack,  68,   T,  8
# 17, Betty, 28,   F, 7
# given: 
# S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"
# C = "age"
# it should return 68

def solution(s, c):
    lines = s.split('\n')
    data_values = []
    header = lines[0].split(",")
    header_index = header.index(c)
    for lines in lines[1:]:
        data = lines.split(",")
        data_values.append(data[header_index])
    return max(data_values)


S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"
C = "age"
result = solution(S, C)
print(result)