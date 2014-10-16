## This simple script fetches the easybaycafe.com menu and parses it
from lxml import html
import requests

# Page is the HTML page to parse, in this case we fetch eastbaycafe.com/menu.php
page = requests.get('http://www.eastbaycafe.com/menu.php')

# Now we form our tree variable and fill it with the pages HTML
tree = html.fromstring(page.text)

# Populate menu with the child div's from menu_content_today and iterate over them
menu = tree.xpath('//div[@id="menu_content_today"]')[0]
for item in menu.getchildren()[0].getchildren():
  print item.text_content()
