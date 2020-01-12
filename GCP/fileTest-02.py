#!/usr/bin/env python3

testFile = open('romeo.txt','r')
out = open('00_test.txt','r+')

for i in testFile:out.write(i)
newTest = out.read()
print(newTest)


testFile.close()
out.close()
