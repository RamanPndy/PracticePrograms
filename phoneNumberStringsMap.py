phoneNumberStrMap = {0: "", 1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

def phoneNumberUtil(nums, curr, output, leng):
    if curr == leng:
        print (output)
        return
    for i in range(len(phoneNumberStrMap[nums[curr]])):
        output.append(phoneNumberStrMap[nums[curr]][i])
        phoneNumberUtil(nums, curr +1, output, leng)
        output.pop()
        if (nums[curr] == 0 or nums[curr] == 1):
            return

def phoneNumber(nums):
    return phoneNumberUtil(nums, 0, [], len(nums))

print (phoneNumber([2,3,4]))
