#!/usr/bin/env python
# coding=utf-8

from com import load_site, write_out

SITE = "http://www.damtp.cam.ac.uk/user/dbs26/AQFT.html"
COURSE = "aqft"


def scrape_aqft():
    driver = load_site(SITE)

    all = [el.get_attribute("href") for el in driver.find_elements_by_xpath("//div[@id='content-primary']/ul/li/b/a")]

    lecture_notes = all[:-4]
    problem_sheets = all[-4:]

    for number, lecture_note_url in enumerate(lecture_notes, 1):
        write_out(COURSE, "n", number, lecture_note_url)

    for number, problem_sheet_url in enumerate(problem_sheets, 1):
        write_out(COURSE, "e", number, problem_sheet_url)

    print("All done!")


if __name__ == "__main__":
    scrape_aqft()
