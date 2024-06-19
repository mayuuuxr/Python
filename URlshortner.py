import pyshorteners

url = input("enter your URl :- ")

print("URL After Shortening :- ",pyshorteners.Shortener().tinyurl.short(url))