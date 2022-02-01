#   Dylan Blaine
#   Dictionary Word Search


import random

dictionary = open('dictionary.txt','r')
words = dictionary.readlines()
dictionary.close()

length = int(input("Enter the length of the words to find:\nLENGTH>")) + 1
seed = input("Enter the seed to use:\nSEED>")

words_list = []

num_words = 0

for i in range(127142):
    x = len(words[i])
    if (x == length):
        num_words = num_words + 1
        words_list.append(words[i])
        
random.seed(seed)
rand_num = random.randint(0,len(words_list))

print('The number of words with length {} is:'.format(length))
print('OUTPUT', num_words)

if (num_words > 0):
    print('Here is one random word with length {}:'.format(length))
    print('OUTPUT', words_list[rand_num])
else:
    print('There are no words of length {} in the dicitonary.'.format(length))
    print('OUTPUT None')
                          
