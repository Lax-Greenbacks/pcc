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

#12/15

halo.sort() #sorts list into alphabetical
print(halo)

halo.sort(reverse=True) #reverse alphabetical
print(halo)

halo.reverse() #does list in reverse order
print(halo)

print(len(halo)) #shows length of list

