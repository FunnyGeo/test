from playwright.sync_api import sync_playwright

url = 'https://dom.ria.com/uk/search?category=1&realty_type=2&operation=3&state_id=10&city_id=10&with_newbuilds=0&price_cur=1&wo_dupl=0&inspected=0&sort=inspected_sort&period=0&notFirstFloor=0&notLastFloor=0&firstIteraction=false&type=list&limit=20&page=0&client=searchV2&ch=246_244'

with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.new_page()

    ads = []
    def log_response(intercepted_response):
        if 'searchEngine/v2/view' in intercepted_response.url:
            js = intercepted_response.json()
            ads.append(js)
            print('matching: {}'.format(intercepted_response.url))
        else:
            print('not matching: {}'.format(intercepted_response.url))


    page.on('requestfinished', log_response)
    page.goto(url)

    browser.close()




