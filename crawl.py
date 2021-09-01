from typing import final
import pypyodbc
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.common.exceptions import NoSuchElementException
import time
class PersistCrawl():
    def __init__(self) -> None:
        #self.jobSize = 100000
        self.ins = 4
        self.browsers = [webdriver.Firefox() for i in range(0,self.ins)]

    def send_jobs(self) -> None:
        """Getting each thread to begin"""
        #idxRange = self.split(self.jobSize,self.ins)
        for i in self.ins:
            self.run_job("test Address")#idxRange[i])
    
    def resume_job(self,i:int):
        """Revive the job that failed"""
        if self.browsers[i].session_id == 'Dead':
            self.run_job(i)
        else:
            self.run_job(i)


    def run_job(self) -> None:
        """Execute a job on a low level"""
        for i in self.ins:
            try:
                self.open_browser(i)
                elem = self.grab_search_box(i)
                if elem == 0:
                    self.resume_job(i)
                    continue
                else:
                    elem.send_keys(Keys.RETURN)
            except:
                print("it blew up! run_job()...browser#: "+str(i))
                continue
        pass

    def open_browser(self,i:int):
        """Opens the browser and using parameter value as index"""
        try:
            self.browsers[i].get("https://www.google.com/maps")
        except:
            print("error in open browser")
            time.sleep(2)
            self.browsers[i].get("https://www.google.com/maps")
        
        

    def grab_search_box(self,i:int):
        """The search box which is passed the input address"""
        try:
            elem = self.browsers[i].find_element_by_id("searchboxinput")
            return elem
        except NoSuchElementException:
            print("error in finding searchbox, trying again")
            time.sleep(2)
            elem = self.browsers[i].find_element_by_id("searchboxinput")
        except:
            time.sleep(2)
            elem = self.browsers[i].find_element_by_id("searchboxinput")
            return elem
        return 0

        return elem
    def split(a:int, n:int) -> list(int):
        """Used to split up the index into ranges for iteration"""
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

    def calculate_geo_diff(self,addr) -> float:
        """This computes the delta, distance from two points"""
        for i in self.ins:
            print("move on")
