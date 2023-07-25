import re


message = 'Call me at 913-444-3943'

phoneNumberReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberReg.search(message)
print(mo.group())


phoneGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mog = phoneGroup.search(message)
print(mog.group(1))
print(mog.group(2))


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#mo = batRegex.findall('I am the Batman and drive the Batmobile!')
mo = batRegex.search('I am the Batman and drive the Batmobile!')

print(mo.group())
