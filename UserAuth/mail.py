import smtplib
# s = smtplib.SMTP('smtp.gmail.com', 587)
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("atul.rana2707@gmail.com", "Ra19883")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("atul.rana2707@gmail.com", "hoyoyax358@aregods.com", message)
print("sent")
  
# terminating the session
s.quit()