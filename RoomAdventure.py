#################################################################################################################################################
# Name: Sadiksha Lamsal
# Date: 5/20/2025
# Description: This program is a text-based escape game with a graphical interface using Tkinter which immerses players in a mysterious mansion, where every room holds hidden clues, 
# puzzles, and items; moving through the mansion, interacting with the surroundings, and collecting together the story will lead to win or death
#################################################################################################################################################

from tkinter import *
from tkinter import simpledialog
import os

class Room:
    def __init__(self, name, image, locked = False, keyType = None):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []
        self.grabbablesDescriptions = []
        self.locked = locked
        self.keyType = keyType

    # accessor and mutator for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    # accessors and mutators for image
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    # accessor and mutator for exits
    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self,value):
        self._exits = value

    # accessor and mutator for items
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self,value):
        self._items = value

    # accessor and mutator for grabbables
    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self,value):
        self._grabbables = value

    # accessor and mutator for grabbablesDescriptions
    @property
    def grabbablesDescriptions(self):
        return self._grabbablesDescriptions

    @grabbablesDescriptions.setter
    def grabbablesDescriptions(self,value):
        self._grabbablesDescriptions = value

    # accessor and mutator for locked 
    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self,value):
        self._locked = value

    # accessor and mutator for keyType
    @property
    def keyType(self):
        return self._keyType

    @keyType.setter
    def keyType(self,value):
        self._keyType = value

    # adds an exit to a room
    # the exit is a string 
    # the room is an instance of the room
    def addExit(self, direction, room):
        self.exits[direction] = room # append the exit and room to the appropriate dictionary

    # the addItem function takes two strings:
    # first = item, second = some description of the item
    def addItem(self, item, description):
        self.items[item] = description
    
    # adds a grabbable item and its description to the room
    # something in the room that can be carried out
    def addGrabbable(self, item, description):
        self.grabbables.append(item)
        self.grabbablesDescriptions.append(description)

    # deletes a grabbable item from the room
    def delGrabbable(self,item):
        index = self.grabbables.index(item)
        del self.grabbables[index]
        del self.grabbablesDescriptions[index]

    # returns a string description of the room
    def __str__(self):
        s = f"You are in the {self.name}\n"

        # add items to the string
        s+= "You see: "

        for item in self.items: 
            s += item + " "
        if len(self.items) == 0: # makes sure that you see: section is not left empty 
            item = "nothing here"
            s += item + " "

        s += "\n"

       #add the exit to the string
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s
    
# the game class
# iherits from the Frame class of Tkinter 
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent)

    # creates the room
    def createRooms(self):
        r1 = Room("utilityRoom", "utilityRoom.png", True, "utility_key")
        r2 = Room("livingRoom", "livingRoom.png", True, "crowbar")
        r3 = Room("kitchen", "kitchen.png")
        r4 = Room("bedroom", "bedroom.png")
        r5 = Room("office", "office.png", True, "office_key")
        r6 = Room("library", "library.png", True, "code") 

        # the final escape room
        escape = Room("outside", "outside.png", True, "key")

        # creates hallway
        h1 = Room("hallway", "hallway.png")

        # customize r1 (utility room)
        r1.addExit("north", h1)
        r1.addItem("shelves", "filled with cleaning supplies, safety goggles, and trash bags; a hidden key labeled 'OFFICE' lies camouflaged among the clutter")
        r1.addItem("tool_box", "contains a wrench and a variety of other tools, perfect for repairs")
        r1.addItem("ladder", "a tall wooden ladder, sturdy and perfect for reaching high places")
        r1.addGrabbable("wrench", "a rusty wrench with chipped teeth, not much use now")
        r1.addGrabbable("ladder", "a sturdy wooden ladder")
        r1.addGrabbable("office_key", "small key labeled 'Office', hidden in the chaos")

        # customize r2 (livingRoom)
        r2.addExit("east", h1)
        r2.addItem("sofa", "a comfortable sofa, looks brand new but has seen better days")
        r2.addItem("tv", "a shattered flat-screen TV, glass fragments scattered across the floor")
        r2.addItem("tea_table", "a wooden table with two missing cards from the bedroom resting atop")
        r2.addItem("wall_clock", "a wall-mounted clock, ticking softly with a faint creak")
        r2.addGrabbable("cards", "two playing cards: ♥4 and ♠A")

        # customize r3 (kitchen)
        r3.addExit("south", h1)
        r3.addItem("fridge", "a large, outdated fridge covered in worn-out fridge magnets, with a faded, folded note tucked inside")
        r3.addItem("dining_table", "a large wooden dining table, dimly lit with flickering candles")
        r3.addItem("countertop", "a long, marble countertop, used for food prep, now slightly cluttered")
        r3.addGrabbable("note", "Can you solve it?\nHIDDEN DEEP WITHIN THIS PLACE, \nA CLUE RESIDES IN PAGES' GRACE.\nSYMBOLS FAINT, YET SECRETS TRUE,\nA NUMBERED PATH FOR YOU TO PURSUE.\nSEEK THE BOOK, WHERE LINES ALIGN,\nA HIDDEN CLUE, FAINT YET FINE.\nWITHIN THE PAGES, YOU'LL FIND,\nTHE WAY TO WHERE SECRETS UNWIND.")

        # customize r4 (bedroom)
        r4.addExit("west", h1) 
        r4.addItem("mattress", "a neatly made bed, slightly lumpy, something feels hidden beneath the mattress.")
        r4.addItem("photoframe", "a strange-looking photo frame, slightly askew above the bed; maybe hints at more behind it")
        r4.addItem("drawer", "a small, easy-sliding drawer, holding an incomplete deck of cards; two cards seem missing — and IS THAT THE KNIFE?")
        r4.addGrabbable("knife", "a sharp, stainless steel knife with a sturdy handle")
        r4.addGrabbable("photoframe", "a hidden code '712' etched discreetly on the back") 
    
        # customize r5 (office)
        r5.addExit("north", h1)  
        r5.addExit("east", escape)
        r5.addItem("desk", "a large wooden desk with a computer and writing tools which were scattered carelessly on the surface")
        r5.addItem("cabinet", "a large, metal cabinet overflowing with documents, each labeled as 'file' followed by 3 digit number")
        r5.addGrabbable("file175", "oh! there's nothing here")
        r5.addGrabbable("file189", "oh! there's nothing here")
        r5.addGrabbable("file199", "as your fingers brush across the items, something glimmers—a faint big key—hidden beneath layers of files")
        r5.addGrabbable("file286", "oh! there's nothing here")
        r5.addGrabbable("file374", "oh! there's nothing here")
        r5.addGrabbable("key", " large, metallic gold key with slightly tarnished edges, hinting at its age and use")

        # customize r6 (library)
        r6.addExit("south", h1)
        r6.addItem("desk", "an old wooden desk, with worn writing supplies scattered about")
        r6.addItem("rack", "an antique wooden shelf with rows of books neatly arranged;\nfive books stand out, each with distinctive titles and markings\nbut its really high need something to reach there")  
                
        # customize h1 (hallway)
        h1.addExit("east", r4)
        h1.addExit("west", r2)
        h1.addExit("northeast", r6)
        h1.addExit("northwest", r3)
        h1.addExit("southeast", r5)
        h1.addExit("southwest", r1)
        h1.addItem("cabinet", "a small, wooden cabinet secured with a rusty padlock; key labeled 'UTILITY', hangs loosely on a hook")
        h1.addGrabbable("utility_key", "a small, old-fashioned key labeled 'UTILITY'")

        # set bedRoom as current room in the beginning of the game
        Game.currentRoom = r4

        # initializing the inventory and its item's descriptions
        Game.inventory = []
        Game.inventoryDescriptions = {}

    # sets up the GUI
    def setupGUI(self):

        # organize the GUI
        self.pack(fill = BOTH, expand = 1)

        # setup the user input at the bottom of the GUI
        Game.player_input = Entry(self, bg = "white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side = BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        img = None
        Game.image = Label(self, width = WIDTH//2, image=img)
        Game.image.image = img
        Game.image.pack(side = LEFT, fill = Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width = WIDTH // 2)

        # disable the Tkinter text by default
        Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
        Game.text.pack(fill = Y, expand = 1)
        text_frame.pack(side = RIGHT, fill = Y)
        text_frame.pack_propagate(False)

    # set the current room image
    def setRoomImage(self):
        if Game.currentRoom is None:
            # if dead, set the skull image
            image_file = os.path.join(os.path.dirname(__file__), "skull.gif")
        else:
            # otherwise grab the image for the current room
            image_file = os.path.join(os.path.dirname(__file__), Game.currentRoom.image)

        Game.img = PhotoImage(file=image_file)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img


    # sets the status displayed in the right side of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state = NORMAL)
        Game.text.delete("1.0", END)

        if not Game.intro_done:
            # if the intro is not done, dont show the room status
            Game.text.insert(END, status)

        elif (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert (END, "You are dead. The only thing you can do now is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status)

        Game.text.config(state = DISABLED)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current status
        self.setRoomImage()

        # initializing the intro_done variable
        Game.intro_done = False
        # initializing code_attempts variable 
        Game.code_attempts = 0
        # initiaizing max number of attempts variable
        Game.max_code_attempts = 3

        # the text to be displayed in the beginning of the game
        intro_text = (
            "Welcome to the world of VAULTED ESCAPE!!!\n"
            "You’ve awoken in a dimly lit bedroom.\n"
            + "=" * 49 + "\n"
            "You can only use 2 words at a time. Your options are:\n"
            "- go\n"
            "- take\n"
            "- look\n"
            "- use\n"
            "- examine (to inspect inventory items and their descriptions)\n"
            + "=" * 49 + "\n"
            "You feel something poking in the mattress. Something hidden.\n"
            "Perhaps something sharp might help uncover the truth beneath.\n"
            "The mansion has 6 interconnected rooms.\n"
            "Every action you take brings you closer to unraveling the mystery.\n"
            "Look closely at item descriptions—they hold important clues.\n"
            "Gather objects and piece together the story to escape.\n"
            "Trust your instincts, and the truth will be revealed.\n"
            + "=" * 49 + "\n"
            "Your journey begins now. Let the adventure unfold\n"
            "Type 'y' to continue..."
        )
        
        self.setStatus(intro_text)

    # processes the player's input
    def process (self, event):

        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, take, use or examine"

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)
        
        # handle the intro prompt before the game starts
        # wait for the player to type 'y' to begin the game
        if not Game.intro_done:
            # player confirmed; start the game
            if action.strip() == "y":
                Game.intro_done = True
                self.setRoomImage()
                self.setStatus("Game started. What do you want to do?")
            else:
                # prompt again until 'y' is entered
                self.setStatus("Type 'y' to begin your escape...")

            # clear input field and stop further processing
            Game.player_input.delete(0, END)
            return

        # if the player is dead 
        if (Game.currentRoom == None):
            Game.player_input.delete(0, END)
            return
        
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # deal with what they typed in, only if they have two words
        if (len (words) == 2):
            # isolate the verb and noun
            verb = words [0]
            noun = words[1]

            if (verb =="go"):
                response = "invalid exit" # update default response

                if noun in Game.currentRoom.exits:
                    next_room = Game.currentRoom.exits[noun]

                    if next_room is None:
                        Game.currentRoom = None
                        self.setRoomImage()
                        self.setStatus("You jumped to your death. GAME OVER.")
                        return
                
                    # check if the room trying to be accessed is locked or not
                    if next_room.locked:
                        response = f"The door has a {next_room.keyType}. Find it to unlock the door!"
                    # if the room is outside escape room
                    elif next_room.name == "outside":
                         Game.currentRoom = next_room
                         response = "You step into the fresh air... You WIN!"
                         Game.player_input.config(state=DISABLED)
                    # for all the other rooms
                    else:
                        Game.currentRoom = next_room
                        response = "Room changed."

            elif (verb == "look"):
                response = "I don't see that item."
                # Check if the player is looking at book5 which causes death
                if noun == "book5":
                    Game.currentRoom = None
                    self.setRoomImage()
                    self.setStatus("As you open the mysterious book, you realize too late that this is no ordinary book.\nYou feel a chilling presence, and before you can react, you are consumed by darkness.\nGAME OVER.")
                    return
            
                # Otherwise, check if the item exists in the room
                if noun in Game.currentRoom.items:
                    response = Game.currentRoom.items[noun]

            elif (verb == "take"):
                response = "That item can't be added into inventory."
            
                # check for valid grabbable items in the current room
                if noun in Game.currentRoom.grabbables:
                    Game.inventory.append(noun)

                    index = Game.currentRoom.grabbables.index(noun)
                    description = Game.currentRoom.grabbablesDescriptions[index]
                    Game.inventoryDescriptions[noun] = description

                    Game.currentRoom.delGrabbable(noun)

                    # Check if you want to match description from Room.items (optional)
                    if noun == "file199":
                        Game.inventory.append("key")
                        Game.inventoryDescriptions["key"] = "A small metallic key to the main door."
                        response = f"Item grabbed: {description}\nThe key has been added to your inventory!"
                    else:
                        response = f"Item grabbed: {description}"

            elif (verb == "examine"):
                response = "There is no such item in your inventory."

                # check if item is in inventory and has a description
                if noun in Game.inventory:
                    if noun in Game.inventoryDescriptions:
                        response = f"{noun}: {Game.inventoryDescriptions[noun]}"
                    else:
                        response = f"{noun}: No description available."

            elif verb == "use":
                response = f"You can't use the {noun} here."

                # knife in bedroom reveals crowbar
                if noun == "knife" and Game.currentRoom.name == "bedroom" and noun in Game.inventory:
                    response = "You successfully cut through the mattress; there is a crowbar beneath it."
                    Game.currentRoom.items["mattress"] = "A tattered mattress with torn fabric."
                    Game.inventory.append("crowbar")
                    Game.inventoryDescriptions["crowbar"] = "A slightly rusted crowbar with a well-worn grip."
                    Game.inventory.remove("knife")
                    del Game.inventoryDescriptions["knife"]

                # ladder in library reveals books and clues
                elif noun == "ladder" and Game.currentRoom.name == "library" and noun in Game.inventory:
                    response = "You use the ladder to reach the higher shelf. New books are now within reach."
                    Game.currentRoom.addItem("book1", "An elegant leather-bound book, slightly heavy but ordinary at first glance.")
                    Game.currentRoom.addItem("book2", "A tattered book with a loose page; scratches and faded notes hint at something more.")
                    Game.currentRoom.addItem("book3", "A slim paperback; a faded bookmark sticks out, whispering secrets.")
                    Game.currentRoom.addItem("book4", "A thick encyclopedia with a faint, musty smell.")
                    Game.currentRoom.addItem("book5", "A red cloth-bound journal; something odd about the cover.")
                    Game.currentRoom.addGrabbable("bookmark", "A faint number '199', barely visible.")
                    Game.inventory.remove("ladder")
                    del Game.inventoryDescriptions["ladder"]
                    Game.currentRoom.addGrabbable("page", "A torn page with a riddle pointing to a hidden file.")
                    Game.inventoryDescriptions["bookmark"] = "A faint number '199', barely visible."
                    Game.inventoryDescriptions["page"] = "A torn page with a riddle pointing to a hidden file."

                # unlocking rooms (keys, crowbar, final key)
                for direction, door in Game.currentRoom.exits.items():
                    if door and hasattr(door, "locked") and door.locked:
                        if noun in Game.inventory:
                            if noun == door.keyType:
                                door.locked = False
                                Game.inventory.remove(noun)
                                del Game.inventoryDescriptions[noun]
                                response = f"You unlocked the {door.name} with the {noun}!"
                                break
                            elif noun == "crowbar" and door.keyType == "crowbar":
                                door.locked = False
                                Game.inventory.remove("crowbar")
                                del Game.inventoryDescriptions["crowbar"]
                                response = f"You forced open the {door.name} with the crowbar!"
                                break
                            elif noun == "key" and door.keyType == "key":
                                door.locked = False
                                Game.currentRoom = door  # move player to escape room
                                self.setRoomImage()
                                response = f"You unlocked the {door.name} with the {noun}!"
                                Game.player_input.config(state=DISABLED)  # Disable input after win
                                break

                        # unlocking library with code
                        elif noun == "code" and door.keyType == "code":

                            code_input = simpledialog.askstring("Code Required", f"Enter 5-digit code to unlock (Attempts left: {Game.max_code_attempts - Game.code_attempts})")

                            if code_input is None:
                                response = "Code entry canceled."
                            elif len(code_input) == 5 and code_input.isdigit():
                                if int(code_input) == 71214:
                                    door.locked = False
                                    Game.code_attempts = 0  # reset for future uses
                                    response = "The padlock has been unlocked with the code!"
                                else:
                                    Game.code_attempts += 1
                                    response = "Incorrect code."
                            else:
                                Game.code_attempts += 1
                                response = "Invalid input. Enter a 5-digit number."

                            if Game.code_attempts >= Game.max_code_attempts and door.locked:
                                Game.currentRoom = None
                                self.setRoomImage()
                                self.setStatus("You failed to unlock the padlock in 3 attempts. You have died.")
                                return
                            
            # display the response on the right of the GUI
            # display the room's image on the left of the GUI
            # clear the player's input
            self.setStatus(response)
            self.setRoomImage ()
            Game.player_input.delete(0, END)


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)

# play the game
g.play()

# wait for the window to closes
window.mainloop()
                


