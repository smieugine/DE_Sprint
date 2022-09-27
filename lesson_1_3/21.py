 #1. Необходимо спарсить данные о вакансиях python разработчиков с сайта hh.ru, введя в поиск python разработчик
#и указав, что мы рассматриваем все регионы. Необходимо спарсить:
#Название вакансии
#Требуемый опыт работы
#Заработную плату
#Регион

'''hh.ru и avito не дают парсить себя
Было решено парсить rabota.ru
Почти вся информация содержалась на главной странице и поэтому не пришлось парсить глубоко по ссылкам
Поля "опыт работы"" на странице не было и поэтому заменил на компанию '''

import requests as req
from bs4 import BeautifulSoup

url  = "https://www.rabota.ru/vacancy/?query=Senior%20Python%20Developer&sort=relevance"
resp = req.get(url)
soup = BeautifulSoup(resp.text, "lxml")

tags = soup.find_all(
    class_=[
        "vacancy-preview-card__top"
    ]
)

title   = soup.find_all(class_=["vacancy-preview-card__title_border"])
salary  = soup.find_all(class_=["vacancy-preview-card__salary"])
region  = soup.find_all(class_=["vacancy-preview-location__address-text"])
company = soup.find_all(class_=["vacancy-preview-card__company-name"])

title   = [i.text.strip() for i in title]
salary  = [i.text.strip() for i in salary]
region  = [i.text.strip() for i in region]
company = [i.text.strip() for i in company]


res = []

for i in zip(title, salary, region, company):
    data = {
        "title":   i[0],
        "salary":  i[1],
        "region":  i[2],
        "company": i[3]
    }
    res.append(data)

print(res)
