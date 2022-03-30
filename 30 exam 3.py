s1 = input('Enter String one: ')
s2 = input('Enter String two: ')

def str_comp(str1, str2):
    if str1 == str2:
        return 'identical'
    else:
        return 'not identical'

print(str_comp(s1,s2))
    