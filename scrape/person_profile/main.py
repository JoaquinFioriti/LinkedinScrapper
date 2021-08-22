from LinkedinScrapper.scrape.person_profile.EmailScrapper import EmailScrapper
from LinkedinScrapper.scrape.person_profile.ImageScrapper import ImageScrapper
from LinkedinScrapper.scrape.person_profile.Login import Login
from LinkedinScrapper.scrape.person_profile.NameScrapper import NameScrapper
from LinkedinScrapper.scrape.person_profile.ProfileScrapper import ProfileScrapper

start = Login("joaquinfioriti9@gmail.com", "paquigold213")
driver = start.go()
scraping = ProfileScrapper([NameScrapper(), EmailScrapper(), ImageScrapper()], driver,
                           "https://www.linkedin.com/in/mariano-garcia-9745a920b/")
scraping.scrape()
driver.quit()
