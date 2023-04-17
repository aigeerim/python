


from bs4 import BeautifulSoup
import requests
import csv

cookies = {
    'PHPSESSID': 'erltj9e49nkit0kef0ubiaj966',
    '_csrf': '0ebe79fe63fcfc25a9de1293c741d8bfd1c524dd7b2ef2379ba45c0875d144d9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22q7BI47c65T9Tf9BLWrjE_sF8wRiG0mWF%22%3B%7D',
    '_gcl_au': '1.1.349184840.1681703188',
    'astratop': '1',
    '_gid': 'GA1.2.2076104035.1681703188',
    '_ym_uid': '1681703188975943999',
    '_ym_d': '1681703188',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '_gat_UA-27923957-1': '1',
    '_gcl_aw': 'GCL.1681703471.eaiaiqobchmi3pogx4cw_givb0krbr0wdwexeaayasaaegl2avd_bwe',
    '_ga_JWPW0MM28G': 'GS1.1.1681703188.1.1.1681703471.28.0.0',
    '_ga': 'GA1.2.233586299.1681703188',
    '_gac_UA-27923957-1': '1.1681703471.eaiaiqobchmi3pogx4cw_givb0krbr0wdwexeaayasaaegl2avd_bwe',
}

headers = {
    'authority': 'www.kivano.kg',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    # 'cookie': 'PHPSESSID=erltj9e49nkit0kef0ubiaj966; _csrf=0ebe79fe63fcfc25a9de1293c741d8bfd1c524dd7b2ef2379ba45c0875d144d9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22q7BI47c65T9Tf9BLWrjE_sF8wRiG0mWF%22%3B%7D; _gcl_au=1.1.349184840.1681703188; astratop=1; _gid=GA1.2.2076104035.1681703188; _ym_uid=1681703188975943999; _ym_d=1681703188; _ym_isad=2; _ym_visorc=w; _gat_UA-27923957-1=1; _gcl_aw=GCL.1681703471.eaiaiqobchmi3pogx4cw_givb0krbr0wdwexeaayasaaegl2avd_bwe; _ga_JWPW0MM28G=GS1.1.1681703188.1.1.1681703471.28.0.0; _ga=GA1.2.233586299.1681703188; _gac_UA-27923957-1=1.1681703471.eaiaiqobchmi3pogx4cw_givb0krbr0wdwexeaayasaaegl2avd_bwe',
    'referer': 'https://www.kivano.kg/?psafe_param=1&gclid=eaiaiqobchmi3pogx4cw_givb0krbr0wdwexeaayasaaegl2avd_bwe',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

response = requests.get('https://www.kivano.kg/noutbuki', cookies=cookies, headers=headers)




soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)


list_view = soup.find_all('div', class_="list-view")
# print(list_view)


new_list = []
for item in list_view:
    new_list.append({
        "title":item.find('div', class_='listbox_title').find('a').text,
        "description":item.find('div',class_="product_text").text,
        "price":item.find('div', class_="listbox_price").find('strong').text,
    })

print(new_list)

