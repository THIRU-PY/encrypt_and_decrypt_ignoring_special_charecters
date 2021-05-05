def decrypt_message(msg):
    de_key=int(input("\nEnter the Key number to decode:\t"))
    de_msg=""
    for letter in msg:
        if letter!=' 'and letter!='!'and letter!='.'and letter!="'"and letter!='%'and letter!='^'and letter!="&"and letter!='*'and letter!='('and letter!=')'and letter!='_'and letter!='-'and letter!='+'and letter!='/'and letter!=';'and letter!='"'and letter!='<'and letter!=">"and letter!=','and letter!='?'and letter!="'\'"and letter!='~'and letter!='`':
            conv_char=ord(letter)
            new_char=conv_char-de_key
            de_msg+=chr(new_char)
        else:
            de_msg+=letter
    return de_msg