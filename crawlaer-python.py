# coding:utf-8

import urllib2
import urllib
import re
import time
import Thread

class Qsbk:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/63.0"
        self.headers = {"User-Agent":self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = "http://www.qiushibaike.com/hot/page/"+str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            reponse = urllib2.urlopen(request)
            pageCode = reponse.read().decode("utf-8")
            return pageCode
        except urllib2.URLError , e:
            if hasattr(e,"reason"):
                print u"connect fail"+e.reason
                return None


    def getPageItem(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "loadPage failed"
            return None
        pattern = re.compile('<a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?' + '<div class="content".*?>.*?<span>(.*?)</span>.*?</div>.*?'
            + '<i class="number".*?>(.*?)</i>.*?' + '<i class="number".*?>(.*?)</i>', re.S)
        items = re.findall(pattern , pageCode)
        pageStories = []
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[1])
            pageStories.append(item[0].strip(),text,item[2].strip(),item[3],strip())
        return pageStories

    def loadStories(self):
        if self.enable:
            if len(self.stories)<2:
                stories = self.getPageItem(self.pageIndex)
                if stories:
                    self.pageIndex +=1
                    self.stories.append(stories)