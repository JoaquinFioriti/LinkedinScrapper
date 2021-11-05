from Scrapper import Scrapper


class EmailScrapper(Scrapper):
    contactInformationUrl = "detail/contact-info/"

    def scrape(self, driver, url):
        driver.get(url + self.contactInformationUrl)

        fields = driver.find_element_by_css_selector("div.artdeco-modal--layer-default").find_element_by_css_selector(
            "div.pv-profile-section__section-info").find_elements_by_css_selector(
            "section.pv-contact-info__contact-type")

        for field in fields:
            text = field.find_element_by_tag_name("h3").text
            if text == "Email":
                return "Email: " + field.find_element_by_tag_name("a").get_attribute("href").split(":")[1]
        return None
