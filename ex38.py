ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not ten things in that list. Let's fix that. Oh My Gooodness, what do wer do? Here is what we does:")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl",
"Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoaaaaaaaaaaa FANCY!!!!!!!!
print(stuff.pop())
print(''.join(stuff)) # NANI SO COOOOOL!!!!!!!!!!1
print('#'.join(stuff[3:5])) # WOWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
