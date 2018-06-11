FILE_NAME = 'C:/Users/Kunal Rathod/Documents/NSWDG.txt'

wordCounter = {}

with open(FILE_NAME,'r') as fh:
  for line in fh:

    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:

      if word not in wordCounter:
        wordCounter[word] = 1
      else:

        wordCounter[word] = wordCounter[word] + 1

print('{:15}{:3}'.format('Word','Count'))
print('-' * 18)

for  (word,occurance)  in wordCounter.items():
  print('{:15}{:3}'.format(word,occurance))