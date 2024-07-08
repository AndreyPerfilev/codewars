alph={'a':1, 'b':2,'c':3, 'd':4,'e':5, 'f':6, 'g':7, 'h':8, 'i':9,
 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16,'q':17,
 'r':18, 's':19, 't':20,'u':21,'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
alphabet_position="The narwhal bacons at midnight."
alph_numbers=''
for i in alphabet_position:
    i=i.lower()
    m=alph.get(i)
    if i in alph :
        alph_numbers+=str(m)+" "
    elif i==alphabet_position[-2]:
        alph_numbers += str(m)
print(str(alph_numbers))
print("20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
print(alphabet_position[-1])



