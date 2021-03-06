import datetime
import os
from random import shuffle

import globals
import postacie
from game import Game
from globals import bot
import settings
from utility import *


async def start_game(ctx, *lista):
    roles = open('Postacie.txt', 'w')
    gracze = list(get_player_role().members)
    guild = get_guild()
    member = get_member(ctx.author.id)
    if globals.current_game != None:
        await ctx.send("Musisz najpierw zakończyć trwającą grę, użyj `&end`.")
        return
    if len(lista) != len(gracze):
        await ctx.send(
            "Błędna liczba postaci. Oczekiwano {}, Otrzymano {}".format(
                len(gracze), len(lista)))
        return

    globals.current_game = Game()

    lista_shuffled = list(lista)
    shuffle(lista_shuffled)

    c = "\nPostacie:\n"
    roles.write("Postacie:\n")
    globals.current_game.roles = lista
    for member, role in zip(gracze, lista_shuffled):
        try:
            await clear_nickname(member, ctx)
            await member.create_dm()
            await member.dm_channel.send(
                """{}\nWitaj, jestem cyfrowym przyjacielem Manitou. Możesz wykorzystać mnie aby ułatwić sobie rozgrywkę. Jako gracz masz dostęp m.in. do następujących komend:
`&help` pokazuje wszystkie dostępne komendy
`&postać <nazwa postaci>` pokazuje opis danej postaci
`&żywi` przedstawia postaci, które biorą udział w grze
{}
Twoja postać to:\n{}""".format(settings.RULLER, settings.RULLER,
                               postacie.get_role_details(role, role)))
        except discord.errors.Forbidden:
            await ctx.send(
                "Nie można wysłać wiadomości do {}\nGra nie została rozpoczęta".format(
                    get_nickname(member.id)))
            globals.current_game = None
            return
        globals.current_game.add_pair(member, role)
    globals.current_game.make_factions(lista)
    for member in sorted(gracze, key=lambda m: get_nickname(m.id).lower()):
        c += "{};\t{}\n".format(get_nickname(member.id),
                                globals.current_game.player_map[member].role)
        k = lambda m: get_nickname(m.id)
        roles.write("{}\t{}\n".format(get_nickname(member.id),
                                      globals.current_game.player_map[
                                          member].role))
        # gracz i rola muszą byc oddzielone przecinkiem, wtedy przy wklejaniu w excela się oddzielają komórki
    try:
        roles.close()
        await send_to_manitou(c)
        with open("Postacie.txt", 'rb') as fp:
            await send_file_to_manitou(discord.File(fp,
                                                    'Postacie {}.txt'.format(
                                                        datetime.datetime.now() + datetime.timedelta(
                                                            hours=2))))
        os.remove("Postacie.txt")
    except discord.errors.Forbidden:
        await ctx.send(
            "Nie można wysłać wiadomości do Manitou\nGra nie została rozpoczęta"
        )
        globals.current_game = None
        return
    await bot.change_presence(activity=discord.Game("Ktulu"))
    for channel in get_guild().text_channels:
        if channel.category_id == settings.FRAKCJE_CATEGORY_ID:
            await channel.send(settings.RULLER)
    team = postacie.print_list(lista)
    await get_glosowania_channel().send("""Rozdałem karty. Liczba graczy: {}
Gramy w składzie:{}""".format(len(lista), team))


def if_game():
    return globals.current_game != None
