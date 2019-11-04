from xml.dom import minidom
from urllib.request import urlopen
from time import sleep
from itertools import cycle
#import curses

url1 = "http://luasforecasts.rpa.ie/xml/get.ashx?action=forecast&stop=bla&encrypt=false"
#url2 = "http://api.openweathermap.org/data/2.5/weather?q=Dublin,ie&APPID=17fd8116fd28f1de0578f7e64117d95a&mode=xml&units=metric"

def printDueMins(trams):
    total = []
    for tram in trams:
        total.append(str(tram.attributes['destination'].value +" "+tram.attributes['dueMins'].value))
    return total


def pbar():
    dom = minidom.parse(urlopen(url1)) # parse the data
    inbound = dom.getElementsByTagName('direction')[0].getElementsByTagName('tram')
    outbound= dom.getElementsByTagName('direction')[1].getElementsByTagName('tram')
    return (inbound,outbound)

duration = 0
for frame in cycle(r'-\|/-\|/'):
    inbound,outbound =pbar()
    in_b = printDueMins(inbound)
    out_b = printDueMins(outbound)
    print('\r', frame,'INBOUND',frame, sep='', end='\t', flush=True)
    for count in range(len(in_b)-1):
        print(in_b[count],sep=' ', end='\t', flush=True)
    sleep(0.2)
    if duration >= 20:
        break
    else:
        duration += 1


