from requests_html import HTMLSession

urlList = ['https://www.amazon.com/Moto-Unlocked-Motorola-Camera-XT2052-1/dp/B086H3HH5V/ref=sr_1_2?dchild=1&keywords=cell+phone&qid=1613092354&sr=8-2',
           'https://www.amazon.com/Tracfone-Samsung-Galaxy-Prepaid-Smartphone/dp/B088NKZT13/ref=sr_1_3?dchild=1&keywords=cell+phone&qid=1613092354&sr=8-3',
           'https://www.amazon.com/Stylus-Battery-Unlocked-Motorola-Camera/dp/B08NWF8SL4/ref=sr_1_4?dchild=1&keywords=cell+phone&qid=1613092354&sr=8-4']

# Price Function
def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render()

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text


    }

    print(product)
    return product


phonePrices = []

for url in urlList:
    phonePrices.append(getPrice(url))

print(len(phonePrices))