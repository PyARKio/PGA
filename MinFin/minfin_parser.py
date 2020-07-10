# -- coding: utf-8 --
from __future__ import unicode_literals
from utilits.log_settings import log
import configs
from bs4 import BeautifulSoup
import requests
import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


usd_retail_data = requests.get('https://minfin.com.ua/ua/data/currency/retail/usd.rates.full.json').json()
log.info(usd_retail_data)
log.info(usd_retail_data[1]['date'])
log.info('{}\n'.format('*'*50))
log.info(datetime.datetime.strptime(usd_retail_data[1]['date'], '%Y-%m-%d'))

usd_nbu_data = requests.get(configs.usd_nbu_json).json()
log.info(usd_nbu_data)


def request_to_minfin(url=None):
    response = requests.get(url=url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html


def get_usd_currency(soup):

    # [$] Курс долара до гривні на 07.07.2020 в Україні ᐈ Мінфін
    try:
        log.info('\n{}'.format(soup.title.text))
    except Exception as err:
        log.error(err)

    log.info('{}\n'.format('*'*50))
    main = soup.main

    # get active currency  ДОЛАР
    div = main.findAll(class_='mfz-container')
    active_mfm_tab_menu = div[1].find(class_='active')
    log.info(active_mfm_tab_menu.text)
    log.info('{}\n'.format('*'*50))

    # get active currency value
    div_mfm_grey_bg = div[1].find(class_='mfm-grey-bg')
    div_mfm_grey_bg_tbody = div_mfm_grey_bg.find('tbody')

    # print(div_mfm_grey_bg_tbody.findAll('span', class_='mfm-posr'))
    # print(len(div_mfm_grey_bg_tbody.findAll('span', class_='mfm-posr')))

    tds = div_mfm_grey_bg_tbody.findAll('tr')[0].findAll('td')
    log.info(tds[0].get('data-title'))
    log.info(tds[0].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[1].get('data-title'))
    log.info(tds[1].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[2].get('data-title'))
    log.info(tds[2].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[3].get('data-title'))
    log.info(tds[3].text)
    log.info('{}\n'.format('*'*50))
    log.info('{}\n'.format('*'*50))

    tds = div_mfm_grey_bg_tbody.findAll('tr')[1].findAll('td')
    log.info(tds[0].get('data-title'))
    log.info(tds[0].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[1].get('data-title'))
    log.info(tds[1].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[2].get('data-title'))
    log.info(tds[2].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[3].get('data-title'))
    log.info(tds[3].text)
    log.info('{}\n'.format('*'*50))
    log.info('{}\n'.format('*'*50))

    tds = div_mfm_grey_bg_tbody.findAll('tr')[2].findAll('td')
    log.info(tds[0].get('data-title'))
    log.info(tds[0].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[1].get('data-title'))
    log.info(tds[1].text)
    log.info('{}\n'.format('*'*50))
    log.info(tds[2].get('data-title'))
    log.info(tds[2].text)
    log.info('{}\n'.format('*'*50))
    log.info('{}\n'.format('*'*50))


if __name__ == '__main__':
    soup = request_to_minfin(url=configs.usd_currency)
    get_usd_currency(soup=soup)
