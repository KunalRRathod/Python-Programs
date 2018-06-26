import collections
from collections import Counter
a= open("C:/Users/Kunal Rathod/Documents/NSWDG.txt", "r")
count = 0
list = 0
for line in a:
   words = line.split()
   for word in words:
        if word in words:
          count=count+1
print(count)