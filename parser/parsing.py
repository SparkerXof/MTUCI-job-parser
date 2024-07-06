from bs4 import BeautifulSoup
from parser.forms import VacationForm
from parser.models import VacationModel
from parser.codes import hhru_area, habr_area
import requests
import json

hhru_vacations_url = "https://hh.ru/search/vacancy"
habr_vacations_url = "https://career.habr.com/vacancies"

def get_hhru_vacations(form: VacationForm):
    if form["experience_skip"].value():
        experience = None
    elif int(form["experience"].value()) < 1:
        experience = 'noExperience'
    elif int(form["experience"].value()) >= 1 and int(form["experience"].value()) < 3:
        experience = 'between1And3'
    elif int(form["experience"].value()) >= 1 and int(form["experience"].value()) < 3:
        experience = 'between3And6'
    else:
        experience = 'moreThan6'
    schedule = []
    if form["fulltime"].value():
        schedule.append('fullDay')
    if form["shift"].value():
        schedule.append('shift')
    if form["home"].value():
        schedule.append('remote')
    if form["flex"].value():
        schedule.append('flexible')
    if form["watch"].value():
        schedule.append('flyInFlyOut')
    for i in range(5):
        param = {
            'area': hhru_area[form['location'].value()],
            'page': i,
            'per_page': 100,
            'text': form["job"].value(),
            'experience': experience,
            'salary': form["salary"].value(),
            'schedule': schedule
        }
        req = requests.get("https://api.hh.ru/vacancies", param)
        data = req.content.decode()
        req.close()
        obj = json.loads(data)
        for item in json.loads(data)["items"]:
            if item["experience"] == 'noExperience':
                min_exp = None
                max_exp = 0
            elif item["experience"] == 'between1And3':
                min_exp = 1
                max_exp = 3
            elif item["experience"] == 'between3And6':
                min_exp = 3
                max_exp = 6
            else:
                min_exp = 6
                max_exp = None
            name = "None"
            if item["department"] != None:
                name = item["department"]["name"]
            vac = VacationModel(service="hh.ru", company_name=name, job=item["name"], link=item["alternate_url"], location=item["area"]["name"], min_salary=item["salary"]["from"], max_salary=item["salary"]["to"], currency=item["salary"]["currency"], min_experience=min_exp, max_experience=max_exp, work_time=item["schedule"]["name"])
            vac.save()


def get_habr_vacations(form: VacationForm):
    for i in range(1, 21):
        soup = BeautifulSoup(requests.get(habr_vacations_url + "?" + (("?locations[]=" + habr_area[str(j).lower] + "&") for j in str(form["location"].value()).split(", ")) + "page=" + i + "&q=" + form["job"].value() + "&salary=" + form["salary"].value()).text, "html.parser")
        vacations = soup.find_all('div', class_='vacancy-card__info')
        for vacation in vacations:
            name = vacation.find('a', class_="link-comp link-comp--appearance-dark")
            job = vacation.find('a', class_="vacancy-card__title-link")
            other = [j for j in vacation.find('div', class_="vacancy-card__meta").stripped_strings]
            while '•' in other:
                  other.remove('•')
            if other[-1] == "Можно удаленно":
                  other.pop(-1)
            if len(other)>1 and (other[1] == "Полный рабочий день" or other[1] == "Неполный рабочий день"):
                max_others = 2
            else:
                max_others = 1
            while len(other) > max_others:
                other.pop(1)
            while len(other) < 2:
                 other.append(None)
            vac = VacationModel(service="Хабр", company_name=name.text, job=job.text, link="https://career.habr.com"+job["href"], location=other[0], min_salary=None, max_salary=None, currency=None, min_experience=None, max_experience=None, work_time=other[1])
            vac.save()


def process_vacation_form(form: VacationForm):
    if form["hhru"].value():
        get_hhru_vacations(form)
    if form["habr"].value():
        get_habr_vacations(form)