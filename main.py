import requests
from bs4 import BeautifulSoup
from bot import sendMes

def getPage(last_title):
	print('started func')
	header = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control': 'max-age=0',
			'cookie': '__cfduid=d2edca66088333df32aea1665409d5da41528542917; session_id=603878690a3946922378fc44461d96ef; device_view=full; visitor_id=77.51.12.186.1528542917713974; qt_visitor_id=77.51.12.186.1528542917713974; XSRF-TOKEN=3aa5c92147be7da5b76e258240543d9a; _ga=GA1.2.1072296475.1528542922; _gid=GA1.2.889408001.1528542922; _gat_UA-62227314-1=1; _br_uid_2=uid%3D592428079705%3Av%3D11.8%3Ats%3D1528542921595%3Ahc%3D1; _pxvid=663fc9f0-6bd6-11e8-bea8-79d104517d7e; _px3=b77cba00d95981411ec3cff3351e48cde0e436bc48fd53bc8200d1d45adff4cd:soUAMqg1oOsyqSG/YJiJFv6FiJWzJIiQnfFu32s+5zdfGuvZodoe0nAy5ZSUp8cEv6/2Gw4ULCCyI2/wJdFbOw==:1000:2VG38u7+pPlUXOjsozwzvb8XoVzozR+2FwQuqQauWEYdxuJ+9VykAcyIk5vOvWrl3CXSUuC/qAaadpLc33wg4GJ6hEw/oNZK1cq1wchBxd/jsp1Mfyui1TwDO/JEyF3qoiI23W0vB+K2enSA4PA76whKM5KxViC5pIWL56yg45s=; sc.ASP.NET_SESSIONID=h3evde1gwtfaym3m0do0ytqs',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'
	}

	url = 'https://www.upwork.com/o/jobs/browse/c/design-creative/sc/illustration/?sort=create_time%2Bdesc'
	url2 = 'https://www.upwork.com/o/jobs/browse/?sort=create_time%2Bdesc'


	title = ''
	description = ''
	href = ''

	htmlContent = requests.get(url2, headers=header)

	soup = BeautifulSoup(htmlContent.text, 'html.parser')

	description = soup.findAll("div", {"class":"d-none d-xl-block"})[0]
	title = soup.findAll("a", {"class": "job-title-link break visited"})[0]
	href = title['href']

	if(title != last_title):
		sendMes(title +'\n' + description +'\n' + href)

	last_title = title.text.strip()
	last_description = description.text.strip()
	last_href = href
	
	return title;

