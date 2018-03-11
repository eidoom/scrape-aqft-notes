#!/usr/bin/env python
# coding=utf-8

from selenium.common.exceptions import NoSuchElementException

from com import load_site, write_out

SITE = "https://www.maths.cam.ac.uk/postgrad/mathiii/part-iii-mathematical-tripos-examination-papers"
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
)


def scrape_past_papers():
    driver = load_site(SITE)

    years_data = driver.find_elements_by_xpath("//div[@class='field-item even']/ul/li/a")

    earliest = int(years_data[-1].get_attribute("textContent"))
    latest = int(years_data[0].get_attribute("textContent"))

    years = list(reversed(range(earliest, latest + 1)))
    links = {course[0]: {year: [] for year in years} for course in COURSES}

    year_urls = [year_data.get_attribute("href") for year_data in years_data]

    for year, year_url in zip(years, year_urls):
        driver.get(year_url)

        def get_link(course):
            try:
                return driver.find_element_by_xpath(f"//th[text()='{course}']/../th/a").get_attribute("href")
            except NoSuchElementException:
                try:
                    return driver.find_element_by_xpath(f"//strong[text()='{course}']/../../th/a").get_attribute("href")
                except NoSuchElementException:
                    try:
                        return driver.find_element_by_xpath(f"//th[text()='{course}']/../td/a").get_attribute("href")
                    except NoSuchElementException:
                        pass

        for course_tup in COURSES:
            for course in course_tup[1:]:
                link = get_link(course)
                if link is not None:
                    links[course_tup[0]][year] += [link]

    driver.quit()

    for course in COURSES:
        acronym = course[0]
        for year in years:
            urls = links[acronym][year]
            length = len(urls)
            for url, n in zip(urls, range(0, length)):
                mod = f"_{n}" if length > 1 else ""
                write_out(acronym, "Past_papers", f"{acronym}-{year}{mod}", url)

    print("All done!")


if __name__ == "__main__":
    scrape_past_papers()
