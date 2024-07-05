def convert(str):
    ch=list(str)
    for i in range(len(str)):
        if(i==0 and ch[i]!=' ' or ch[i]!=' ' and ch[i-1]==' '):
            if(ch[i]>='a' and ch[i]<='z'):
                ch[i]=chr(ord(ch[i])-ord('a')+ord('A'))
        else:
            if(ch[i]>='A' and ch[i]<='Z'):
                ch[i]=chr(ord(ch[i])+ord('A')-ord('a'))

    str="".join(ch)
    return str

str="hello good morning mahender"
print(convert(str))

def commas(s):
    return s.replace('',',')[1:-1]

print(repr(commas('Apple')))

def remove_word(str,word):
    return str.replace(word,'')
print(remove_word("mahender udutala hi mahender udutala hello","udutala"))