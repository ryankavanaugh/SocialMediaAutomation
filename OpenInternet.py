import webbrowser

url = "https://www.facebook.com/"

#webbrowser.open_new(url)

import re, os, sys

class Facebook():
    def __init__(self, email, password):
        self.email = email
        self.password = password

        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
                            ('Content-Type', 'application/x-www-form-urlencoded'),
                            ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]
        self.opener = opener

    def login(self):
        url = 'https://login.facebook.com/login.php?login_attempt=1'
        data = "locale=en_US&non_com_login=&email="+self.email+"&pass="+self.password+"&lsd=20TOl"

        usock = self.opener.open('http://www.facebook.com')
        usock = self.opener.open(url, data)
        if "Logout" in usock.read():
            print("Logged in.")
        else:
            print("failed login")
            print (usock.read())
            sys.exit()

f = Facebook("rjkavanaugh@gmail.com", "Hulk1234")
f.login()
