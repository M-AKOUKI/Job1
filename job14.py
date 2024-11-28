x = int(input("Entrez un entier supérieur à 0 (N):"))
print("la table de",x,"est :")
for i in range(1,x+1):
    x += 1
    for i in range(11):
        print(i,"x",x,"=",i*x)