from tkinter import *
from main import Main
from main_2 import Main_2

class Interface(Tk):
    def __init__(self):
        super(Interface, self).__init__()
        self.title("BasketLakers")
        self.config(background='#6700A6')
        self.iconbitmap("logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)


        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="BasketLakers" , bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=400, y=20)

        text_principal = Label(self, text="""
            Bienvenue sur BasketLakers

            Tu cherche a visionez la biographie des joueurs
            et leur photo sans te casser la tete ?
                
            Alors BasketLakers est la
            pour t'aider !
            """, bg="#6700A6", font=('arial', 17),
                                fg='#fff')
        text_principal.place(x=-50, y=180)
        text_principal["justify"] = CENTER

        boutton_histoires = Button(self, text="Histoires des Lakers", bg="#000000", fg="white", relief=FLAT,
                                    font=('arial', 20), width=20, activebackground="#000000", activeforeground="White",
                                   command=lambda: Main_2(self.destroy()))
        boutton_histoires.place(x=640, y=170)


        boutton_Biographie = Button(self, text="Biographie des joueurs", bg="#000000", fg="white", relief=FLAT,
                                   font=('arial', 20), width=20, activebackground="#000000", activeforeground="White",
                                   command=lambda: Main(self.destroy()))
        boutton_Biographie.place(x=640, y=350)

        droit = Label(self, text="© 2022 BasketLakers", bg="#6700A6", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=420, y=510)

        self.mainloop()
Interface()