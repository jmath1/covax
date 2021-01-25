from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import os
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        import pdb; pdb.set_trace()

chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(executable_path="/Users/jmath/Downloads/chromedriver2",chrome_options=chrome_options)  
driver.get("https://padoh.maps.arcgis.com/home/webmap/viewer.html?useExisting=1&layers=8f6a17bbb8af42c0951c24e3b0a15566&layerId=0") 
import pdb; pdb.set_trace()