def zahadka():
    LIFE=0
    while LIFE<7:
        print("Загадка 1: не песок, сладок")
        answer1 = input()
        if answer1.lower() == "сахар":
            print("Верно")

        else:
            print("Неверно")
            print(LIFE,"использовано попыток из семи для этой загадки")
        print("Загадка 2: коричневое, продолговатое, не тонет")
        answer2 = input()
        if answer2.lower() == "бревно":
            print("Верно")
            break
        else:
            print("Неверно")
            print(LIFE,"использовано попыток из семи для этой загадки")
        print("Загадка 3: не человек, чёрт")
        answer3 = input()
        if answer3.lower() == "Артемий":
            print("Верно")
            break
        else:
            print("Неверно")
            print(LIFE,"использовано попыток из семи для этой загадкиа")
            LIFE+=1
            if LIFE>=5:
                print("LIFE кончились")