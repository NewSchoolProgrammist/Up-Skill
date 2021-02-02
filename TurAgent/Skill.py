import eel

eel.init("WEbb")

@eel.expose
def calll(place):
    if place == "Андрей":
        return "ЛОХ"
    if place == "CSS":
        return "Есть в наличии, вот ссылка:  file:///Users/user/Desktop/TurAgent/Tur.html"
        print("Есть в наличии, вот ссылка:    file:///Users/user/Desktop/TurAgent/Tur.html")
    else:
        return "Такого курса нет"
    print("Есть в наличии, вот ссылка:    file:///Users/user/Desktop/TurAgent/Tur.html")
eel.start("Tur.html", size=(1200,1200))
