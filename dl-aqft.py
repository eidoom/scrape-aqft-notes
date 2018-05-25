#!/usr/bin/env python
# coding=utf-8

from com import load_site, write_out, get_named_urls, get_urls, write_out_list, DAMTP_BASE

SITE_0 = f"{DAMTP_BASE}dbs26/AQFT.html"
SITE_1 = f"{DAMTP_BASE}kafr2/aQFT"
COURSE = "aqft"


def scrape_aqft():
    driver = load_site(SITE_0)
    first = get_urls(driver, "//div[@id='content-primary']/ul/li/b/a")

    driver.get(SITE_1)
    second = get_named_urls(driver, "//body/table/tbody/tr/td/a[contains(@href,'.pdf')]")

    driver.quit()

    lecture_notes = first[:-4]
    problem_sheets = first[-4:]

    write_out_list(COURSE, "n", enumerate(lecture_notes, 1))
    write_out_list(COURSE, "e", enumerate(problem_sheets, 1))

    for name, url in second:
        if name[-4:] == ".pdf":
            name = name[:-4]
        write_out(COURSE, f"Example_sheets/Kai_Roehrig_solutions/{name}", url)

    print("All done!")


if __name__ == "__main__":
    scrape_aqft()
