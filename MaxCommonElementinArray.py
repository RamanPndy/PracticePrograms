def most_commom(lst):
    return max(set(lst),key=lst.count)

lst = [1,5,7,3,7,3,1,8,4,7,4,2,7]
print lst

print most_commom(lst)