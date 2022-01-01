#Myles Barrett 12/9/2021

print("Not gonna say hello world cause that'd be cringe... oh wait")

cringe = "My name is Ivan"
print(cringe)

poop = "Lax Greenbax"
print(poop.upper()) #this kinda cool, idk how useful it is
print(poop.lower())

first_name = "myles"
last_name = "barrett"
full_name = f"{first_name} {last_name}" #doing maths
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

#12/10

math1 = 3*2
math2 = 3**2 #can do exponents like this. never knew this
print(math1)
print(math2)

math3 = 2+3*4 #python supports order of operations ex.
math4 = (2+3)*4
print(math3)
print(math4)

math5 = 4/2 #division always gives a float
math6 = 1+2.0 #even with whole numbers
print(math5)
print(math6)

num1 = 1_000_000 #can use underscores to make big number more readable
print(num1)

x, y, z = 1, 2, 3 #multiple assignments
print(x, y, z)

CONSTANT = 100 #book says constants that should never change to be written with all capitals. This is because python has no contant type

#chapter 3 starts here on page 33
pokemon = ['puff', 'pikachu', 'pichu'] #this is a list
print(pokemon[0]) #zero gives us first thing in list
print(pokemon[0].title()) #this makes it neat and uses capital p
print(pokemon[-1]) #-1 will always give u the last item in the list

pokemon[1] = 'mewtwo' #u can change the elements in a list
print(pokemon[1])

#12/14

pokemon.append('bulba') #can add things to lists like this
print(pokemon)

halo = [] #can add to empty list too
halo.append('chief')
halo.append('weapon')
halo.append('arby')
print(halo)

halo.insert(0, 'spark') #can add at specific place without replacing
print(halo)

del halo[0] #delete lists items like this
print(halo)

#12/18

halo.sort() #sorts list into alphabetical
print(halo)

halo.sort(reverse=True) #reverse alphabetical
print(halo)

halo.reverse() #does list in reverse order
print(halo)

print(len(halo)) #shows length of list

#12/19

halo.remove('arby') #how to remove items by value
print(halo)

gun = 'weapon' #removing by definition
halo.remove(gun)
print(halo)

pirates = ['peg', 'rum', 'eyepatch', 'parrot']
pirates.sort() #sorting like this is permanent in the code
print(pirates)

pirates.reverse() #simply reverses order of list
print(pirates)

for things in pirates: #this dont work right i dont get it
    print(pirates)

#12/20

for value in range(1, 5): # doesn't print the 5
    print(value)

even_numbers = list(range(2, 11, 2)) #printing the evens
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] #finding things with lists of numbas
print(min(digits))
print(max(digits))
print(sum(digits))

#12/30

rooster = ['egg', 'feather', 'hen', 'chick', 'omlet']
print(rooster[0:3]) #gets specific slice of a list
print(rooster[1:4]) #rember how the indexing works bruh
print(rooster[:4]) #list will default start to beginning
print(rooster[2:]) #this ones unique cause it will finish off the list
print(rooster[-3:]) #this one takes last 3 because of the -

people = ('john', 'matt', 'jo', 'jack', 'jeep') # looping in this slice
print("Here's the first 3 people in the list:")
for humans in people[:3]:
    print(humans.title())

my_foods = ['pizza', 'falafel', 'carrot cake'] #copying a list
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

dimensions = (200, 50) #this is a tuple, it uses ( ) instead of [ ]
print(dimensions[0])
print(dimensions[1])

#chapter 5 if statements

fruits = ['apple', 'banana', 'kiwi', 'peach']
for fruit in fruits:
    if fruit == 'kiwi':
        print(fruit.upper())
    else:
        print(fruit.title())

car = 'bmw'
print(car == 'bmw') #This shows true
print(car == 'audi') #This shows false
print(car == 'Bmw') #case sensitie (false)

answer = 20
if answer != 42:
    print("Not the correct answer.")

age = 19
print(age < 21) #true
print(age <= 21) #true
print(age > 21) #false
print(age > 15 and age < 33) #can do multiple (true)

toppings = ['mushrooms', 'salami', 'tomato']
print('mushrooms' in toppings) #checking stuff in a list (true)

admission = 12 #here some else if stuff
if admission < 4:
    print("Your admission cost is $0.")
elif admission < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

