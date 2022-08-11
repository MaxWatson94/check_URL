import requests
from headers import headers
import time

def getLink(file):
    # Open file with sites and readlines
    with open(file) as file:
        url = [row.strip() for row in file]
    # After run funtions where wee try to check sites
    checkUrl(url=url)

def checkUrl(url):
    print('==== NEW REPORT ====')
    for check in url:
        try:
            # send requsts to site
            r = requests.get(check, headers=headers)
            # check response code from the site
            if r.status_code == 200:
                print(str(check) + '- is Good!')
            else:
                print(str(check) + '- bad response!!!')
        except:
            print(str(check) + '- Invalid URL or bad response!!!')

    print('==== END REPORT ====\n\n')
def main():
    getLink(file='sites.txt')

if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)