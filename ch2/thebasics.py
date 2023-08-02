message = 'hello from VS code'
print(message)

message = 'goodbye from VS code!!!'
print(message)

message = 'ada lovelace'
print(message.title())
print(message.upper())
print(message.lower())

firstName = 'Ada'
lastName = 'Lovelaces'
fullName = f"{firstName} {lastName}"
print(fullName)
print(f"Hello, \n\t {fullName.title()}")

favLang = 'Python    '
print(favLang)
print(favLang.rstrip())

print(f"my favortie laguage is {favLang}!")
print(f"my favortie laguage is {favLang.rstrip()}!")


url = 'https://nostarch.com'
print(url)
url = url.removeprefix('https://')
print(url)


personName = 'Bailey'
message = (f"Hello {personName}, would you like to play a game?")
print(message)

print(message.title())
print(message.lower())
print(message.upper())

quote = 'Albert Einstein once said, "A person does stuff."'
print(quote)

famPerson = 'Bob Dole'
quote = 'Let them eat cake'
print(f'{famPerson} once said \n\t"{quote}"')


# numbers

num = 4/2
print(num)


x, y, z = 0, 0, 0
print(x, y, z)
print(4+4)
print(4*2)
print(16/2)
print(10-2)

favNum = 13
print(f"Favorite number is {favNum}!")
