#Variables
health = 3
sword = False
first_key = False
second_key = False
wardrobe_open = False
door_open = False

#0. Game start
print("\033[1mWelcome to: Labyrinth escape\033[0m")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
user_name = input("Enter your name: ")
#1. Room before labyrinth
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"\033[1mScene 1: The Room\033[0m"
    f"\nSo, {user_name}, you are woke up in an uыnfamiliar room.\n"
    "The air is stale, and only a narrow window near the ceiling lets in a faint beam of light.\n"
    "You feel dizzy for a moment, then slowly get to your feet.\n"
    "\033[1mLooking around you sees:\033[0m\n"
    "– an old wooden \033[1m[table]\033[0m in the corner,\n"
    "– a tall antique \033[1m[wardrobe]\033[0m, slightly open,\n"
    "– and a heavy metal \033[1m[door]\033[0m with no visible handle.")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
while not door_open:
    user_input = str(input(f"!->> {user_name}, what we should check?: ")).lower()
#Items interaction
    #Interacting with the table
    if user_input == "table":
        if not first_key:
            first_key = True
            print(f"{user_name}: 🗝️ You found a small rusty key in the table drawer.")
        else:
            print(f"\n{user_name} You've already checked the table.")
        #interacting with the wardrobe
    elif user_input == "wardrobe":
        if first_key and not wardrobe_open:
            wardrobe_open = True
            second_key = True
            sword = True
            print(f"{user_name} You unlocked the wardrobe with the rusty key.")
            print(">> Inside, you found a shiny 🔑 key and... a 🗡️ sword!")
        elif not first_key:
            print(f"{user_name} The wardrobe is locked. You might need a key.")
        else:
            print(f"{user_name} You already open the wardrobe and took everything that was inside")
    #interacting with the door
    elif user_input == "door":
        if second_key and not door_open:
            door_open = True
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f">> Congrats {user_name}: 🔓The silver key fits perfectly. The door opens with a creak...")
            print("You step out into the maze beyond.")
            print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
        elif first_key:
            print(f"{user_name} You try the rusty key... but it doesn't fit this lock.")
        else:
            print(f"{user_name} The door is locked and has no handle. Only a keyhole is visible.")
    else:
        print(f"{user_name} Please select from available items to interact:\n"
            "- [table]"
            "- [wardrobe]"
            "- [door]")
#2. Inside the maze
enemy_dead = False
environment_listed = False
left_attempt = False
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\033[1mScene 2: The Corridor\033[0m\n"
        "You step through the heavy metal door… and find yourself in a narrow stone corridor.\n"
        "The air is colder here. Damp.\n"
        "Your footsteps echo off the walls, and somewhere far away, water drips with maddening rhythm.\n"
        "Faint torchlight flickers ahead, casting long shadows that dance across ancient bricks.\n"
        "There’s no turning back now — only forward.\n"
        "At the far end, the path splits into two")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\033[1mPossible actions:\033[0m")
print("- listen")
print("- go left")
print("- go forward")

while not enemy_dead:
    user_input = str(input(f"!->> {user_name} what will you do?: ")).lower()
    if user_input == "listen":
        if not environment_listed:
            environment_listed = True
            print("- To the \033[1mleft\033[0m, faint scratching and squeaking echo through the air. A cold draft carries the sharp stench of rot.\n"
                    "- Straight \033[1mahead\033[0m, you hear slow, heavy breathing... like stone grinding against stone.")
        else:
            print(f"Hey {user_name}, you already listen, and there is what we have:"
                    "- To the \033[1mleft\033[0m, faint scratching and squeaking echo through the air. A cold draft carries the sharp stench of rot.\n"
                    "- Straight \033[1mahead\033[0m, you hear slow, heavy breathing... like stone grinding against stone.")
    elif user_input == "go left" or user_input == "left":
        if not environment_listed:
            print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
            print("You push the creaky door on the left and step into pitch darkness.")
            print("The air is thick. You can’t see anything — not even your own hands.")
            print("As you take the first step forward...")
            print("CLICK.")
            print("A mechanism triggers beneath your foot.")
            print("The door behind you slams shut with a metallic thud.")
            print("You spin around and try to force it open... but it's locked tight.")
            print("Then you hear them — a thousand tiny feet skittering in the dark.")
            print("The sound grows louder. The rats are coming.")

            health = 3
            while health >0:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"\nJust like in all games, here you have {health} live{'s' if health > 1 else ''} left.")
                print("Choose how to fight the swarm:")
                print("- swing sword")
                print("- punch")
                print("- kick")
                combat_actions = input(f"{user_name} What will be your combat action? >> ").lower()

                if combat_actions == "swing sword":
                    print("X-> You slash through the air — some rats squeal and fall, but more take their place.")
                elif combat_actions == "punch":
                    print("X-> You punch into the swarm… it's useless. Your hand is bleeding.")
                elif combat_actions == "kick":
                    print("X-> You kick blindly in the dark, sending a few flying. It buys you a moment, nothing more.")
                else:
                    print("X-> In panic, you fumble and waste a moment...")
                health -=1
            print("\nThey overwhelm you. The pain is sharp, fast, everywhere.")
            print("Your vision fades as the swarm devours you in the dark.")
            print("\033[1m-=GAME OVER=-\033[0m")
            exit()
        else:
            environment_listed = False
            print("You listen first and hear the squeaking — something doesn’t feel right.")
            print("You decide not to go in just yet.")

    elif user_input == "go forward" or user_input == "forward":
        if environment_listed:
            print("You stepped into the room, from which you had previously heard heavy breathing... like stone grinding against stone.\n" 
                    "You already understood that behind this door, the old guardian golem will meet you.\n"
                    "As you carefully observe the golem, you notice a small red ruby embedded in its chest — a weak spot. \n"
                    "! > If you strike it with precision, your sword will pierce through its core, taking the golem down with a single blow.\n"
                    "Timing is everything — [hit the ruby] and end the fight swiftly.")
        if not environment_listed:
            print(
                "You step into the dark room, immediately feeling an unusual atmosphere — the air is heavy, filled with a mysterious echo.\n"
                "The light from the flickering torches trembles on the walls, casting ominous shadows that move in rhythm with your breath.\n"
                "In the corner of the room, a massive pile of stones looms before you — unnaturally large, as if the earth itself had cast it there.\n"
                "Nothing seems out of place, but something about its form gives off an unsettling feeling.")
            print(
                "You take a step forward, and suddenly, under the weight of your foot, the pile of stones begins to stir.\n"
                "The rocks shift with a loud rumble, and from beneath them emerges a gigantic figure — a golem, massive and terrifying, made of roughly hewn stone blocks that don’t seem to fit together properly.\n"
                "Its eyes, resembling glowing embers, flicker as it starts to move.")
            print(
                "The golem rises, cracking as if its body were nothing more than a mosaic of stone pieces, precariously held together.\n"
                "In its hands, it holds enormous fists, ready to crush anything in its path.\n"
                "His ruby heart glowing and you understood that you need to fight")

        health = 3
        golem_lives = 3
        while golem_lives > 0:
            print(f"\nJust like in all games, here you have {health} live{'s' if health > 1 else ''} left.")
            print("You can [strike] the golem from the [left] or [right] to break through its stone armor, each hit weakening its defense.\n"
                  "Alternatively, look for a vulnerable spot and thrust your sword precisely to deal a devastating blow.")
            combat_actions = input(f"!->> {user_name} What will be your combat action? >> ").lower()
            if combat_actions == "hit the ruby" or combat_actions == "strike the ruby":
                golem_lives = 0
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"!->> Congrats {user_name}, you defit the old guardian golem, now you can move forward and try to escape the maze")
                print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n")
            elif combat_actions == "strike left" or combat_actions == "left" or combat_actions == "hit left":
                golem_lives -= 1
                print(f"! >> You hit the golem really hard.\nGolem live = {golem_lives}")
            elif combat_actions == "strike right" or combat_actions == "right" or combat_actions == "hit right":
                golem_lives -=1
                print(f"! >> Golem didn't expect this move, you hit him. Golem live = {golem_lives}")
            elif combat_actions == "strike" or combat_actions == "strike golem" or combat_actions == "hit golem" or combat_actions == "hit":
                golem_lives -=1
                print(f"! >>You moving like a lightning, and you are hitting like a thunder. Golem lives = {golem_lives}")
            else:
                print("X >> In panic, you fumble and waste a moment...")
                health -= 1
                if health == 0:
                    print("\nGolem overwhelm you.")
                    print("Your vision fades as the swarm devours you in the dark.")
                    print("\033[1mGAME OVER\033[0m")
                    exit()
        enemy_dead = True
    else:
        print(f"\n\033[1m{user_name}, note the possible actions is:\033[0m")
        print("- listen")
        print("- go left")
        print("- go forward")

#3. Maze level 2
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\033[1mScene 3: The Room of Suspicious Choices\033[0m\n")
print("You step into a new chamber… and instantly regret it.")
print("The air here smells like mystery, old socks, and possibly cheese.")
print("Before you stand three doors, each one radiating 'Pick me!' energy like a bad dating app bio.")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\nDoor 1 is \033[1mbright red\033[0m — bold, aggressive, and probably compensating for something.")
print("Door 2 is \033[1mblue\033[0m — calm and trustworthy… or pretending to be.")
print("Door 3 is \033[1mgreen\033[0m — the color of nature, frogs, and terrible decisions.")

print("\nEach door has a note taped to it. You squint and read:")

print("\n[1] 'The door to freedom is not green.'")
print("[2] 'This door is a lie.'")
print("[3] 'The red door leads to death.'")

print("\nYou sigh. Logic puzzles. Your old enemy.")
correct_door = False
while not correct_door:
    print("\033[1mPossible actions:\033[0m")
    print("- Door 1") #Red door - 'The door to freedom is not green.'
    print("- Door 2") #Blue door - 'This door is a lie.' <Correct>
    print("- Door 3") #Green door - 'The red door leads to death'.
    print("- PANIC")
    print("- Cry")

    user_input = str(input(f"!->> {user_name} What will you do?: ")).lower()
    if user_input in ["Door 1", "door 1", "Door1", "door1", "1"]:
        print(f"🚪 Door 1 — 'Too Confident. Too Wrong.'")
        print("You walk in with your head held high, full of confidence."
                "The room seems empty… until suddenly:"
                "!->> You feel a chill... and then you hear a faint 'meow'."
                "A massive, hyper-realistic cat with laser eyes appears — because, why not?")
        print("Honestly, I can't even imagine what you need to do with this. In any case, here is some option")
        print("- Pet the cat")
        print("- Run!")
        print("- Fight")
        user_input = str(input(f"{user_name} what will you do?: ")).lower()
        if user_input in ["pet the cat", "Pet the cat", "Pet", "petthecat"]:
            print("The cat accepts your affection... then vaporizes you anyway")
            print("\033[1mGAME OVER\033[0m")
        elif user_input in ["Run!", "Run", "run", "RUN"]:
            print("You try. You fail. You are now cat food.")
            print("\033[1mGAME OVER\033[0m")
        elif user_input in ["Fight", "fight"]:
            print("Really? With what — your student debt?")
            print("\033[1mGAME OVER\033[0m")
        else:
            print("X >> In panic, you fumble and waste a moment...")
            print("Kitty doesn't wait, he just ate you")
            print("\033[1mGAME OVER\033[0m")
        exit()
    elif user_input in ["Door 2", "door 2", "Door2", "door2", "2"]:
        correct_door = True
        print("\nYou reach for the handle of the blue door...")
        print("It creaks open like it rehearsed for this moment all its life.")
        print("A soft breeze hits your face. Real, fresh air. Is that... freedom?")
        print("You take a cautious step forward, then another.")
        print("No traps. No riddles. No talking goats demanding passwords.")
        print("Just a quiet stone hallway that leads to — wait for it —")
        print("\n\033[1m🌄 THE EXIT.\033[0m")
        print("You blink at the sunlight. It’s real.")
        print("Somewhere, epic victory music starts playing (in your head).")
        print("You laugh, cry a little, and whisper to no one in particular:")
        print(f"'{user_name}, you magnificent survivor… you did it.'")
        print("\n\033[1m🏆 CONGRATULATIONS!\033[0m")
        print("You have officially escaped the Labyrinth.")
        print("…With minimal trauma. Probably.")
        print("\nThanks for playing. Now go touch some grass.")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        exit()
    elif user_input in ["Door 3", "door 3", "Door3", "door3", "3"]:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\033[1mScene ???: The Endless Room\033[0m\n")
        print("You walk through the green door. Bold move. Green usually means go, right?")
        print("At first glance, it’s just… a room. A completely ordinary, absurdly unremarkable room.")
        print("Stone walls. A floor. A ceiling. More motivational posters than you asked for.")
        print("\"Believe in yourself!\" — one says, aggressively cheerful.")
        print("\"Mistakes are proof you’re trying.\" Yeah? Tell that to your sword arm.")
        print("You take a few steps forward... the room doesn't change.")
        print("You turn around... the door is gone. Replaced by another poster that says:")
        print("\033[3m‘Success is just failure that kept trying.’\033[0m")
        print("You’re starting to feel like you’re inside a screensaver. Or your old therapist’s office.")
        while True:
            tries = 0
            print("\n\033[1mPossible actions:\033[0m")
            print("- walk")
            print("- turn around")
            print("- scream")
            print("- give up")
            print("- read poster")
            user_input = input(f"!->> {user_input} What do you do? ").lower()
            if user_input in ["exit", "door", "quit", "Exit", "Door", "Quit"]:
                print("A door appears where there was none. You're free.")
                break
            elif user_input in ["walk", "Walk"]:
                print("You walk. One step. Two steps. The room looks... exactly the same.")
                print("You're either stuck in a time loop or this is an IKEA showroom.")
            elif user_input in ["turn around", "Turn around", "Turn Around", "turnaround", "turn", "Turn"]:
                print("You spin dramatically like you're in a music video.")
                print("The door is still gone. But hey, at least you're well choreographed.")
            elif user_input in ["scream", "Scream", "SCREAM"]:
                print("You scream. Loud. Powerful. Primal.")
                print("Your echo screams back: 'Try harder.'")
                print("Wow. Even your echo is judging you now.")
            elif user_input in ["give up", "Give Up", "Give up", "giveup", "Giveup"]:
                print("You drop to your knees and mutter, 'I give up.'")
                print("The posters begin to flicker. One falls off the wall, revealing... a hidden \n\033[1mdoor\033[0m?!")
                print("Looks like giving up is *finally* productive.")
            elif user_input in ["read poster", "Read poster", "readposter"]:
                print("It says: ‘You’re doing great!’ You feel gaslit.")
            elif tries == 5:
                print("You've been wandering a while… Maybe try thinking differently?")
            elif tries == 6:
                print("What is missing in this room?")
            elif tries == 7:
                print("The room sighs. So do you.")
            elif tries == 8:
                print("Good, please - Try to [exit] or found the [door]")
            else:
                print("Motivational posters surround you. They are judging.")
    elif user_input in ["PANIC", "Panic", "panic", "PANIC!", "Panic!", "panic!"]:
        print("You panic. Wildly. Arms flailing. Breathing like you just saw your exam schedule.")
        print("The room watches in silence. Unimpressed.")
        print("One of the posters falls off the wall in embarrassment.")
    elif user_input in ["Cry", "cry", "CRY"]:
        print("You sit down and start to cry. Loudly. Theatrically.")
        print("One of the posters falls off the wall. Another one says:")
        print("\"Tears are just sweat from the soul. Keep going!\"")
        print("You now regret being emotionally vulnerable in front of paper.")
    else:
        print("You try something… unexpected.")
        print("The room pauses. Even the posters look confused.")
        print("One of them slowly peels off the wall and whispers, 'No.'")