import PySimpleGUI as Sg
Sg.theme("DarkGreen4")
Sg.theme_text_color("#FFFF00")
Window = Sg.Window(title="Profile Firda Kharisma",
                   layout=[[Sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25))],
                           [Sg.Text("NPM    : 2310010683")],
                           [Sg.Text("Nama   : Firda Kharisma")],
                           [Sg.Text("Kelas  : 5A Non Regular Banjarmasin")],
                           [Sg.Text("Matkul : Pemrograman Visual 3")]
                           ],
                    size=(500,200),
                    font=("Times", 18))
Window()
Window.close()