
from bs4 import BeautifulSoup
import requests
import datetime


usd_currency = 'https://minfin.com.ua/ua/currency/usd/'
usd_retail_json = 'https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json'
usd_auction_json = 'https://minfin.com.ua/ua/data/currency/auction/usd.1000.median.daily.format.json'
usd_nbu_json = 'https://minfin.com.ua/data/currency/nbu/nbu.usd.stock.json?1594214142'


usd_retail_data = requests.get('https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json').json()
print(usd_retail_data)
print(usd_retail_data[1]['date'])
print('{}\n'.format('*'*50))
print(datetime.datetime.strptime(usd_retail_data[1]['date'], '%Y-%m-%d'))

usd_nbu_data = requests.get(usd_nbu_json).json()
print(usd_nbu_data)


def request_to_minfin(url=None):
    response = requests.get(url=url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html


def get_usd_currency(soup):

    # [$] Курс долара до гривні на 07.07.2020 в Україні ᐈ Мінфін
    print('\n{}'.format(soup.title.text))
    print('{}\n'.format('*'*50))
    main = soup.main

    # get active currency  ДОЛАР
    div = main.findAll(class_='mfz-container')
    active_mfm_tab_menu = div[1].find(class_='active')
    print(active_mfm_tab_menu.text)
    print('{}\n'.format('*'*50))

    # get active currency value
    div_mfm_grey_bg = div[1].find(class_='mfm-grey-bg')
    div_mfm_grey_bg_tbody = div_mfm_grey_bg.find('tbody')

    # print(div_mfm_grey_bg_tbody.findAll('span', class_='mfm-posr'))
    # print(len(div_mfm_grey_bg_tbody.findAll('span', class_='mfm-posr')))

    tds = div_mfm_grey_bg_tbody.findAll('tr')[0].findAll('td')
    print(tds[0].get('data-title'))
    print(tds[0].text)
    print('{}\n'.format('*'*50))
    print(tds[1].get('data-title'))
    print(tds[1].text)
    print('{}\n'.format('*'*50))
    print(tds[2].get('data-title'))
    print(tds[2].text)
    print('{}\n'.format('*'*50))
    print(tds[3].get('data-title'))
    print(tds[3].text)
    print('{}\n'.format('*'*50))
    print('{}\n'.format('*'*50))

    tds = div_mfm_grey_bg_tbody.findAll('tr')[1].findAll('td')
    print(tds[0].get('data-title'))
    print(tds[0].text)
    print('{}\n'.format('*'*50))
    print(tds[1].get('data-title'))
    print(tds[1].text)
    print('{}\n'.format('*'*50))
    print(tds[2].get('data-title'))
    print(tds[2].text)
    print('{}\n'.format('*'*50))
    print(tds[3].get('data-title'))
    print(tds[3].text)
    print('{}\n'.format('*'*50))
    print('{}\n'.format('*'*50))

    tds = div_mfm_grey_bg_tbody.findAll('tr')[2].findAll('td')
    print(tds[0].get('data-title'))
    print(tds[0].text)
    print('{}\n'.format('*'*50))
    print(tds[1].get('data-title'))
    print(tds[1].text)
    print('{}\n'.format('*'*50))
    print(tds[2].get('data-title'))
    print(tds[2].text)
    print('{}\n'.format('*'*50))
    print('{}\n'.format('*'*50))


if __name__ == '__main__':
    soup = request_to_minfin(url=usd_currency)
    get_usd_currency(soup=soup)
