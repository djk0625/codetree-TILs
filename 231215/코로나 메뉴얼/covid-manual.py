a, b = input().split()
c, d = input().split()
e, f = input().split()

if (a == "Y" and int(b) >= 37):
    if(c == "Y" and int(d) >= 37) or (e == "Y" and int(f) >= 37):
        print("E")
    else:
        print("N")

else:
    if(c == "Y" and int(d) >= 37) and (e == "Y" and int(f) >= 37):
        print("E")
    else:
        print("N")