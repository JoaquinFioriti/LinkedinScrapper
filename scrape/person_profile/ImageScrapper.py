from Scrapper import Scrapper


class ImageScrapper(Scrapper):

    def scrape(self, driver, url):
        field = "image-url: "
        return field + driver.find_element_by_css_selector("img.pv-top-card-profile-picture__image").get_attribute(
            "src")
