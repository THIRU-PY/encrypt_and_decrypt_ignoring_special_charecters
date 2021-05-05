#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from encode import encrypt
from decode_encoded_msg import decrypt_after_encrypt
from decode_msg import decrypt_message




choice=input("\nEnter encode to encrypt and decode to decrypt:\t")

en_msg=""
de_msg=""


if choice=="encode":
    mesg=input("\nType your message:\t")
    if mesg==""or mesg==" ":
        print("\nThere is no message to Encrypt")
    else:
        key=int(input("\nEnter the Shift key:\t"))
        en_msg=encrypt(mesg,key)
        print("\nThe encrypted message is:\t"+en_msg)
        choice2=input("\nDo you want to decrypt the message (y/n)\t").lower()
        if choice2=='y':
            de_msg=decrypt_after_encrypt(en_msg,key)
            print("\nThe Decoded message is:\t"+de_msg)
elif choice=="decode":
    mesg=input("\nType your message:\t")
    if mesg!="" and mesg!=" ":
        dec_msg=decrypt_message(mesg)
        print("\nThe Decrypted message is:\t"+dec_msg)
    else:
        print("\nThere is no message to decrypt")
else:
    print("\nWrong Choice")

