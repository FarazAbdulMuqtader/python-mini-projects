import re

def clean_text(message):
    convert_lowercase=message.lower()
    print("Lowercase: ", convert_lowercase)
    special_chars=r"[@,./&^%$#]"
    txt=re.sub(special_chars, "", convert_lowercase)
    print("Special characters removed: ", txt)
    words=txt.split()
    print("Words: ", words)
    word_count=len(words)
    print("Word count: ", word_count)
    word_data=[]
    for i in range(len(words)):
        dict={"word":words[i], "count":words.count(words[i])}
        if dict not in word_data:
            word_data.append(dict)
    print("Word data: ", word_data)


message=str(input("Write multi-line statements: "))
clean_text(message)