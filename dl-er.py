#!/usr/bin/env python
# coding=utf-8

from com import load_site, write_out, SITE_BASE, get_link

SITE = f"{SITE_BASE}postgrad/mathiii/part-iii-mathematical-tripos-examination-rubrics"
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
