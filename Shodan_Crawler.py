#coding=utf-8
import requests, sys, codecs
from bs4 import BeautifulSoup

def check_ip_range(iprange):
    def check_ip(ipaddr):
        try:
            addr = ipaddr.strip().split('.')
        except:
            print "Wrong IP format."
            sys.exit()
        if len(addr) != 4: 
            print "IP address is ilegal."
            sys.exit()
        for i in range(4):
            try:
                addr[i]=int(addr[i])
            except:
                print "IP address has ilegal numbers."
                sys.exit()
            if addr[i]<=255 and addr[i]>=0:
                pass
            else:
                print "IP address out of range."
                sys.exit()
    try:
        start_ip = iprange.split('-')[0]
    except:
        print "First IP wrong IP format."
        sys.exit()
    try:
        end_ip = iprange.split('-')[1]
    except:
        print "Second IP wrong IP format."
        sys.exit()
    check_ip(start_ip)
    check_ip(end_ip)
    if int(end_ip.split('.')[3]) <= int(start_ip.split('.')[3]):
        if int(end_ip.split('.')[2]) <= int(start_ip.split('.')[2]):
            if int(end_ip.split('.')[1]) <= int(start_ip.split('.')[1]):
                if int(end_ip.split('.')[0]) <= int(start_ip.split('.')[0]):
                    print "Second IP is small than first IP."
                    sys.exit()

def get_ip(ipaddr):
    a = ipaddr.split('.')
    return a

iprange = raw_input('Please input the ip range,\nsuch as 8.8.8.8-8.8.8.9:\n\t')
check_ip_range(iprange)
start_ip = iprange.split('-')[0]
end_ip = iprange.split('-')[1]

int_ip = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])
ip_int = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

for i in range(ip_int(start_ip), ip_int(end_ip)+1):
    try:
        r = requests.get('https://www.shodan.io/host/' + int_ip(i))
    except:
        print 'Some errors happened, check your network or something else.'
    else:
        with codecs.open('result.txt', 'a', 'utf-8') as f:
            soup = BeautifulSoup(r.text, 'lxml')
            td = []
            th = []
            a = []
            for tbody in soup.find_all('tbody'):
                for tr in soup.find_all('tr'):
                    td.append(tr.find('td').string)
                    th.append(tr.find('th').string)
            for ul in soup.find_all('ul', class_ = 'ports'):
                for li in ul.find_all('li'):
                    a.append(li.find('a').string)
            f.write('\n' + 'IP' + '\t')
            for j in range(len(td)):
                f.write(td[j] + '\t')
            for j in range(len(a)):
                f.write('Port' + '\t')
            f.write('\n' + str(int_ip(i)) + '\t')
            for j in range(len(th)):
                f.write(th[j] + '\t')
            for j in range(len(a)):
                f.write(a[j] + '\t')
