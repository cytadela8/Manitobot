from utility import *

new_night_com = {
    "Szeryf": [(
               "Wybierz osobę, którą chcesz zamknąć. Użyj komendy `&zamk NICK`",
               "arrest")],
    "Dziwka": [(
               "Wybierz osobę, którą chcesz zadziwić. Użyj komendy `&dziw NICK`",
               "dziw")],
    "Pastor": [(
               "Wybierz osobę, którą chcesz sprawdzić. Użyj komendy `&spow NICK`",
               "pasteur")],
    "Opój": [(
             "Jeśli chcesz upijać użyj komendy `&pij NICK`, jeśli nie chcesz upijać użyj `&nie`. Możesz upijać jeszcze {} razy",
             "drink")],
    "Pijany_Sędzia": [(
                      "Jeśli chcesz upijać użyj komendy `&pij NICK`, jeśli nie chcesz upijać użyj `&nie`. Możesz upijać jeszcze {} razy",
                      "drink")],
    "Hazardzista": [(
                    "Jeśli chcesz zagrać w rosyjską ruletkę użyj `&graj NICK`, jeśli nie użyj `&nie`",
                    "play")],
    "Mściciel": [(
                 "Jeśli chcesz zabijać użyj `&zabij NICK`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                 "kill")],
    "Wojownik": [(
                 "Jeśli chcesz zabijać użyj `&zabij NICK`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                 "kill")],
    "Zielona_Macka": [(
                      "Jeśli chcesz zabijać użyj `&zabij NICK`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                      "kill")],
    "Samotny_Kojot": [(
                      "Jeśli chcesz zabijać użyj `&zabij NICK`, jeśli nie użyj `&nie`",
                      "kill")],
    "Płonący_Szał": [(
                     "Jeśli chcesz zabijać użyj `&zabij NICK`, jeśli nie użyj `&nie`",
                     "kill")],
    "Cicha_Stopa": [(
                    "Jeśli chcesz podłożyć komuś posążek użyj `&podł NICK`, jeśli nie użyj `&nie`",
                    "plant")],
    "Złodziej": [(
                 "Jeśli chcesz spróbować ukraść posążek użyj `&szukaj`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                 "search")],
    "Purpurowa_Przyssawka": [(
                             "Jeśli chcesz spróbować ukraść posążek użyj `&szukaj`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                             "search")],
    "Szuler": [(
               "Jeśli chcesz kogoś oszulerzyć użyj `&ograj NICK`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
               "cheat")],
    "Szamanka": [(
                 "Jeśli chcesz podłożyć komuś ziółka użyj `&zioł NICK`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                 "herb")],
    "Lornecie_Oko": [(
                     "Jeśli chcesz sprawdzić kto ma posążek użyj `&kto`, jeśli nie użyj `&nie`. Możesz działać raz na grę.",
                     "who")],
    "Detektor": [
        ("Aby sprawdzić gdzie znajduje się posążek użyj `&detekt`", "detect")],
    "Pożeracz_Umysłów": [
        ("Aby sprawdzić czyjąś kartę użyj `&rola NICK`", "eat")],
    "Szaman": [(
               "Aby sprawdzić czyjąś kartę użyj `&szam NICK`, , jeśli nie użyj `&nie`. Możesz działać raz na grę.",
               "szam")],
    "Wikary": [(
               "Aby sprawdzić czy osoba należy do frakcji posiadaczy posążka użyj `&posiad NICK`",
               "holders")],
    "Ministrant": [(
                   "Pastor nie żyje. Aby sprawdzić frakcję jakiegoś gracza użyj `&spow NICK`. Możesz to zrobić {} raz",
                   "pasteur")],
    "Misjonarz": [(
                  "Aby sprawdzić czy osoba jest heretykiem użyj `&heretyk NICK`. Jeśli po chcesz dodatkowo przeszukać tą osobę użyj `&przesz`, jeśli nie użyj `&nie`, możesz to zrobić jeszcze {} razy",
                  "reserch")],
    "Spowiednik": [(
                   "Aby sprawdzić kartę kracza użyj `&rola NICK`, możesz to zrobić 1 raz. Aby dobić sprawdzaną osobę użyj `&dobij`",
                   "eat")],
    "Lusterko": [(
                 "Aby sprawdzić czyjąś rolę użyj `&lustruj NICK`. Jeżeli chcesz skopiować zdolność tej osoby użyj `&kopiuj`. Możesz to zrobić jeszcze {} razy",
                 "copy")],
    "Lucky_Luke": [(
                   "Aby kogoś przeszukać użyj `&szukaj NICK`. Następnie, aby kogoś zabić użyj `&zabij NICK`, możesz zabijać jeszcze {} razy",
                   "kill"), (
                   "\nAby zacząć śledzić użyj `&śledź NICK`, możesz to zrobić jeszcze {} razy. Kiedy użyjesz wszystkich pożądanych zdolności użyj `&kto`, aby dowiedzieć się kto ma posążek.",
                   "follow")]
}

night_action_com_public = {
    "Szeryf": ("Zamknięty został {}", [get_town_channel], [get_manitou_role]),
    "Opój": ("Upity został {}", [], [get_manitou_role]),
    "Pijany_Sędzia": ("Upity został {}", [], [get_manitou_role]),
    "Pastor": ("Pastor sprawdził {}", [], [get_manitou_role]),
    "Dziwka": ("Dziwka zadziwiła {}", [], [get_manitou_role])
}

night_action_com_private = {
    "Szeryf": "Zostałeś zamknięty. Nie obudzisz się więcej tej nocy.",
    "Opój": "Zostałeś upity. Nie obudzisz się więcej tej nocy.",
    "Pijany_Sędzia": "Zostałeś upity. Nie obudzisz się więcej tej nocy.",
    "Dziwka": "Zostałeś zadziwiony przez {}"
}

operation_com_private = {
    "arrest": "Zostałeś zamknięty. Nie obudzisz się więcej tej nocy.",
    "drink": "Zostałeś upity. Nie obudzisz się więcej tej nocy.",
    "dziw": "Zostałeś zadziwiony przez **{author}**",
    "cheat": "Zostałeś ograny przez Szulera, nie obudzisz się więcej tej nocy"
}

operation_com_public = {
    "wins": ("Decyzją Sędziego pojedynek wygrywa **{subject}**",
             [get_town_channel, get_glosowania_channel], []),
    "arrest": (
    "Szeryf zamknął **{subject}**", [get_town_channel, get_manitou_notebook],
    [get_manitou_role]),
    "dziw": (
    "Dziwka zadziwiła {subject}", [get_manitou_notebook], [get_manitou_role]),
    "pasteur": (
    "Pastor sprawdził {subject}", [get_manitou_notebook], [get_manitou_role]),
    "drink": (
    "Upity został {subject}", [get_manitou_notebook], [get_manitou_role]),
    "refuse": (
    "{role} odmówił skorzystania ze swojej zdolności", [get_manitou_notebook],
    [get_manitou_role]),
    "play": (
    "{role} zabił {subject}", [get_manitou_notebook], [get_manitou_role]),
    "plant": ("{role} podłożył(a) posążek {subject}", [get_manitou_notebook],
              [get_manitou_role]),
    "cheat": (
    "{role} ograł {subject}", [get_manitou_notebook], [get_manitou_role]),
    "szam": (
    "{role} sprawdził {subject}", [get_manitou_notebook], [get_manitou_role]),
    "who": ("{role} dowiedział(-o) się kto ma posążek", [get_manitou_notebook],
            [get_manitou_role]),
    "detect": (
    "{role} sprawdził {subject}", [get_manitou_notebook], [get_manitou_role]),
    "eat": ("{role} sprawdził rolę {subject}", [get_manitou_notebook],
            [get_manitou_role]),
    "herb": ("{role} podłożyła ziólka {subject}", [get_manitou_notebook],
             [get_manitou_role]),
    "holders": (
    "{role} dowiedział się czy {subject} należy do frakcji posiadaczy posążka",
    [get_manitou_notebook], [get_manitou_role]),
    "finoff": (
    "{role} zabił {subject}", [get_manitou_notebook], [get_manitou_role]),
    "burn": (
    "{role} zabił {subject}", [get_manitou_notebook], [get_manitou_role]),
    "heretic": ("{role} dowiadział się, czy {subject} jest heretykiem",
                [get_manitou_notebook], [get_manitou_role]),
    "research": (
    "{role} przeszukał {subject}", [get_manitou_notebook], [get_manitou_role])
}


async def night_send(author, member, role):
    if role in night_action_com_private:
        await member.send(
            night_action_com_private[role].format(get_nickname(author.id)))
    mess_det = night_action_com_public[role]
    for channel in mess_det[1]:
        await channel().send(mess_det[0].format(
            member.name if member.nick == None else member.nick))
    for funk in mess_det[2]:
        for person in funk().members:
            await person.send(mess_det[0].format(get_nickname(member.id)))


async def operation_send(operation, author, role, member):
    try:
        mess_det = operation_com_public[operation]
        for channel in mess_det[1]:
            await channel().send(mess_det[0].format(subject=member.display_name,
                                                    role=role.replace('_',
                                                                      ' ')))
        for funk in mess_det[2]:
            for person in funk().members:
                await person.send(
                    mess_det[0].format(subject=member.display_name,
                                       role=role.replace('_', ' ')))
    except AttributeError:
        try:
            for channel in mess_det[1]:
                await channel().send(
                    mess_det[0].format(role=role.replace('_', ' ')))
            for funk in mess_det[2]:
                for person in funk().members:
                    await person.send(
                        mess_det[0].format(role=role.replace('_', ' ')))
        except KeyError:
            pass
    except KeyError:
        pass
    try:
        mess = operation_com_private[operation]
        await member.send(mess.format(author=author.display_name))
    except KeyError:
        pass
