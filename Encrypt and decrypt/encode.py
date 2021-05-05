def encrypt(txt,shift):
    en_msg=""
    for letter in txt:
        if letter!=' 'and letter!='!'and letter!='.'and letter!="'"and letter!='%'and letter!='^'and letter!="&"and letter!='*'and letter!='('and letter!=')'and letter!='_'and letter!='-'and letter!='+'and letter!='/'and letter!=';'and letter!='"'and letter!='<'and letter!=">"and letter!=','and letter!='?'and letter!="'\'"and letter!='~'and letter!='`':
            conv_char=ord(letter)
            new_char=conv_char+shift
            en_msg+=chr(new_char)
        else:
            en_msg+=letter
    return en_msg