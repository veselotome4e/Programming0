from random import randint

n = int(input("Enter dice side: "))
player1_name = input("Enter player1 name: ")
player2_name = input("Enter player2 name: ")

player1_roll = randint(1,n)
print("%s rolls %d"%(player1_name,player1_roll))
player2_roll = randint(1,n)
print("%s rolls %d"%(player2_name,player2_roll))

if player1_roll == player2_roll:
    print("Both randoms are even")
elif player1_roll > player2_roll:
    print("%s wins!"%player1_name)
else:
    print("%s wins!"%player2_name)
    
