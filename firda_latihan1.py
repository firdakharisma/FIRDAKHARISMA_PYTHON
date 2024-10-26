import PySimpleGUI as Sg
Window = Sg.Window(title="Profile",
                   layout=[[Sg.Text("NPM    : 2310010683")],
                           [Sg.Text("Nama   : Firda Kharisma")],
                           [Sg.Text("Kelas  : 5A Non Regular Banjarmasin")],
                           [Sg.Text("Matkul : Pemrograman Visual 3")]
                           ],
                    size=(400,200))
Window()
Window.close()