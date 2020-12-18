import mechanize
import random
import time
from http.cookiejar import LWPCookieJar

"""This is an extensio of the Mechanize Browser class to allow for the
dealing with User Agents and Cookies"""

USERAGENT =[('User-agent','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0')]

class anonBrowser(mechanize.Browser):

    def __init__(self, proxies=[], user_agents=[]):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies = proxies
        self.user_agents = USERAGENT

        self.cookie_jar = LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
        self.anonymize()

    def clear_cookies(self):
        self.cookie_jar = LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)

    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies({'http': self.proxies[index]})

    def anonymize(self, sleep=False):
        self.clear_cookies()
        self.change_proxy()

        if sleep:
            time.sleep(60)