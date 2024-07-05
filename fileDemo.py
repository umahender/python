'''
read()
readline()
readlines()
write()
writelines()
close

'''
fp=open('abc.txt','r')
print(fp.name)
print(fp.mode)
content=fp.read(5)
print(content)