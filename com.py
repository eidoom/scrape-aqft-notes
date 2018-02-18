#!/usr/bin/env python
# coding=utf-8

from requests import get
from selenium import webdriver

CHROME_DRIVER_PATH = f"C:\Programs\chromedriver_win32\chromedriver.exe"
COURSES_DIRECTORY = "C:/sync/physics/6_Part_iii/Courses"


def load_site(site):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get(site)
    return driver


def write_out(course, document_type, number, url):
    if document_type == "n":
        folder = "Notes"
    elif document_type == "e":
        folder = "Example_sheets"
    else:
        exit(f"{document_type} is an unknown document_type!")

    filename = f"{COURSES_DIRECTORY}/{course.capitalize()}/{folder}/{course}-{document_type}-{number}.pdf"
    print(f"{url}\n  -> {filename}")
    with open(filename, "wb") as file:
        file.write(get(url).content)


def write_out_list(course, document_type, scrape_data):
    for number, url in scrape_data:
        write_out(course, document_type, number, url)


if __name__ == "__main__":
    exit()
