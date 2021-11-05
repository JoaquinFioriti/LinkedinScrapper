from EmailScrapper import EmailScrapper
from ImageScrapper import ImageScrapper
from Login import Login
from NameScrapper import NameScrapper
from ProfileScrapper import ProfileScrapper

start = Login("", "")
driver = start.go()
scraping = ProfileScrapper([NameScrapper(), EmailScrapper(), ImageScrapper()], driver,
                           "https://www.linkedin.com/in/mariano-garcia-9745a920b/")
scraping.scrape()
driver.quit()
