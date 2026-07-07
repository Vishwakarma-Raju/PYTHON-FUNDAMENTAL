p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "click this"
p4 = "Subscribe this"

msg = input("Enter your comment: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg) ):
    print("This comment is a spam")
else:
    print("This comment is not spam ")