def CeasarCipher(strParam,num):
    new=""
    for i in range(len(strParam)):
        char=strParam[i]
        if(char.isupper()):
            new=new +chr((ord(char) + num - 65)%26+65)
        else:
            new = new + chr((ord(char) + num - 97) % 26 + 97)
    return new
print(CeasarCipher(input(),input()))