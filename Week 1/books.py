total = 0
counter = 0

book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
total += book1_price
counter+=1
print("Book name: %s , book price: %d " %(book1_name, book1_price))

book2_name = "Learn You a Haskell"
book2_price = 0
total += book2_price
counter+=1
print("Book name: %s , book price: %d " %(book2_name, book2_price))

book3_name = "The Healthy Programmer"
book3_price = 50
total += book3_price
counter+=1
print("Book name: %s , book price: %d " %(book3_name, book3_price))

book4_name = "Code Complete"
book4_price = 60
total += book4_price
counter+=1
print("Book name: %s , book price: %d " %(book4_name, book4_price))

book5_name = "The Pragmatic Programmer"
book5_price = 20
total += book5_price
counter+=1
print("Book name: %s , book price: %d " %(book5_name, book5_price))

book6_name = "Pro Git"
book6_price = 0
total += book6_price
counter+=1
print("Book name: %s , book price: %d " %(book6_name, book6_price))

book7_name = "Introduction to Algorithms"
book7_price = 80
total += book7_price
counter+=1
print("Book name: %s , book price: %d " %(book7_name, book7_price))

book8_name = "Concrete Mathematics"
book8_price = 100
total += book8_price
counter+=1
print("Book name: %s , book price: %d " %(book8_name, book8_price))
print()

priceForLastTwo = book7_price + book8_price
print('If you take "%s" and "%s", you will end paying %d instead of %d'
      %(book7_name, book8_name, priceForLastTwo - (0.25 * priceForLastTwo), priceForLastTwo))

print("Total sum of books: %d" % total )
print("Total count of books: %d" % counter )
print()

maxBook = 5
availableSets = 6
print("The maximum number of books you could take for your budget is %d."% maxBook)
print('You coud always get our free books: "%s" and "%s"'%(book6_name,book2_name))

print("For the remaining part, you have to pick from %d remaining sets" %availableSets)
print()
print('First set: "%s", "%s" and "%s"'%(book1_name,book3_name,book4_name ))
print('Second set: "%s", "%s" and "%s"'%(book1_name,book3_name,book5_name))
print()
print('Third set: "%s", "%s" and "%s"'%(book3_name,book1_name,book8_name ))
print('Fourth set: "%s", "%s" and "%s"'%(book5_name,book1_name,book4_name))
print()
print('Fifth set: "%s", "%s" and "%s"'%(book3_name,book5_name, book7_name))
print('Sixth set: "%s", "%s" and "%s"'%(book7_name,book3_name, book1_name  ))
print()
 
