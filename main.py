from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from math import sin, cos, sqrt, atan2, radians
import time
import geopy.distance
import pypyodbc


db_host = 'localhost'
db_name = 'database'
db_user = 'username'
db_password = 'password'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'

#conn = pypyodbc.connect("DRIVER={SQL Server};"
#                    "SERVER=DESKTOP-G615CF2;"
#                    "DATABASE=UserAccounts;"
#                    "UID=PracticeGuest;"
#                    "PWD=123456;") #dummy

#cursor = conn.cursor()
#cursor.execute('SELECT * FROM [table]')

#for row in cursor:
    #print('row = %r' % (row,))
drives = [webdriver.Firefox() for x in range(0,2)]
print(drives[0])
print(drives[1])


#drive = webdriver.Firefox()
#driver1 = webdriver.Firefox()
drives[0].get("https://www.google.com/maps")
drives[1].get("https://www.google.com/maps")
#assert "Python" in driver.title
#time.sleep(7)
elem = drives[0].find_element_by_id("searchboxinput")
elem.clear()
elem.send_keys("36.80076861493657"+", "+ "-119.7866723580912") #SJVAPCD
elem.send_keys(Keys.RETURN)
time.sleep(5)
url = driver.find_element_by_css_selector('meta[itemprop=image]').get_attribute('content')
lat = radians(float(url.split('?center=')[1].split('&zoom=')[0].split('%2C')[0]))
long = radians(float(url.split('?center=')[1].split('&zoom=')[0].split('%2C')[1]))
coords1 = (lat,long)
coords2 = (radians(36.80101771350111), radians(-119.79094247899053)) #DON Pepe
#print(lat+"," +long )

print(geopy.distance.geodesic(coords1,coords2, ellipsoid='GRS-80').miles)
#assert "No results found." not in driver.page_source
#driver.close()

#trigonometry
