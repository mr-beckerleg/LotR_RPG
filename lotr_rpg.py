import random

wizard = "Wizard"
elf = "Elf"
human = "Human"
dwarf = "Dwarf"
hobbit = "Hobbit"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dwarf_hp = 200

wizard_damage = 100
elf_damage = 75
human_damage = 50
dwarf_damage = 75

dragon_hp = 300 + (random.randrange(25, 200))
dragon_damage = 50

while True:
    print(f'''
    1)   {wizard}
    2)   {elf}
    3)   {human}
    4)   {dwarf}
    5)   Surrender''')
    character = input("Choose your character: ")
    if character == "1" or character == "Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage * (random.randrange(1, 3))

        break
    if character == "2" or character == "Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage * (random.randrange(1, 3))
        break
    if character == "3" or character == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage * (random.randrange(1, 3))
        break
    if character == "4" or character == "Dwarf":
        character = dwarf
        my_hp = dwarf_hp
        my_damage = dwarf_damage * (random.randrange(1, 3))
        break
    if character == "5" or character == "Surrender":
        print("The coward has fled at the sight of the Dragon")
        quit()
    print("Unknown Character")

print(f'''You have chosen the Character:{character}
 
Health  = {my_hp}
Damage  = {my_damage}
''')

while True:
    my_damage = my_damage + (random.randrange(-25, 50))
    dragon_hp = dragon_hp - my_damage
    print(f'''The {character} damaged the Dragon!
Dragon's Health is now: {dragon_hp}''')
    if dragon_hp <= 0:
        print(f'''The Dragon has LOST the battle!

        YOU WON!!!''')
        break
    dragon_damage = dragon_damage + (random.randrange(-25, 50))
    my_hp = my_hp - dragon_damage
    print(f'''The Dragon damaged {character}!
{character}'s Health is now: {my_hp}''')
    if my_hp <= 0:
        print(f'''{character} has LOST the battle!
        
        YOU LOST!''')
        break
#    play_again = input("Play again?")
#        if play_again == "yes" or play_again == "Yes"

