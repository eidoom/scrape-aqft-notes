#!/usr/bin/env python
# coding=utf-8

from requests import get
from selenium import webdriver


def main():
    chrome_driver_path = f"C:\Programs\chromedriver_win32\chromedriver.exe"

    driver = webdriver.Chrome(chrome_driver_path)
    driver.get("http://www.damtp.cam.ac.uk/user/dbs26/AQFT.html")

    all = [el.get_attribute("href") for el in driver.find_elements_by_xpath("//div[@id='content-primary']/ul/li/b/a")]

    lecture_notes = all[:-4]
    problem_sheets = all[-4:]

    for number, lecture_note_url in enumerate(lecture_notes, 1):
        with open(f"C:/sync/physics/6_Part_iii/Courses/AQFT/Notes/aqft-n-{number}.pdf", "wb") as file:
            file.write(get(lecture_note_url).content)

    for number, problem_sheet_url in enumerate(problem_sheets, 1):
        with open(f"C:/sync/physics/6_Part_iii/Courses/AQFT/Example_sheets/aqft-e-{number}.pdf", "wb") as file:
            file.write(get(problem_sheet_url).content)

    print("All done!")


if __name__ == "__main__":
    main()
