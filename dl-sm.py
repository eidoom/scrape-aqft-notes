#!/usr/bin/env python
# coding=utf-8

from com import load_site, write_out_list, get_named_urls, DAMTP_BASE

SITE = f"{DAMTP_BASE}/cet34/teaching/SM/"
COURSE = "sm"


def scrape_sm():
    driver = load_site(SITE)
    raw = get_named_urls(driver, "//div[@class='main']/ul/li/a")
    driver.quit()

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

    write_out_list(COURSE, "n", lecture_notes)
    write_out_list(COURSE, "e", problem_sheets)

    print("All done!")


if __name__ == "__main__":
    scrape_sm()
