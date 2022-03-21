import requests
import pastebin
import banner
import mail

banner.banner()

inputMSG = """
>> 1. Use Pastebin URL
>> 2. Use Text File
"""

print(inputMSG,"\n")
inputd = input(">> Choose Input Method : ")

text = open("checked_hosts.txt","a")
email = input("Enter Your Email : ")
if inputd == "1":
    urls = input("Enter Pastebin URL: ")
    hosts = pastebin.scrape(urls)
elif inputd == "2":
    with open('hosts.txt', 'r') as f:
        hosts = [line.strip() for line in f]

for url in hosts:
    try:
        data = requests.get(url,verify=True,timeout=2)
        response = str(data)
    
    except:
        response = None

#print(response)

    if response == "<Response [200]>":
        print("Host Working {0}".format(banner.tick))
        text.write(url+"\n")
    elif response == "<Response [301]>":
        print("Host Moved Permanently {0}".format(banner.move))
        text.write(url+" --Response 301"+"\n")
    else:
        print("Host Not Working {0}".format(banner.cross))
text.write("\n")
mail.sendmail(email=email)
print("Valid Hosts sent via an Email")