import re

'''print(re.subn('ub', '~*', "Subject has uber booked alreadyUB", flags=re.IGNORECASE))


p = 'the'
se = 'the jbj the jbun bujb bujn jnuju'

for match in re.finditer(p,se):
    s=match.start();
    e=match.end();
    print(s,e)
    print(se[s:e])

print(re.findall('c',"abchCgc", re.I))

print(re.findall('c',"abchcgcC"), re.I)#ignore case



print(re.escape("this is awesome"))

print(re.escape("this is awesome [a-9], he said \t^WOW"))



p=re.compile('ab |abbb')
print(p.findall("ababbabbbabbbb"))

p=re.compile('abb|abbb')
print(p.findall("ababbabbbabbbb"))

p=re.compile('ab|b{4}')
print(p.findall("ababbabbbabbbb"))

p=re.compile('ab |b+')
print(p.findall("ababbbabbbabbbbbc"))


p=re.compile('b*')
print(p.findall("ababbbabbbabbbb"))

p=re.compile('b?')
print(p.findall("ababbbabbbabbbb"))

p=re.compile('b{2}')
print(p.findall("ababbbabbbabbbb"))

p=re.compile('ab*')
print(p.findall("abaaabbbabbbabbbb"))

p=re.compile('\w+')
print(p.findall("hi you are awesome u jhg jhi oj nvtyfnih huh"))

p=re.compile('\d+')
print(p.findall("i want hima at 4 on 11 july 2011"))

p=re.compile('\d')
print(p.findall("i want hima at 4 on 11 july 2011"))

p=re.compile('\D')
print(p.findall("i want hima at 4 on 11 july 2011"))

'''
#[a\-z] matches a or - or z coz \ escapes it
     
