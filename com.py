#!/usr/bin/env python
# coding=utf-8

from requests import get
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

CHROME_DRIVER_PATH = f"C:\Programs\chromedriver_win32\chromedriver.exe"
COURSES_DIRECTORY = "C:/sync/physics/6_Part_iii/Courses"
SITE_BASE = "https://www.maths.cam.ac.uk/"
COURSES = (
    ("qft", "Quantum Field Theory",),
    ("sfp", "Symmetries, Fields and Particles", "Symmetries and Particles",
     "Symmetry and Particle Physics", "Symmetry and Particles", "Elementary Particle Physics",),
    ("gr", "General Relativity",),
    ("sft", "Statistical Field Theory", "Statistical Fields Theory",),
    ("aqft", "Advanced Quantum Field Theory",),
    ("sm", "Standard Model", "The Standard Model",),
    ("bh", "Black Holes",),
    ("st", "String Theory", "Advanced String Theory",),
    ("susy", "Supersymmetry", "Supersymmetry and Extra Dimensions", "Introduction to Supersymmetry",
     "Supersymmetry and extra dimensions",),
    ("cqs", "Classical and Quantum Solitons", "Solitons and Instantons",),
    ("c", "Cosmology",),
)


def get_link(driver, course):
    try:
        return driver.find_element_by_xpath(f"//th[text()='{course}']/../th/a").get_attribute("href")
    except NoSuchElementException:
        try:
            return driver.find_element_by_xpath(f"//strong[text()='{course}']/../../th/a").get_attribute("href")
        except NoSuchElementException:
            try:
                return driver.find_element_by_xpath(f"//th[text()='{course}']/../td/a").get_attribute("href")
            except NoSuchElementException:
                try:
                    return driver.find_element_by_xpath(
                        f"//strong[text()='{course}']/../../th/strong/a").get_attribute("href")
                except NoSuchElementException:
                    pass


def load_site(site):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get(site)
    return driver


def write_out(course, name, url, extension="pdf"):
    filename = f"{COURSES_DIRECTORY}/{course.upper()}/{name}.{extension}"
    print(f"{url}\n  -> {filename}")
    with open(filename, "wb") as file:
        file.write(get(url).content)


def write_out_list(course, document_type, scrape_data):
    for number, url in scrape_data:
        if document_type == "n":
            folder = "Notes"
        elif "e" in document_type:
            folder = "Example_sheets"
        elif document_type == "p":
            folder = "Past_papers"
        else:
            exit(f"{document_type} is an unknown document_type!")

        write_out(course, f"{folder}/{course}-{document_type}-{number}", url)


def get_named_urls(driver, xpath):
    return [(el.get_attribute("textContent"), el.get_attribute("href")) for el in driver.find_elements_by_xpath(xpath)]


def get_urls(driver, xpath):
    return [el.get_attribute("href") for el in driver.find_elements_by_xpath(xpath)]


if __name__ == "__main__":
    exit()
