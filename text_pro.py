from ast import While


def sentene_maker(p):
    introgatives = ("how","why","what","when","where")
    c= p.capitalize()
    if p.startswith(introgatives):
        return "{}?".format(c)
    else:
        return "{}.".format(c)
'''
print(sentene_maker("how are you"))
'''
result=[]
while True:
     print("when you are done write \end")
     user_input = input("Say something: ")
     if user_input == "\end" :
         break
     else:
         result.append(sentene_maker(user_input))

print(" ".join(result))


