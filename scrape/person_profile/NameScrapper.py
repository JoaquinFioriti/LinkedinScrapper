from LinkedinScrapper.scrape.person_profile.Scrapper import Scrapper


# A good idea is that every scrapper add in a dictionary the name that will be in the columns
class NameScrapper(Scrapper):

    def scrape(self, driver, url):
        field = "Name: "
        return field + driver.find_element_by_css_selector("h1.text-heading-xlarge").text
