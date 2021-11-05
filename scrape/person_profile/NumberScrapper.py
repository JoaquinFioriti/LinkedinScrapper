from Scrapper import Scrapper


class NumberScrapper(Scrapper):

    def scrape(self, driver, url):
        details = driver.find_element_by_css_selector("section.pv-profile-section").find_element_by_css_selector(
            "div.pv-profile-section__section-info").find_elements_by_tag_name("section")
