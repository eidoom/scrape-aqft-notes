#!/usr/bin/env python
# coding=utf-8

from string import ascii_lowercase

from com import write_out_list

COURSE = "st"


def scrape_st():
    problem_sheets = enumerate(
        [f"http://www.damtp.cam.ac.uk/user/examples/3P6{letter}.pdf" for letter in ascii_lowercase[:4]], 1)
    lecture_notes = [(0, "http://www.damtp.cam.ac.uk/user/examples/3P6La.pdf")]

    write_out_list(COURSE, "n", lecture_notes)
    write_out_list(COURSE, "e", problem_sheets)

    print("All done!")


if __name__ == "__main__":
    scrape_st()
