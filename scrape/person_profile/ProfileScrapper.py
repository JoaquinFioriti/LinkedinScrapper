class ProfileScrapper:

    def __init__(self, fields, driver, url):
        self.driver = driver
        self.url = url
        self.fields = fields
        self.driver.get(self.url)
        driver.implicitly_wait(2)

    def scrape(self):
        for field in self.fields:
            print(field.scrape(self.driver, self.url))
