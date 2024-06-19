import wikipedia

query = input("enter the topic name : ")

result = wikipedia.summary(query)

print(result)