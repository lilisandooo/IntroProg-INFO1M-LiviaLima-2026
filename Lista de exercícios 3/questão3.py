#exercício Maratona de animes
print("Hmm que tédio, acho que vou fazer uma maratona de animes. Tô sem nada para fazer mesmo. quer assistir comigo?")
anime = input("Agora.. temos que decidir qual assistir... \n Naruto (1) \n One Piece (2) \n Dragon Ball (3)? \n ")
while anime != "1" and anime != "2" and anime != "3":
    print("Então né... não sei se você sabe, mas só temos essas opções de animes. Bora escolher uma dessas três opções, por favor?")
    anime = input("Agora.. temos que decidir qual assistir... \n Naruto (1) \n One Piece (2) \n Dragon Ball (3)? ")
if anime == "1":
    print("Sim! Eu amo Naruto, é uma ótima ideia!")
    eps = int(input("Ah, mas quantos episódios a gente assiste? Uns... "))
    if eps <= 0:
        print("Eita, você não quer assistir nada? Que chato, né... Bora assistir pelo menos 1 episódio, vai!")
    elif eps <= 720:
        tempo = eps * 23
        if tempo <= 60:
            print(f"Então bora assistir {eps} episódios de Naruto, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de Naruto. Mas o tempo passa mais rápido doque parece.")
            print(f"Iiixi,que maratonista fraco! Dá nem 1 hora de maratona, só {tempo} minutos. Bora assistir mais uns episódios, vai!")
        elif tempo <= 180:
            print(f"Então bora assistir {eps} episódios de Naruto, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de Naruto. Foi um tempo divertido, mas poderia ser mais...")
            print(f"ehhh, só isso? Que rápido. Pensei que iríamos tipo... MARATONAR! Sabe, isso dá só {tempo/60:.2f} horas... mas tá valendo, bora assistir mais uns episódios, vai!")
        elif tempo <= 300:
            print(f"Então bora assistir {eps} episódios de Naruto, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de Naruto. Demorou uma eternidade.")
            print(f"WOOOW, SIM! Ahh, isso que eu chamo de maratona! Você tem noção que isso dá {tempo/60:.2f} horas de maratona?! Chega cansei, bora ver a luz do sol, se é que ele ainda está de pé!")
        else:
            print(f". . . você tá foragido da polícia que não sai de casa?! VAI VER A LUZ DO SOL, CARA! Você vai assistir {tempo/60:.2f} horas de maratona?! Isso é um ABSURDO!")
    else:
        print("Eita, você quer assistir mais episódios do que existem?! Tá é doido KKKKKKKK.")
elif anime == "2":
    print("Isso vai demoras uma eternidade... masss tá valendo, eu amo One Piece!")
    eps = int(input("Ah, mas quantos episódios a gente assiste? Tem milhões KKKKKK. bora assistir uns... "))
    if eps <= 0:
        print("Eita, você não quer assistir nada? Que chato, né... Bora assistir pelo menos 1 episódio, vai!")
    elif eps <= 1175:
        tempo = eps * 23
        if tempo <= 60:
            print(f"Então bora assistir {eps} episódios de One Piece, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de One Piece. Mas o tempo passa mais rápido doque parece.")
            print(f"Iiixi,que maratonista fraco! Dá nem 1 hora de maratona, só {tempo} minutos. Bora assistir mais uns episódios, vai!")
        elif tempo <= 180:
            print(f"Então bora assistir {eps} episódios de One Piece, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de One Piece. Foi um tempo divertido, mas poderia ser mais...")
            print(f"ehhh, só isso? Que rápido. Pensei que iríamos tipo... MARATONAR! Sabe, isso dá só {tempo/60:.2f} horas... mas tá valendo, bora assistir mais uns episódios, vai!")
        elif tempo <= 300:
            print(f"Então bora assistir {eps} episódios de One Piece, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de One Piece. Demorou uma eternidaaaade, ainda mais com os episódios flashbacks que tem.")
            print(f"WOOOW, SIM! Ahh, isso que eu chamo de maratona! Você tem noção que isso dá {tempo/60:.2f} horas de maratona?! Chega cansei, bora ver a luz do sol, se é que ele ainda está de pé!")
        else:
            print(f". . . você tá foragido da polícia que não sai de casa?! VAI VER A LUZ DO SOL, CARA! Você vai assistir {tempo/60:.2f} horas de maratona por acaso?! Isso é um ABSURDO!!!")
    else:
        print("Eita, você quer assistir mais episódios do que existem?! Tá é repreendido KKKKKKKK.")
else:
    print("Dragon Ball?! Nunca assisti, mas ouvi falar que é muito bom! Bora ver se é mesmo, né? KKKKK")
    eps = int(input("Ah, mas quantos episódios a gente deveria assistir? Talvez uns... "))
    if eps <= 0:
         print("Eita, você não quer assistir nada? Que chato, né... Bora assistir pelo menos 1 episódio, vai!")
    elif eps <= 1175:
        tempo = eps * 23
        if tempo <= 60:
            print(f"Então bora assistir {eps} episódios de Dragon Ball, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de Dragon Ball. Mas o tempo passa mais rápido doque parece.")
            print(f"Iiixi,que maratonista fraco! Dá nem 1 hora de maratona, só {tempo} minutos. Bora assistir mais uns episódios, vai!")
        elif tempo <= 180:
            print(f"Então bora assistir {eps} episódios de Dragon Ball, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de Dragon Ball. Foi um tempo divertido, mas poderia ser mais...")
            print(f"ehhh, só isso? Que rápido. Pensei que iríamos tipo... MARATONAR! Sabe, isso dá só {tempo/60:.2f} horas... mas tá valendo, bora assistir mais uns episódios, vai!")
        elif tempo <= 300:
            print(f"Então bora assistir {eps} episódios de Dragon Ball, vai ser daora!")
            print(f"Vocês assistem os {eps} episódios de Dragon Ball. Até que foi legal.")
            print(f"WOOOW, SIM! Ahh, isso que eu chamo de maratona! Você tem noção que isso dá {tempo/60:.2f} horas de maratona?! Chega cansei, bora ver a luz do sol, se é que ele ainda está de pé!")
        else:
            print(f". . . você tá foragido da polícia que não sai de casa?! VAI VER A LUZ DO SOL, CARA! Você vai assistir {tempo/60:.2f} horas de maratona por acaso?! Isso é um ABSURDO!!!")
    else:
        print("Eita, você quer assistir mais episódios do que existem?! Tá é repreendido KKKKKKKK.")
    