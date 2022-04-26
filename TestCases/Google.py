import pytest
from selenium import webdriver


def test_one():
    driver = webdriver.Firefox(executable_path='E:\\GitPractice\\Drivers\\geckodriver.exe')
    driver.get('https://www.google.co.in')
    print("Page Title is : %s" % driver.title)
    driver.quit() 2
