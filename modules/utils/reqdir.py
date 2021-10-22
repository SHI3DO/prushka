def make():
    f = open("./resources/runtime/music_list.txt", 'w', encoding='UTF-8')
    f.close()

    f = open("./resources/runtime/options_screen.txt", 'w', encoding='UTF-8')
    f.write("0")
    f.close()

    f = open("./resources/runtime/chat_screen.txt", 'w', encoding='UTF-8')
    f.write("0")
    f.close()

    f = open("./resources/runtime/music_pnum.txt", 'w', encoding='UTF-8')
    f.write("0")
    f.close()

    f = open("./resources/runtime/mainscene_active.txt", 'w', encoding='UTF-8')
    f.write("0")
    f.close()