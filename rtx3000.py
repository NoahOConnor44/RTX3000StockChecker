from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from datetime import datetime
import time
import webbrowser
from playsound import playsound

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}

item_urls = ['https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
'https://www.bestbuy.com/site/msi-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175',
'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6432400.p?skuId=6432400',
'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6432399.p?skuId=6432399',
'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436194.p?skuId=6436194',
'https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3885-kr/p/N82E16814487520?Description=RTX%203080&cm_re=RTX_3080-_-14-487-520-_-Product&quicklink=true',
'https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?Description=RTX%203080&cm_re=RTX_3080-_-14-137-598-_-Product',
'https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?Description=RTX%203080&cm_re=RTX_3080-_-14-137-597-_-Product',
'https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description=RTX%203080&cm_re=RTX_3080-_-14-126-452-_-Product',
'https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?Description=RTX%203080&cm_re=RTX_3080-_-14-126-453-_-Product',
'https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521?Description=RTX%203080&cm_re=RTX_3080-_-14-487-521-_-Product',
'https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522?Description=RTX%203080&cm_re=RTX_3080-_-14-487-522-_-Product',
'https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?Description=RTX%203080&cm_re=RTX_3080-_-14-137-600-_-Product']

def whereFrom(item):
    fromBestBuy = True
    if item[12:13] == 'n':
        fromBestBuy = False
    else:
        fromBestBuy = True
    return fromBestBuy

while True:
    for item in item_urls:    
        if whereFrom(item) == False:
            req = Request(item, headers=header)
            page = urlopen(req).read()
            page_soup = soup(page,"html.parser")
            status = page_soup.find('span', 'btn-message')
            if(status == None):
                playsound('C:/Users/Noah/ilovertx3000/ding.wav')
                webbrowser.get().open(item, new=2)
                print('In stock')
            time.sleep(0.5)
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print('--> ---------------------------------------------------------------------- <--' + str(current_time))
        else:
            '''
            req = Request(item, headers=header)
            page = urlopen(req).read()
            page_soup = soup(page,"html.parser")
            status = page_soup.find('button', 'btn')
            print(status)
            time.sleep(0.5)
            print('--> ---------------------------------------------------------------------- <--')
            '''
    time.sleep(180)