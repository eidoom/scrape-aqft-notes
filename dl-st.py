#!/usr/bin/env python
# coding=utf-8

from com import write_out_list

COURSE = "st"


def get_links(*letters):
    return enumerate([f"http://www.damtp.cam.ac.uk/user/examples/3P6{letter}.pdf" for letter in letters], 1)


def scrape_st():
    lecture_notes = get_links("c")
    problem_sheets = get_links("a", "b", "d")
    problem_solutions = get_links("e")

    write_out_list(COURSE, "n", lecture_notes)
    write_out_list(COURSE, "e", problem_sheets)
    write_out_list(COURSE, "e-s", problem_solutions)

    print("All done!")


if __name__ == "__main__":
    scrape_st()
