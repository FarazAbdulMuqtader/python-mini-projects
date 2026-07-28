txt=str(input("Write multi-line statements: "))

convert_lowercase=txt.lower()

special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
if(punc:=convert_lowercase.replace(special_chars, "")):
    print(punc)

