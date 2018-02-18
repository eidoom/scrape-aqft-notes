#!/usr/bin/env python
# coding=utf-8

from requests import get
from selenium import webdriver

CHROME_DRIVER_PATH = f"C:\Programs\chromedriver_win32\chromedriver.exe"
COURSES_DIRECTORY = "C:/sync/physics/6_Part_iii/Courses"
SITE = "http://www.damtp.cam.ac.uk/user/cet34/teaching/SM/"
COURSE = "sm"
COURSE_CAPS = COURSE.capitalize()


def load_site():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get(SITE)
    return driver


def write_out(scrape_data, document_type):
    if document_type == "n":
        folder = "Notes"
    elif document_type == "e":
        folder = "Example_sheets"
    else:
        exit(f"{document_type} is an unknown document_type!")

    for number, url in scrape_data:
        filename = f"{COURSES_DIRECTORY}/{COURSE_CAPS}/{folder}/{COURSE}-{document_type}-{number}.pdf"
        print(f"{url} -> {filename}")
        with open(filename, "wb") as file:
            file.write(get(url).content)


def main():
    driver = load_site()

    raw = [(el.get_attribute("textContent"), el.get_attribute("href")) for el in
           driver.find_elements_by_xpath("//div[@class='main']/ul/li/a")]

    lecture_notes = []
    problem_sheets = []
    lecture_number = 0

    for name, link in raw:
        if "Example" in name:
            problem_number = "".join([a for a in name if a.isdigit()])
            problem_sheets.append((problem_number, link))
        else:
            lecture_notes.append((lecture_number, link))
            lecture_number += 1

    write_out(lecture_notes, "n")
    write_out(problem_sheets, "e")

    print("All done!")


if __name__ == "__main__":
    main()
