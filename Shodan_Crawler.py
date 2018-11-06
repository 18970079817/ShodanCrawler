import requests, sys
from bs4 import BeautifulSoup

def check_ip_range(iprange):
    def check_ip(ipaddr):
        try:
            addr = ipaddr.strip().split('.')
        except:
            print "Wrong IP format."
            sys.exit()
        if len(addr) != 4: 
            print "IP address is less than 4 parts."
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
        first_ip = iprange.split('-')[0]
    except:
        print "First IP wrong IP format."
        sys.exit()
    try:
        second_ip = iprange.split('-')[1]
    except:
        print "Second IP wrong IP format."
        sys.exit()
    check_ip(first_ip)
    check_ip(second_ip)
    if int(second_ip.split('.')[3]) <= int(first_ip.split('.')[3]):
        if int(second_ip.split('.')[2]) <= int(first_ip.split('.')[2]):
            if int(second_ip.split('.')[1]) <= int(first_ip.split('.')[1]):
                if int(second_ip.split('.')[0]) <= int(first_ip.split('.')[0]):
                    print "Second IP is small than first IP."
                    sys.exit()

def get_ip(ipaddr):
    a = ipaddr.split('.')
    return a

iprange = raw_input('Please input the ip range,\nsuch as xxx.xxx.xxx.xxx-xxx.xxx.xxx.xxx:')
check_ip_range(iprange)
first_ip = iprange.split('-')[0]
second_ip = iprange.split('-')[1]

r = requests.get('https://www.shodan.io/host/' + first_ip)
#print r
#print r.text
soup = BeautifulSoup(r.text, 'lxml')
for tbody in soup.find_all('tbody'):
    for tr in soup.find_all('tr'):
        print tr.find('td').string
        print tr.find('th').string
        

