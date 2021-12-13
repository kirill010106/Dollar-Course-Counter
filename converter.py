import requests
from bs4 import BeautifulSoup
def get_course():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    page = requests.get("https://www.banki.ru/products/currency/usd/", headers=headers)
    current = page.text
    soup = BeautifulSoup(current, features="lxml")
    course_list = soup.find("div", class_="currency-table__large-text").text.split(",")
    course = float(".".join(course_list))
    return course
def count_value():
    dollars = float((input("Введите желаемое количество долларов для перевода в рубли: ")))
    print(f"{dollars} долларов в рублях: {(course * dollars)} RUB")

course = get_course()
count_value()