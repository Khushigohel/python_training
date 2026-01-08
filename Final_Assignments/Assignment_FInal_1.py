''' Assignment 1: Word Counter'''
##  Create a Python script that reads a text file and counts the frequency of each word in the file. ##

frequency_count={}
with open("Day8/file.txt",'r') as file:
    for line in file:
        words=line.lower().split()
        for word in words:
            if word in frequency_count:
                frequency_count[word] += 1
            else:
                frequency_count[word]=1
print("Total frequency of each wor is :")
for item,count in frequency_count.items():
    print(item, "-", count)
    

##  Store the word frequencies in a dictionary. ##
frequency_count={}
with open("Day8/file.txt",'r') as file:
    for line in file:
        words=line.lower().split()
        for word in words:
            if word in frequency_count:
                frequency_count[word] += 1
            else:
                frequency_count[word]=1
print(" \n Total frequency of each wor is :")
print(frequency_count)

## Print out the top 5 most common words and their frequencies.
word_freq = {}

with open("Day8/file.txt", "r") as file:
    for word in file.read().lower().split():
        word_freq[word] = word_freq.get(word, 0) + 1
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

print("Top 5 most common words:\n")
for word, count in sorted_words[:5]:
    print(word, ":", count)

    

