#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:12:57 2017

@author: cocco
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import time

from facebook import *
import cleverbot3
import humanRandom

""" Opens FacebookClient and chats with random person """
# Setup
username,password= sys.argv[1], sys.argv[2]
fb = FacebookClient(username,password)
chatbot = cleverbot3.Session()
# choose random "friend" to chat with

posts=[]
wall= fb.browser.find_element(By.CSS_SELECTOR,"div[id='contentArea']")
for _ in range(5):
    print( "scroll")
    time.sleep(0.5)
    posts.extend( wall.find_elements(By.CSS_SELECTOR,"div[id*='substream']"))
    fb.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     
for post in set(posts):
    #time.sleep(2+random.random())
    try:
        post.find_element(By.CSS_SELECTOR,".UFILikeLink").click()
        print("like")
    except:
        print("no like here!")       
      
# close browser
#fb.destroy()
