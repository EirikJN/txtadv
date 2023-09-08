hp = 100

def rom_1():
    global hp

    print("HP:", hp )

    print("Du står nå i rom 1")
    valg = input("Velg A for rom 2, velg B for rom 3")
    if valg == "A":
        rom_2()
    if valg == "B":
        rom_3()

def rom_2():
    global hp

    print("Du står nå i rom 2")
    hp -= 30
    print("HP: ", hp )

    valg = input("Velg A for rom 1, velg B for rom 3")
    if valg == "A":
        rom_1()
    if valg == "B":
        rom_3()

def rom_3():
    global hp

    print("Du står nå i rom 3")
    hp += 15
    print("HP:", hp )

    valg = input("Velg A for rom 1, velg B for rom 2")
    if valg == "A":
        rom_1()
    if valg == "B":
        rom_2()

    if hp <= 0:
        print("god natt")

