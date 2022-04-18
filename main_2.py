from tkinter import *


class Main_2(Tk):
    def __init__(self, Interface = None):
        super(Main_2, self).__init__()
        self.title("Histoires des Lakers")
        self.geometry("1000x542")
        self.iconbitmap("logo.ico")
        self.config(background='#6700A6')
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title = Label(self, text="Histoires des Lakers", font=("times new roman",25),bg='#000000',fg='white',anchor='w')
        title.place(x=350, y=20)

        title = Label(self, text="Nous allons vous raconter la petit histoires des Lakers-Los Angeles :", font=("times new roman",15),bg='#6700A6',fg='white',anchor='w')
        title.place(x=15, y=120)

        title = Label(self, text="Tout commence en 1946 par la création de la NBL, qui deviendra en 1949 la NBA.  La franchise Détroit Gems voit le jour ",font=("times new roman", 15), bg='#6700A6', fg='white', anchor='w')
        title.place(x=15, y=180)

        title = Label(self,text="et connait une première saison catastrophique ponctuée de 40 défaites en 44 matches.",
                      font=("times new roman", 15), bg='#6700A6', fg='white', anchor='w')
        title.place(x=15, y=200)

        title = Label(self, text="En 1947, elle est rachetée et délocalisée à Minneapolis sous le nom de « Lakers » (les habitants du Lac) en référence à la",
                      font=("times new roman", 15), bg='#6700A6', fg='white', anchor='w')
        title.place(x=15, y=260)

        title = Label(self,text="région des « Grands Lacs » dont est proche la ville.",
                      font=("times new roman", 15), bg='#6700A6', fg='white', anchor='w')
        title.place(x=15, y=280)

        title = Label(self, text="Elle restera en place jusqu’en 1960 avant de rejoindre Los Angeles pour ses plus belles heures de gloire.",
                      font=("times new roman", 15), bg='#6700A6', fg='white', anchor='w')
        title.place(x=15, y=320)

        self.mainloop()

