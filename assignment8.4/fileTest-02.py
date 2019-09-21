testFile = open('romeo.txt','r')
out = open('00_test.txt','r+')

for i in testFile:out.write(i)

testFile.close()
out.close()
