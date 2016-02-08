
from datetime import datetime
from requests import get as rget

NODESJSON = 'https://ffmuc.net/data/nodelist.json'

def scrape(url):
    '''returns remote json'''
    try:
        return rget(url).json()
    except Exception as ex:
        print('Error: %s' %(ex))

if __name__ == '__main__':
    nodes = scrape(NODESJSON)

    if nodes:
        online = 0
        nonclient = 0

        for node in nodes['nodes']:
            if node['status']['online']:
                online += 1
                if not node['status']['clients']:
                    nonclient += 1

        now = datetime.now().strftime('%H:%M %d.%m.%Y')
        resultmsg = 'Status: online: %d (%d Router, %d Teilnehmer) %s' %(online, nonclient, online-nonclient, now)

        print(resultmsg)

