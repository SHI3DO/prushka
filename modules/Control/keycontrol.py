def inputkey(inx):
    if inx == "z":
        f = open("./resources/runtime/chat_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "0":
            f.close()
            f = open("./resources/runtime/chat_screen.txt", 'w', encoding='UTF-8')
            f.write("1")
        else:
            f.close()
            f = open("./resources/runtime/chat_screen.txt", 'w', encoding='UTF-8')
            f.write("0")

        f.close()

    if inx == "c":
        f = open("./resources/runtime/options_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "0":
            f.close()
            f = open("./resources/runtime/options_screen.txt", 'w', encoding='UTF-8')
            f.write("1")
        else:
            f.close()
            f = open("./resources/runtime/options_screen.txt", 'w', encoding='UTF-8')
            f.write("0")

        f.close()
