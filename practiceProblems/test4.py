n = 5

try:
    n/0
except Exception as e:
    print e.message

try:
    n/0
except:
    print "Exception Raised"

#open file in Write Mode
# try:
#     f = open("sample.txt","w")
#     f.write("Raman")
# except:
#     print "File Cannot be opened"

#open file in Read mode
# try:
#     f = open("sample.txt","r")
#     print f.read()
# except:
#     print "File Cannot be read"

#opne file in append mode
try:
    f = open("sample.txt","a")
    f.write("Shubham")
except:
    print "File cannot be opened"

x = 5

def scopeTest():
    print x
    global y #Global Keyword is used to define any variable globally
    y = 8
    print y

scopeTest()
print y

x = "raman"
s = list()
for i in x:
    s.append(i)
print s
r = list()
for i in reversed(s):
    r.append(i)
print r

y = ''.join(r)
print y
# s = ["r","m","l"]
#
# print ''.join(s)