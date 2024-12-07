meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BOT": "Alguien malo en un juego",
            "IA": "Inteligencia Artificial",
            "GGS": "Una muy buena partida",
            }


word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("esta palabra no esta disponible")
