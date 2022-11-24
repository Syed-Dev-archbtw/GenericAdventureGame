# Imports
import time
from PIL import Image
from os import name, system

# Functions VV

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# Code VV

print("Hello Adventurer!")
print("(If you get any option wrong the program will suicide)")
print("I see your a new fellow.")
a1 = input("Follow me! [Y/N]\n")
health = 100
exp = 0
inventory = []
if a1 == 'N':
    print("I see...")
    exit()
else:
    print("Ok!")
print("So first you walk in a forest, you see trees around you, you keep walking and get amazed by its beauty.")
print("It turns dark soon and then you realize you have to go back, only to realize your lost.")
print("")
print("What do you do?")
print("")
print("A: Build a shelter and try to survive. B: Find a cave to live in.")
print("C: Climb the trees and build a treehouse D: You just sleep where ever")
a2 = input("")
clear()
House = ""
if a2 == "A":
    House = "hut"
    print("You take sticks and stone and tree logs and assemble")
    print("them into a small hut")
    im = Image.open(r"pictures/hut.png")
    im.show()
    input("[Enter to continue] ")
    print("")
elif a2 == "B":
    House = "cave"
    print("you find a pretty large cave to live in and you decide to stay inside")
    im = Image.open(r"pictures/cave.png")
    im.show()
    input("[Enter to continue] ")
    print("")
elif a2 == "C":
    House = "treehouse"
    print("you find a short tree you can Climb and decide to build your treehouse ontop of it")
    im = Image.open(r"pictures/Screenshot from 2022-09-07 18-26-43.png")
    im.show()
    input("[Enter to continue] ")
    print("")
else:
    House = "non-existent house"
print("Now you have a house and even though its turning dark thanks to your "+ House +" You still feel comfy.")
print("You decide its time to sleep so you take some leaves and shrubury to assemble a bed in your "+ House)
print("You wake up in the morning and you feel hungry, what should you eat?")
print("A: Berries B: Meat")
a3 = input("")
clear()
food_eaten = ""
if a3 == "A":
    print("You go outside of your "+ House +" and search for some berries, you check if its poisoned")
    print("By feeding it to squirrels sure enough they were still alive, so you ate some berries as")
    print("a light snack and you feel pretty good after that.")
    food_eaten = "Fruit"
elif a3 == "B":
    print("You go hunting for some squirrels and you manage to trap and cook 4 squirrels, you ate them")
    print("all and you get all the energy you need.")
    food_eaten = "Meat"
else:
    print("ERROROROROORORO CRASHING!I")
    exit()
print("Now your full you decide to make a weapon to defend yourself")
print("You look around and decide to make a..")
print("A: Sword B: Bow C: Spear D: Club")
a4 = input("")
clear()
weapon = ""
attack_damage = 0
attack_damage_string = ""
if a4 == "A":
    weapon = "sword"
    attack_damage = 15
    print("You go around looking for materials to make a sword, you find a rock some sticks and some fiber.")
    print("You use the rock to sharpen the sticks and then you use the fiber to tie it all up.")
    print("TADA!! You have a wooden sword which has 15 attack damage")
elif a4 == "B":
    weapon = "bow"
    attack_damage = 10
    attack_damage_string = str(attack_damage)
    print("TADA!! You have a "+ weapon +" which has "+ attack_damage_string +" attack damage")
elif a4 == "C":
    weapon = "spear"
    attack_damage = 20
    attack_damage_string = str(attack_damage)
    print("TADA!! You have a "+ weapon +" which has "+ attack_damage_string +" attack damage")
elif a4 == "D":
    weapon = "club"
    attack_damage = 10
    attack_damage_string = str(attack_damage)
    print("TADA!! You have a "+ weapon +" which has "+ attack_damage_string +" attack damage")
else:
    print("ERROROROROORORO CRAAAAAAAAAAAAAAAASHINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
    exit()
print("Now that you have a "+ weapon +" you feel more safe adventuring outside,")
print("So you get outside of your "+ House +" and head in the woods.")
print("")
print("you hear some noise...")
time.sleep(2)
print("...")
time.sleep(3)
print("A bear attacks you!")
print("you dodge the first hit but its going to do another swipe")
print("What do you do?")
print("A: Fight B: Run away C: Tame it")
a5 = input("")
clear()
if a5 == "A":
    print("You use your "+ weapon +", you damaged the bear and it seems badly injured")
    print("but sadly you got a small scratch in the fight")
    print("-10 HP")
    health = health - 10
    health_str = str(health)
    print("You now have "+ health_str +" HP")
    print("What do you do?")
    print("A: Fight B: Run away")
    fighterinput = input('')
    if fighterinput == 'A':
        print("You go in for another strike and hit it in the eye!")
        print("It collapses and dies")
        print("+10 EXP")
        exp = exp + 10
        health_str = str(health)
        print("What do you do with its body??")
        print('A: Harvest Hide B: Harvest Meat')
        fighterinput = input('')
        if fighterinput == 'A':
            print('+1 Bear Hide!')
            inventory.append('Bear Hide')
        else:
            print("+1 Raw Bear Meat!")
            inventory.append('Bear Meat')
    else:
        print("You ran away..")
        print("No effect")
elif a5 == "B":
    print("You ran away..")
    print("No effect")
elif a5 == "C":
    if food_eaten == "Meat":
        print("You held out the dead cooked squirrel you made before..")
        time.sleep(2)
        print("The bear ignored it and lunged towards you, breaking your back thus dying. idiot")
        health = health - 100
        health_str = str(health)
        if health == 0:
            print("You died")
            exit()
        else:
            pass
    elif food_eaten == "Fruit":
        print("You hold out some berries you saved for later, the bear litteraly")
        print("ignored it and killed you, moron")
        health = health - 100
        health_str = str(health)
        if health == 0:
            print("You died")
            exit()
        else:
            pass
else:
    print("YOU IDIOTJGLKDJHOI UGIUSGF:HSPOI JCRASHING CRASHINGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    exit()


print("Now you dealt with that bear you decide to try and relocate society")
print("You...")
print("A: Follow a river till you find a town or city B: You make an sos sign hoping a plane flies over you")
a6 = input("")
clear()
chad = True
if a6 == "A":
    print("You find a river near your "+ House +" and you decide to follow it")
    time.sleep(3)
    print("A day passes")
    time.sleep(5)
    print("A week passes")
    time.sleep(4)
    print("3 weeks pass and you decide to exit(), your too tired to do anything so you sleep for the night")
    time.sleep(5)
    chad = True
elif a6 == "B":
    print("You collect some leaves and shrubury and use some flint and steel to burn the leaves")
    print("You sleep for the night")
    time.sleep(5)
    chad = False
else:
    print("ERROROROROROROOR CRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRASSSSSSSSSSSSSSSSSSSHHHHHHHHHHHHHHH")
    exit()
print("After returning back to your "+ House +" you decide to eat food, what will you do this time?")
print("A: Forage For Plants B: Hunt")
a7 = input("")
clear()
if a7 == "A":
    print("You forage for plants to eat and you find some bannanas and apples")
    food_eaten = "Fruit"
elif a7 == "B":
    print("You hunt down 1 cow because of your "+ weapon +".")
    food_eaten = "Meat"
else:
    print("l")
    exit()
time.sleep(3)
print("")
def lmao():
    im = Image.open("pictures/crashedcopter.png")
    im.show()
if chad == False:
    print("You hear helicopter blades, and then...")
    time.sleep(3)
    print("ITS A HELICOPTER!")
    time.sleep(1)
    print("finaly, saftey..")
    print("you get on and you sleep...")
    time.sleep(5)
    print("You hear alarms blaring")
    time.sleep(1)
    print("The captain is panicking")
    time.sleep(3)
    print("You faint from stress")
    print("It crashes, your the only survivor.")
    time.sleep(1)
    lmao()
    input("[Enter to Continue]")
    print("Seems like your in an abadoned city.")
    time.sleep(3)
    print("Here we go again.")
else:
    print("Uhh you got the normal ending you lived in the forest for your entire life.")
    exit()
print("")
print("Chapter 2 : The Abandoned City")
print("")
time.sleep(5)
print("You get out the helicopter and head to the nearest shelter seems to be an abandoned building.")
time.sleep(6)
print("You see inside there is a hotdog stand, the hotdogs are still warm and good-looking so you")
time.sleep(1)
print("eat some.")
print("")
time.sleep(4)
print("You see a broken brown door with blood stains, go in? [Y/N]")
a8 = input("")
clear()
def supersos():
    im = Image.open(r"pictures/deadhangingcorpse.png")
    im.show()
if a8 == "Y":
    supersos()
    print("You walk in to see a dead corpse...")
    time.sleep(2)
    input("[Enter to continue]")
    print("..")
    print("You see a table with a book on it, there is a puddle of blood next to it.")
    print("Open it? [Y/N]")
    chad = True
    a9 = input("")
    if a9 == "Y":
        im = Image.open(r"pictures/book.png")
        im.show()
        print("[Enter to continue]")
        print("")
        print("...")
        print("I think we should leave")
else:
    print("You ignore the door and walk past")

print("You walk up the stairs and you hear a childs scream in the distance.")
time.sleep(3)
print("You dont feel safe anymore.")
print("Maybe this is some sort of Nightmare?")
print("Anyway you continue")
print("You see millions of bloody foot prints on the floor")
print("All headed to a black door.")
print("Go in? [Y/N]")
a10 = input("")
clear()
def supersos():
    im = Image.open(r"pictures/doorttoanotherwoooooorld.png")
    im.show()
if a10 == "Y":
    supersos()
    print("You open the door only to see the room is missing. its gone? how?")
    input("[Enter to Continue]")
else:
    print("You ignore it and walk past")
if chad == True:
    print("Your scared of what might be in this building")
else:
    print("You have an unwary feeling about this building.")
time.sleep(1)
print("You decide to sleep in one of the apartment rooms which seemed normal")
time.sleep(3)
print("You wake up and walk in the kitchen, what should you cook/make?")
print("A: Salad B: Steak")
a11 = input("")
if a11 == "B":
    print("You cook a nice juicy steak and eat it.")
    food_eaten = "Meat"
else:
    print("You make a nice sald with some tomatos and lettuce.")
    food_eaten = "Fruit"
print("You walk out the building to find a MASSIVE lion.")
print("What do you do?")
print("A: Fight B: Run away")
a12 = input("")
clear()
if a12 == "A":
    print("You attack it with your "+ weapon +".")
    print("The lion loses -"+ attack_damage_string +".")
    print("What do you do?")
    print("A: Fight B: Run away")
    a13 = input("")
    if a13 == "A":
        if food_eaten == "Meat":
            print("You attack the lion but it dodges and attacks you.")
            print("-20 Hp")
            health = health +- 20
            health_str = str(health)
            print("You now have "+ health_str+".")
            print("But thankfully thanks to that steak you also land a critical hit on it too.")
            print("The lion loses -20 HP and runs away!")
            print("+20 EXP")
            exp = exp + 20
        else:
            print("You attack the lion but it dodges and attacks you.")
            print("-20 Hp")
            health = health +- 20
            health_str = str(health)
            print("You run away.")
else:
    print("You run away.")
print("You go back to your apartment room and wonder, What was THAT?!")
print("You decide just to sleep hoping that the lion looked big because of sleep deprivation.")
time.sleep(5)
print("You wake up")
print("You get up and go outside")
time.sleep(1)
print("You walk for 15 minutes and you see footprints, you decide to follow it.")
print("You see a MASSIVE exploded nuclear power plant.")
input("[Enter to Continue]")
im = Image.open(r"pictures/nuclearpowerplant.png")
im.show()
time.sleep(1)
print("You instantly run back to your apartment room and find a radio box.")
time.sleep(3)
print("You try to use it but you dont know how to.")
time.sleep(1)
print('You just choosE to sleep again.')
time.sleep(3)
print("You wake up in the morning confused and scared, if that exploded nuclear power plant was what caused that wierdly large animals..")
time.sleep(2)
print("Imagine what else it can do..")
if chad:
    print("Considering what we saw in that room.")
time.sleep(1)
print("You walk outside to the garden with a book.")
time.sleep(1)
print("It was the Diary of the wimpy kid book. Rodrick Rules.")
time.sleep(1)
print("It reminds you of your child hood..")
time.sleep(1)
if chad:
    clear()
    time.sleep(1)
    print(".")
    time.sleep(3)
    clear()
    print("..")
    time.sleep(3)
    clear()
    print("...")
    time.sleep(3)
    clear()
    print("BUT WHO CARES ABOUT THAT RIGHT?")
    time.sleep(0.1)
    clear()
print("You get up and remember what your doing here.")
time.sleep(3)
print("You start thinking...")
time.sleep(1.5)
print("What was the doors about?")
time.sleep(1.5)
print("Why were the animals mutated so bad?")
time.sleep(1.5)
print("What even happened here?")
time.sleep(2.5)
clear()
print("Well, i'll find that out later.")
time.sleep(2)
print('For now i need to find out how this radio box.')
time.sleep(2)
print('You fumble with the switches and the knobs until you can hear a human voice in the whitenoise!')
time.sleep(2)
print('"Make sure to buy your greens -d---d--d"')
time.sleep(2)
print('Nevermind, its just an AD')
time.sleep(2)
print('You hear a loud roar outside your room.')
time.sleep(2)
print('You grab a knife and peak through the door.')
im = Image.open(r"pictures/hallway.png")
im.show()
sussy = input('[Enter to continue]')
time.sleep(2)
clear()
print('Wha-')
time.sleep(0.5)
print('What is that?')
time.sleep(2)
print('I.. have never seen anything like that before.')
time.sleep(2)
print('No such animals have such bright eyes.')
time.sleep(2)
if chad:
    print('Is, that what they were talking about?')
    time.sleep(2)
    print('Is THAT, what caused the.. ')
    time.sleep(2)
    print('Well i have to focus right now.')

print('What do you do?')
print('A: Pick a gun and fight B: Run')
charinput = input('')
clear()
if charinput == 'A':
    print('You run back into the room and look into your night stand drawer.')
    time.sleep(2)
    print('You run back into the hall and point your gun into the darkness.')
    time.sleep(2)
    print("There's nothing there.")
    time.sleep(2)
    print('Where did it go?')
    time.sleep(2)
    print('You go back into your room and decide its a good time to sleep.')
    time.sleep(2)
    print('You wake up hungry.')
else:
    print('You get out the room and book it to the elevator.')
    time.sleep(2)
    print('You then realise that you litteraly stay in an abadoned')
    print('city.')
    time.sleep(2)
    print('You run down the stairs instead and find a bathroom.')
    time.sleep(2)
    print('You go in one and lock the bathroom stall.')
    time.sleep(2)
    print('You wait for so long you fall asleep inside the stall.')
    time.sleep(2)
    clear()
    print('You wake up.')
    time.sleep(2)
    print('You go back into your room.')
    time.sleep(2)
    print('You search for anything that had changed.')
    time.sleep(2)
    print('.')
    time.sleep(2)
    print('Nothing.')
time.sleep(2)
print('You find that there is no food to eat.')
time.sleep(2)
try:
    if inventory[0] == 'Bear Meat':
        print('But then you remember that you have some meat from')
        time.sleep(0.5)
        print('That bear you killed.')
        time.sleep(2)
        print('You go to the kitched and cook the meat.')
        time.sleep(2)
        print('You ate it and you feel satisfied.')
        food_eaten = 'Meat'
except:
    print('What do you do?')
    print('A: Steal meat from the grocery store. ')
    print('B: Steal some greens from the farm.')
    charinput = input('')
    clear()
    if charinput == 'A':
        print('You go out of the apartment building and find a grocery store')
        time.sleep(2)
        print('Suprisingly everything looks like it has been maintained.')
        time.sleep(2)
        print('The food is still fresh, the lights are working, there is electricity ')
        time.sleep(2)
        print('Whatever')
        time.sleep(2)
        print('You go to the meat aisle and steal some meat.')
        time.sleep(2)
        print('You come back to your room and cook some nice food.')
        time.sleep(2)
        food_eaten = 'Meat'
    else:
        print('You go to your local farm and steal some potatos.')
        time.sleep(2)
        print('You boil them and you eat them.')
        time.sleep(2)
        print('You feel good.')
        food_eaten = 'Not-Meat'

time.sleep(2)
print('You hear a loud bomb go off outside.')
time.sleep(2)
print('You walk out your room to see the same creature which you last night.')
time.sleep(2)
print('Your sick of this.')
time.sleep(1.5)
print('This creature has been harrasing you for far too long.')
time.sleep(1.5)
print('You pull out the pistol from your pocket and aim towards the darkness.')
time.sleep(1.5)
print('You fire mercilessly.')
time.sleep(1.5)
print('You open your eyes and you see nothing in the darkness in front of you.')
time.sleep(2)
clear()
print('Is it dead?')
time.sleep(1.5)
print('Have you dealt with that nightmare?')
time.sleep(1.5)
print('You feel a light breathing on your neck.')
time.sleep(1.5)
print('Your heart drops at what you just realised.')
clear()
bosshealth = 300
cntr = 0
while bosshealth > 0:
    clear()
    time.sleep(1)
    if health == 0:
        print('You failed. you died')
        exit()
    print('                                            BOSS FIGHT                                                 ')
    time.sleep(0.1)
    print('                                       "LIGHTS"     300 HP                                             ')
    time.sleep(0.25)
    print('What do you do?')
    time.sleep(0.5)
    print('A: Fight')
    input()
    clear()
    if cntr == 0:
        print('You shoot its eye! dealing 30 damage!')
        bosshealth = bosshealth - 30
        time.sleep(1.8)
        print('A loud deafening ring followed by a bright light plays.')
        time.sleep(1.8)
        print('You see hundreds of eyes!')
        time.sleep(1.8)
        print('Each one charges at you, punting you towards the wall.')
        print('-20 HP')
        health = health - 20
        cntr = cntr + 1
    elif cntr == 1:
        print('You get up clutching your shoulder.')
        time.sleep(1.8)
        print('You look at it, and you shoot it twice again, dealing 60 damage!')
        bosshealth = bosshealth = 60
        time.sleep(1.8)
        print('This time sparing no time and grabing an axe piercing its pure black body!')
        time.sleep(1.8)
        print('dealing 40 damage!')
        bosshealth = bosshealth - 40
        time.sleep(1.8)
        print('You go in for another swing but it grabs your hanf and picks you up.')
        time.sleep(1.8)
        print('You try to reach in for the gun you left on the floor but it throws you')
        time.sleep(0.5)
        print('on the side of the wall and uses its claws to scratch your chest')
        time.sleep(1.8)
        print('Suprisingly it didnt hurt, -20 HP')
        health = health - 20
        cntr = cntr + 1
    elif cntr == 2:
        print('You decide you want to finish this.')
        time.sleep(1.8)
        print('You see a flash light on the floor and the axe.')
        time.sleep(1.8)
        print('You run towards it and you repeatedly wacking your axe on to its body')
        time.sleep(1.8)
        print('The axe creating a big wound and using the light to burn its skin.')
        time.sleep(1.8)
        clear()
        print('.')
        time.sleep(2)
        clear()
        print('..')
        time.sleep(2)
        clear()
        print('...')
        time.sleep(2)
        clear()
        print('KILLING IT IN THE PROCESS!')
        time.sleep(1.8)
        print('+100 xp')
        exp = exp + 100
        bosshealth = bosshealth - 270
    time.sleep(1.5)
clear()
time.sleep(2)
print('You go back into your room collapsing on to your bed, asleep')










# this game good
clear()
print('Credits')
print('')
print('Me (obviously)')
print('My brother for some GFX')
print('My friend for chapter 1 houses GFX')
input('')
