
from bs4 import BeautifulSoup
import requests


url = 'https://minfin.com.ua/ua/currency/usd/'


response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
print('{}\n\n'.format(soup.title.text))  # [$] Курс долара до гривні на 07.07.2020 в Україні ᐈ Мінфін
main = soup.main

# get active currency
div = main.findAll(class_='mfz-container')
active_mfm_tab_menu = div[1].find(class_='active')
print(active_mfm_tab_menu.text)
print('\n**************************\n')

# get active currency value
div_mfm_grey_bg = div[1].find(class_='mfm-grey-bg')
div_mfm_grey_bg_tbody = div_mfm_grey_bg.find('tbody')
# print(div_mfm_grey_bg)
# print('\n**************************\n')

print(div_mfm_grey_bg_tbody)
print('\n**************************\n')
print(div_mfm_grey_bg_tbody.findAll('span', class_='mfm-posr'))
print(len(div_mfm_grey_bg_tbody.findAll('span', class_='mfm-posr')))

# print(div)
# sub_div_1 = div.find(attrs={'class': 'mfz-container'})
# print(sub_div_1)




