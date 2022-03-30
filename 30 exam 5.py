fo = open('myfile.txt', 'r')

vowel = 'aeiouAEIOU'
line = fo.readline()
while line != '':
    for char in line:
      if char in vowel:
        vowel += 1
    line = fo.readline()
        
print(vowel)
    
# i cheated