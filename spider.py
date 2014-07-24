import urllib2 
import urllib 
   
class  get_mm_pic(object): 
    def __init__(self,page_num): 
        self.page_num = page_num 
        self.mmurl= "http://mm.taobao.com/json/request_top_list.htm?type=0&page="#这个是我们要抓取的网站的url，page = 数字。。 
    def  get_pic(self):         
        i = 0 
        page_num = self.page_num 
        temp  ='''<img src="'''
        while i<page_num: 
            url = self.mmurl + str(i) #某页的全部url 
            up =  urllib2.urlopen(url) #获取页面内容 
            cont = up.read() 
  
            ahref = "<a href"
            target = "target"
            pa = cont.find(ahref) 
            pt = cont.find(target, pa)#找到匹配字符串的前后位置，获取由网页提供的美女模特的个人主页之类的页面地址。可通过审查元素获取格式。并设定匹配规则。 
  
            modelurl = cont[pa+len(ahref) +2: pt-2]#切割匹配成功的字符串 
            mup=  urllib2.urlopen(modelurl) 
            mcont = mup.read()  #读取美女主页的全部内容，和第一次读取页面其实一样 
  
            header = "<img style"#通过审查元素获得特征，并选择字符串匹配。 
            tail = ".jpg"
            iph = j = 0
            while iph != -1:   #循环读取，找到所有图片 
                iph = mcont.find(header) 
                ipj  =  mcont.find(tail,  iph)         
                mpic = mcont[iph : ipj + len(tail)] 
                ips = mpic.find("src") 
                urlpic =  mpic[ips +len("src ="): ]#同样的，我们找到了图片的地址。可以在浏览器中查看是否正确 
                urllib.urlretrieve(urlpic, "lady"+str(i*10+j)+".jpg")#下载图片到程序保存目录，若改变目录，可加路径 
                print ">>>downloading : lady"+str(i*10+j)+".jpg......"
  
                mcont = mcont[ipj+1:]#移动字符串其实位置，进入下一个匹配循环 
                j+=1
            i += 1
        print ">>>download completed"    
def main(page_num): 
    get_mm_pictures = get_mm_pic(page_num) 
    get_mm_pictures.get_pic() 
  
if __name__ == '__main__': 
    main(2)#这个数字可以自己写咯。当然写成输入的形式会更好。