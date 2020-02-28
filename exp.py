s="#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
print(s.isalnum())
hasalpha=False
for a in s:
    if a.isalpha():
        hasalpha=True
        break
print(hasalpha)

hasdigit=False
for a in s:
    if a.isdecimal():
        hasdigit=True
        break
print(hasdigit)

haslo=False
for a in s:
    if a.islower():
        haslo=True
        break
print(haslo)

hashigh=False
for a in s:
    if a.upper():
        hashigh=True
        break
print(hashigh)