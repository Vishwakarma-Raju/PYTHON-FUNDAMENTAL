# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l
    
# l = ["Raju","Rajjo","Jojo","aj"]

# print(rem(l,"aj"))


def rem(l,word):
    n = []
    for item in l:
        if not( item == word):
            n.append(item.strip(word))
    return n

l = ["Raj","Rajjo","Jojo","aj"]

print(rem(l,"aj"))