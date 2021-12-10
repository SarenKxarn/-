from tkinter import *

def login():
    # извлекаем данные из формы
    cnt = country.get()
    yr = year.get()
    # проверяем заполненные данные
    if cnt == '' or yr == '':
        message.set("Заполните пустые поля!!!")
    else:
      if cnt == "Россия":
          if 1895 <= int(yr) <= 2021:
            message.set("Настройки применены!")
          else:
            message.set("Год вне диапазона!")
      else:
        message.set("Данной страны нет в списке!")


# функция авторизации формы Tk() из библиотеки tkinter

def random():
    message.set("Применены случайные настройки")

def FilmForm():
    global film_window
    film_window = Tk()
    film_window.title("Настройки предпочтений фильмов")
    film_window.geometry("600x400")
    film_window.columnconfigure(0, weight=2) # вес 0го столбца
    film_window.columnconfigure(1, weight=1) # вес 1го столбца
    film_window.columnconfigure(2, weight=1) # вес 2го столбца
    # объявление переменных для использования в других функциях
    global message
    global country
    global year
    country = StringVar()
    year = StringVar()
    message = StringVar()
    lab_enter = Label(film_window, text="Выберите три любимых жанра", bg="green2", fg="orange4")
    spn_genre0 = Spinbox(film_window, values=('Боевик', 'Комедия', 'Драма', 'Хоррор', 'Фэнтези', 'Фантастика'), width=15)
    spn_genre1 = Spinbox(film_window, values=('Боевик', 'Комедия', 'Драма', 'Хоррор', 'Фэнтези', 'Фантастика'), width=15)
    spn_genre2 = Spinbox(film_window, values=('Боевик', 'Комедия', 'Драма', 'Хоррор', 'Фэнтези', 'Фантастика'), width=15)
    lab_cntr = Label(film_window, text="Страна")
    ent_cntr = Entry(film_window, textvariable=country)
    lab_yr = Label(film_window, text="Год выпуска(1895 - 2021)")
    ent_yr = Entry(film_window, textvariable=year)
    btn_log = Button(film_window, text="Применить настройки", width=30, height=1, bg="green2", command=login)
    btn_random = Button(film_window, text="Случайный выбор", width=30, height=1, bg="green2", command=random)
    lab_msg = Label(film_window, text="", textvariable=message)
    lab_enter.grid(column=0, row=0, columnspan=3)
    spn_genre0.grid(column=0, row=1)
    spn_genre1.grid(column=1, row=1)
    spn_genre2.grid(column=2, row=1)
    lab_cntr.grid(column=0, row=2)
    ent_cntr.grid(column=0, row=3)
    lab_yr.grid(column=2, row=2)
    ent_yr.grid(column=2, row=3)
    btn_log.grid(column=0, row=4, columnspan=3)
    btn_random.grid(column=0, row=5, columnspan=3)
    lab_msg.grid(column=0, row=6, columnspan=3)
    film_window.mainloop()

# вызов функции формы
if __name__ == '__main__':
    FilmForm()