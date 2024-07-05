import re
text='949339'
x=re.search("/^[0-9]{6}",text)
print(x)