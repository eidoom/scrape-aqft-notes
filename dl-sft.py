#!/usr/bin/env python
# coding=utf-8

from com import load_site, write_out_list, get_urls, DAMTP_BASE

SITE = f"{DAMTP_BASE}tong/sft.html"
COURSE = "sft"


def scrape_sft():
    driver = load_site(SITE)
    notes = get_urls(driver, "//div[@id='content-primary']/strong/center/a[contains(@href,'.pdf')]")
    probs = get_urls(driver, "//div[@id='content-primary']/ul/li/b/a[contains(@href,'.pdf')]")[4:]
    driver.quit()

    write_out_list(COURSE, "n", enumerate(notes))
    write_out_list(COURSE, "e", enumerate(probs, 1))

    print("All done!")


if __name__ == "__main__":
    scrape_sft()
