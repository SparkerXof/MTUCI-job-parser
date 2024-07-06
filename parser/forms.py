from django import forms

class VacationForm(forms.Form):
    hhru = forms.BooleanField(label="hh.ru", required=False)
    habr = forms.BooleanField(label="Хабр Карьера", required=False)
    location = forms.CharField(label="Регион:", max_length=100)
    job = forms.CharField(label="Работа:", max_length=100, required=False)
    salary = forms.IntegerField(label="Минимальная зарплата:", min_value=0, initial=0)
    experience = forms.IntegerField(label="Опыт работы:", min_value=0, initial=0)
    experience_skip = forms.BooleanField(label="Опыт не имеет значения:", required=False)
    fulltime = forms.BooleanField(label="Полный день", required=False)
    shift = forms.BooleanField(label="Сменный график", required=False)
    home = forms.BooleanField(label="Удалённая работа", required=False)
    flex = forms.BooleanField(label="Гибкий график", required=False)
    watch = forms.BooleanField(label="Вахтовый метод", required=False)
