#!/usr/bin/env python
# coding=utf-8

from requests import get
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def main():
    chrome_driver_path = f"C:\Programs\chromedriver_win32\chromedriver.exe"

    courses = (("QFT", "Quantum Field Theory",),
                ("SFP", "Symmetries, Fields and Particles", "Symmetries and Particles",
                 "Symmetry and Particle Physics", "Symmetry and Particles", "Elementary Particle Physics",),
                ("GR", "General Relativity",),
                ("SFT", "Statistical Field Theory", "Statistical Fields Theory",),
                ("AQFT", "Advanced Quantum Field Theory",),
                ("SM", "Standard Model", ("The Standard Model")),
                ("BH", "Black Holes",),
                ("ST", "String Theory", "Advanced String Theory", ),
                ("SUSY", "Supersymmetry", "Supersymmetry and Extra Dimensions", "Introduction to Supersymmetry",
                 "Supersymmetry and extra dimensions"),
               )

    driver = webdriver.Chrome(chrome_driver_path)
    driver.get("https://www.maths.cam.ac.uk/postgrad/mathiii/part-iii-mathematical-tripos-examination-papers")

    years_data = driver.find_elements_by_xpath("//div[@class='field-item even']/ul/li/a")

    earliest = int(years_data[-1].get_attribute("textContent"))
    latest = int(years_data[0].get_attribute("textContent"))

    years = list(reversed(range(earliest, latest + 1)))
    links = {course[0]: {year: [] for year in years} for course in courses}

    year_urls = [year_data.get_attribute("href") for year_data in years_data]

    for year, year_url in zip(years, year_urls):
        driver.get(year_url)

        def get_link(course):
            try:
                return driver.find_element_by_xpath(f"//th[text()='{course}']/../th/a").get_attribute("href")
            except NoSuchElementException:
                try:
                    return driver.find_element_by_xpath(f"//strong[text()='{course}']/../../th/a").get_attribute(
                        "href")
                except NoSuchElementException:
                    try:
                        return driver.find_element_by_xpath(f"//th[text()='{course}']/../td/a").get_attribute(
                            "href")
                    except NoSuchElementException:
                        pass

        for course_tup in courses:
            for course in course_tup[1:]:
                link = get_link(course)
                if link is not None:
                    links[course_tup[0]][year] += [link]

    for course in courses:
        acronym = course[0]
        for year in years:
            urls = links[acronym][year]
            length = len(urls)
            for url, n in zip(urls, range(0, length)):
                mod = f"_{n}" if length > 1 else ""
                with open(f"C:/sync/physics/6_Part_iii/Courses/{acronym}/Past_papers/{acronym}_{year}{mod}.pdf",
                          "wb") as file:
                    file.write(get(url).content)

    print("All done!")


if __name__ == "__main__":
    main()
