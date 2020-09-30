Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text=input()

text2=()
word=[]

final_text=[]

print(text)

n=len(text)
m=0 
l=0

while m<n:
    text2=(text[m])
    if text[m].isspace()==False:
        word.append(text2)
    else:
        final_text.append(word)
        word.clear()
        text2=()

    m=m+1



print(final_text)
