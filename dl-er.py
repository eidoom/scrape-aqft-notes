#!/usr/bin/env python
# coding=utf-8

from com import load_site, write_out, MATH_BASE, get_link, COURSES

SITE = f"{MATH_BASE}part-iii-mathematical-tripos-examination-rubrics"


def scrape_exam_rubrics():
    driver = load_site(SITE)

    links = {}

    for course_tup in COURSES:
        for course in course_tup[1:]:
            link = get_link(driver, course)
            if link is not None:
                links[course_tup[0]] = link

    driver.quit()

    for course in COURSES:
        acronym = course[0]
        write_out(acronym, f"{acronym}-exam_rubric", links[acronym])

    print("All done!")


if __name__ == "__main__":
    scrape_exam_rubrics()
