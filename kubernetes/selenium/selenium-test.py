#!/usr/bin/env python

from selenium import webdriver

def check_chrome():
  options = webdriver.ChromeOptions()
  driver = webdriver.Remote(
    command_executor='http://localhost/wd/hub',
    options=options
  )
  driver.get("http://www.google.com")
  assert "google" in driver.page_source
  driver.quit()
  print("Browser %s checks out!" % browser)


check_chrome()

