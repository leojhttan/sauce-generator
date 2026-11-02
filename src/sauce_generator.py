import random
import webbrowser


def order_up():
    sauce = random.randrange(478372)
    url = f"https://nhentai.net/g/{sauce}"
    print(f"{sauce}")
    webbrowser.open(url, 0, True)


Stop = 0
while Stop <= 1:
    order_up()
    Stop = Stop + 1
