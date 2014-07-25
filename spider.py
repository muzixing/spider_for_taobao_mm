import urllib2
import urllib
import sys

class  get_mm_pic(object): 
    def __init__(self,page_num): 
        self.page_num = page_num 
        self.mmurl= "http://mm.taobao.com/json/request_top_list.htm?type=0&page="
    def  get_pic(self):      
        i = 1
        page_num = self.page_num 
        temp  ='''<img src="'''
        while i<page_num: 
            url = self.mmurl + str(i) 
            up =  urllib2.urlopen(url) 
            cont = up.read() 
            pa = j = 0 
            while True: 
                ahref = '''<a href="http'''
                target = "target"
                pa = cont.find(ahref)
                pt = cont.find(target, pa) 
                if pa == -1:
                    break
                modelurl = cont[pa+len(ahref)-4: pt-2] 
                mup=  urllib2.urlopen(modelurl) 
                mcont = mup.read() 
   
                header = "<img style"
                tail = ".jpg"
                iph = k = 0
                while True: 
                    iph = mcont.find(header) 
                    ipj  =  mcont.find(tail,  iph) 
                    if iph == -1:
                        break       
                    mpic = mcont[iph : ipj + len(tail)] 
                    ips = mpic.find("src") 
                    urlpic =  mpic[ips +len("src ="):]
                    try: 
                        print ">>>downloading : lady_p"+str(i)+"_no_"+str(j)+"_pic_"+str(k)+".jpg......"
                        urllib.urlretrieve(urlpic,  "lady_p"+str(i)+"_no_"+str(j)+"_pic_"+str(k)+".jpg") 
                    except KeyboardInterrupt: 
                        print "SIGINT, exit..."
                        sys.exit(0) 
                    except: 
                        pass
                    mcont = mcont[ipj+1:]
                    k+=1
                cont = cont[pt+1:]
                j+=1
            i += 1
        print ">>>download completed"
def main(page_num): 
    get_mm_pictures = get_mm_pic(page_num) 
    print "@Author:www.muzixing.com"
    get_mm_pictures.get_pic() 

if __name__ == '__main__': 
    main(int(sys.argv[1]))
