from math import sqrt
# MAIN
def Main():
    print("ENCRYPTER 1.0")
    print("------------------------------")
    while True:
        print("What tool do you want to use?")
        print("0 - Exit")
        print("1 - Encrypter")
        print("2 - Decrypter")
        print("------------------------------")
        UserDecision = input("")
        print("------------------------------")
        if UserDecision == "0":
            return
        elif UserDecision == "1":
            
            UserText = GetUserText()
            print(f"Encrypted text: {Encrypt(UserText)}")
        elif UserDecision == "2":
            UserText = GetUserText()
            print(f"Decrypted text: {Decrypt(UserText)}")
        else:
            print("Wrong Input!")
        print("------------------------------")
# MAIN FUCNTIONS
def Encrypt(text):
    ASCII_Numbers_list = Text_To_ASCII_Numbers_List(text)
    Encrypted_ASCII_Numbers_List = ASCII_Number_Encryption(ASCII_Numbers_list)
    Encrypted_Text = ASCII_Numbers_To_Text(Encrypted_ASCII_Numbers_List)
    return Encrypted_Text
def Decrypt(text):
    ASCII_Numbers_list = Text_To_ASCII_Numbers_List(text)
    Decrypted_ASCII_Numbers_list = ASCII_Number_Decryption(ASCII_Numbers_list)
    Decrypted_Text = ASCII_Numbers_To_Text(Decrypted_ASCII_Numbers_list)
    return Decrypted_Text

# TEXT TO NUM AND NUM TO TEXT
def Text_To_ASCII_Numbers_List(text):
    ASCII_Numbers_list = list(str(ord(x)) for x in text)
    return ASCII_Numbers_list
def ASCII_Numbers_To_Text(Encrypted_ASCII_Numbers_List):
    EncryptedText = ""
    for Encrypted_ASCII_Number in Encrypted_ASCII_Numbers_List:
        EncryptedText += chr(Encrypted_ASCII_Number)
    return EncryptedText


#MATH OPERATIONS (ENRYPT, DECRYPT)
def ASCII_Number_Encryption(ASCII_Numbers_list):
    Encrypted_ASCII_Numbers_List = []
    for ASCII_num in ASCII_Numbers_list:
        NewASCII_num = ((int(ASCII_num) ** 2) + 13) * 4
        Encrypted_ASCII_Numbers_List.append(NewASCII_num)
    return Encrypted_ASCII_Numbers_List
def ASCII_Number_Decryption(ASCII_Numbers_List):
    Decrypted_ASCII_Numbers_List = []
    for ASCII_num in ASCII_Numbers_List:
        NewASCII_num = int(sqrt((int(ASCII_num)//4)-13))
        Decrypted_ASCII_Numbers_List.append(NewASCII_num)
    return Decrypted_ASCII_Numbers_List

# GET INPUT TEXT
def GetUserText():
    print("Enter your text")
    print("------------------------------")
    UserText = input("")
    print("------------------------------")



    return UserText


if __name__ == "__main__":
    Main()

