import string


n=input("enter a sentence: ")
result=n.split()
frequency={}
for words in result:
    words=words.lower()
    words=words.strip(string.punctuation)
    if words in frequency:
        frequency[words]+=1
    else:
        frequency[words]=1

print(frequency)