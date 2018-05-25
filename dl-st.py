#!/usr/bin/env python
# coding=utf-8

from com import write_out_list, DAMTP_BASE

COURSE = "st"
SITE = f"{DAMTP_BASE}examples"


def get_links(*letters):
    return enumerate([f"{SITE}/3P6{letter}.pdf" for letter in letters], 1)


def scrape_st():
    lecture_notes = get_links("")
    problem_sheets = get_links("a", "b", "c", "d")
    problem_solutions = get_links("e", "f", "g", "h")

    write_out_list(COURSE, "n", lecture_notes)
    write_out_list(COURSE, "e", problem_sheets)
    write_out_list(COURSE, "e-s", problem_solutions)

    print("All done!")


if __name__ == "__main__":
    scrape_st()
