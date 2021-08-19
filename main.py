from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import geopy.distance
driver = webdriver.Firefox()
driver.get("https://www.google.com/maps")
#assert "Python" in driver.title
#time.sleep(7)
elem = driver.find_element_by_id("searchboxinput")
elem.clear()
elem.send_keys("36.80076861493657"+", "+ "-119.7866723580912") #SJVAPCD
elem.send_keys(Keys.RETURN)
time.sleep(5)
url = driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content')
lat = str(url.split('?center=')[1].split('&zoom=')[0].split('%2C')[0])
long = str(url.split('?center=')[1].split('&zoom=')[0].split('%2C')[1])
coords1 = (lat,long)
coords2 = ("36.80101771350111", "-119.79094247899053") #DON Pepe
print(lat+"," +long )

print(geopy.distance.geodesic(coords1,coords2, ellipsoid='GRS-80').miles)
#assert "No results found." not in driver.page_source
#driver.close()