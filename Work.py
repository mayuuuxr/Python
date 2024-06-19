import webbrowser as web
import os 

def WorkAuto():
 Code = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
 os.startfile(Code)
 Chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
 URLS=('https://www.udemy.com/course/python-in-action-a-practical-course-50-real-world-projects/','https://chatgpt.com/','https://www.youtube.com/')

 for url in URLS:
    web.get(Chrome_path).open(url)

WorkAuto()