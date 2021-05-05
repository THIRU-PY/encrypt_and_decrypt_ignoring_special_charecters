def decrypt_after_encrypt(en_msg,shift):
    de_msg=""
    de_key=int(input("\nEnter the Shift key to decode:\t"))
    if de_key==shift:
        for letter in en_msg:
            if letter!=' 'and letter!='!'and letter!='.'and letter!="'"and letter!='%'and letter!='^'and letter!="&"and letter!='*'and letter!='('and letter!=')'and letter!='_'and letter!='-'and letter!='+'and letter!='/'and letter!=';'and letter!='"'and letter!='<'and letter!=">"and letter!=','and letter!='?'and letter!="'\'"and letter!='~'and letter!='`':
                conv_char=ord(letter)
                new_char=conv_char-de_key
                de_msg+=chr(new_char)
            else:
                de_msg+=letter
    return de_msg