import smtplib

To = input("Enter EMail of the Recipent : ")

Message = input("type your Message :- ")

def sendEmail(To,Message):
   try: 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('your gmail','your app password')#app password will be in your gmail settings,just search app password and set an app name u will get app password!
    server.sendmail('your gmail',To,Message)
    server.close()
    print("Email sent!")

   except smtplib.SMTPException as e:
     print(f"FAILED!!:{e}") 

    
sendEmail(To,Message)
