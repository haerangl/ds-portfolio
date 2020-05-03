import sys
import os
import time # For delaying actions during interaction with user in commandline.
import random # Choose reactions from the cat randomly 
import numpy as np 
from ascii_images import * # This is a separate module that contains ASCII art

class Friend:
    """Albert or Flipper"""
    def __init__(self, name, happiness, sleepiness, asleep, location, previously_asleep):
        self.name = name
        self._happiness = happiness
        self._sleepiness = sleepiness
        self._asleep = asleep
        self._location = location
        self._previously_asleep = previously_asleep
        self._sleep_turn_counter = 0 
    
    def __str__(self):
        return self.name 
    
    def __repr__(self): # For easy debugging, create __repr__ to print all the attributes 
        return  ', \n'.join("%s: %s" % item for item in vars(self).items())
    
    # Happiness ---------------------------
    
    @property
    def happiness(self):
        return self._happiness
    
    @happiness.setter
    def happiness(self, happiness_factor): 
        self._happiness += happiness_factor
        
        # Make sure the happiness level ranges from 0 to 100.
        if self._happiness > 100:
            self._happiness = 100
        elif self._happiness < 0:
            self._happiness = 100
    
    # Sleepiness ---------------------------
    
    @property
    def sleepiness(self):
        return self._sleepiness
    
    @sleepiness.setter
    def sleepiness(self, sleepiness_factor): 
        self._sleepiness += sleepiness_factor 
        
        # Make sure the sleepiness level ranges from 0  to 100.
        if self._sleepiness > 100:
            self._sleepiness = 100
        elif self._sleepiness < 0:
            self._sleepiness = 0
            
        if self._sleep_turn_counter >=3: # If Friend has been sleeping for three turns, wake them up.
            self._sleepiness = 0
    
    # Asleep ---------------------------
    
    @property
    def asleep(self):
        if self._asleep:
            return "asleep"
        else:
            return "awake"
    
    # I wanted to use a decorator method, but that wouldn't allow me to pass in more than one argument.
    # So going to setter method instead. 
    def set_asleep(self):
        # Determine the likelihood that the Friend will be asleep
        # based on the known happiness level and the sleepiness level.
        self._previously_asleep = self._asleep 
        
        if self._sleep_turn_counter >=3: # If Friend has been sleeping for three turns, wake them up.
            self._asleep = False
            self._sleep_turn_counter = 0
        
        else:

            true_point = self._happiness + self._sleepiness + self._asleep 
            false_point = (100 - self._happiness) + (100 - self._sleepiness) 

            true_prob = true_point / (true_point + false_point)
            false_prob = false_point / (true_point + false_point)

            # Then, using this as a probability, determine whether the friend is sleepy.
            if self.name == "Albert" and self._location.albert_okay_to_sleep == False:
                print("Albert really wants to take a nap, but can't sleep in the", self._location, 
                      ", because he is not a cat. So he stays awake")
                self._asleep = False 

            else:
                self._asleep = np.random.choice([True, False], p=[true_prob, false_prob])

                # If Flipper is not in sight, then do not show her new asleep status.
                if flipper.location != albert.location and self.name == "Flipper":
                    pass 
                else:
                    if self._previously_asleep:

                        if self._asleep: # previously sleeping and still sleeping
                            print(self.name, "stays", self.asleep)

                        else: # previously sleeping but not awake 
                            print(self.name, "is", self.asleep)

                    else: # previously awake and now asleep

                        if self._asleep:
                            print(self.name, "fell", self.asleep)

                        else: # previously awake and still awake
                            pass 

            if self._asleep:
                self._sleep_turn_counter += 1
            else:
                self._sleep_turn_counter = 0

                    
     
    # Location ---------------------------
    
    @property
    def location(self): 
        return self._location
    
    @location.setter
    def location(self, new_location): 
        self._location = new_location 
    
        
class Activity:
    '''These are the activities that Albert and Flipper can do.
    Depending on the location and each Friend's happiness/sleepiness level, an activity is chosen randomly.
    Activity will interact with the Friend class to modify each Friend's happiness, sleepiness, or asleep status.
    '''
    def __init__(self, friend, verb, description, happiness_mean, happiness_sd, sleepiness_sd, sleepiness_mean):
        self._friend = friend
        self._verb = verb
        self._description = description
        
        
        self._previous_happiness = self._friend.happiness 
        self._happiness = self._friend.happiness 
        self._happiness_mean = happiness_mean
        self._happiness_sd = happiness_sd
        
        self._previous_sleepiness = self._friend.sleepiness 
        self._sleepiness = self._friend.sleepiness 
        self._sleepiness_mean = sleepiness_mean
        self._sleepiness_sd = sleepiness_sd
    
    def __str__(self):
        return "{} decided to {}.\
        \nprevious happiness: {:,.2f}\
        \ncurrent happiness: {:,.2f}\
        \ndescription: ".format(self._friend, self._verb, self._previous_happiness, self._happiness, self._description)
    
    def __repr__(self): # For easy debugging, create __repr__ to print all the attributes 
        return  ', \n'.join("%s: %s" % item for item in vars(self).items())
    

    def set_happiness(self):
        self._previous_happiness = self._friend.happiness 
        
        # Calculate the happiness factor. There is a random component to it. 
        self._happiness_factor = round(np.random.normal(self._happiness_mean, self._happiness_sd), 2)
        
        # Change happiness of the Friend instance by feeding it the happiness factor.
        self._friend.happiness = self._happiness_factor
        if self._happiness_factor > 0:
            self._happier = "happier."
        elif self._happiness_factor < 0:
            self._happier = "less happy."
        else: 
            self._happier = "no happier or less happy than before."
        
        # Then pull that happiness level into activity 
        self._happiness = self._friend.happiness 
        
        if self._friend.name == "Flipper" and flipper.location != albert.location:
            pass
        else:
            print(self._friend, "decided to", self._verb, "-", np.random.choice(self._description),
                 "As a result,", self._friend, "became", self._happier
                 )
    
    def set_sleepiness(self):
        self._previous_sleepiness = self._friend.sleepiness 
        
        # Calculate the sleepiness factor. There is a random component to it. 
        self._sleepiness_factor = round(np.random.normal(self._sleepiness_mean, self._sleepiness_sd), 2)
        
        # Change sleepiness of the Friend instance by feeding it the sleepiness factor.
        self._friend.sleepiness = self._sleepiness_factor
        
class Locations:
    """Albert and Flipper can go to all these places."""
    
    def __init__(self, name, albert_okay_to_sleep):
        self._name = name 
        self._albert_okay_to_sleep = albert_okay_to_sleep
    
    def __str__(self):
        return self._name 
    
    @property
    def albert_okay_to_sleep(self):
        return self._albert_okay_to_sleep
    
        
    
def consequences(user_direction):
    """After the user tells Albert to move or stay, these actions follow.
    1. Albert & Flipper either move to a location or stays in the current location.
    2. If Albert has found Flipper in that location, they may interact with each other.
       Otherwise, Albert does a solo activity. 
    """

    
    
    # Albert either stays or moves to a new location, based on user input.
    if user_direction in ["move", "m"]:
        if albert.asleep == "asleep":
            print("Albert can't go elsewhere because he is currently asleep.")
            print("So he stays in the", albert.location) 
        
        else:
            new_albert_location = np.random.choice(all_locations)

            while albert.location == new_albert_location:
                new_albert_location = np.random.choice(all_locations)

            # gotta set the location of the Albert class to the new location 
            albert.location = new_albert_location # move - new location. 

            print("Albert decides to go to the", albert.location)
    
    else: # automatically, this means user_direction in ["stay", "s"]:
        print("Albert stays in the", albert.location) # No change to curr_location 
        
    
    
    # Flipper either stays or moves to a new location, regardless of user input.
    if flipper.asleep == "awake":
        flipper.location = np.random.choice(all_locations)
    
    
    # Is Flipper here? 
    flipper_here = (albert.location == flipper.location)
    
    if albert.asleep == "asleep": # Print various types of descriptions to show that Albert is sleeping.
        albert_activity = a_continue_sleep 
        
        if flipper_here:
            print(np.random.choice(flipper_pic)) # Show a picture of Flipper
            
            if flipper.asleep == "asleep": # Messages if Flipper is sleeping
                flipper_activity = f_continue_sleep 
                print(np.random.choice(["Look at the two friends, fast asleep.",
                                       "Flipper is napping on Albert's lap. The two are very relaxed."]))
            else:
                flipper_activity = np.random.choice(flipper_interactive_activity_options)
                
                print(np.random.choice(["Flipper is here, but Albert doesn't notice, because he's asleep.",
                                       "Flipper meowed. Albert has a happy dream.",
                                       "'When will Albert wake up?' Flipper wonders."]))

        else:
            flipper_activity = np.random.choice(flipper_interactive_activity_options + [f_fall_asleep])
            print(np.random.choice(["Flipper is nowhere in sight.",
                                   "No cats here, but Albert doesn't know, because he's fast asleep",
                                   "No fluffy felines here."]))
            
    else: # Print descriptions to show that Albert is up.
        # Even though Flipper is not here and we can't see her, I'd like her to do an activity somewhere else.
        flipper_activity = np.random.choice(flipper_interactive_activity_options + [f_fall_asleep])
        
        if flipper_here:
            albert_activity = np.random.choice(albert_interactive_activity_options)
            
            print(np.random.choice(flipper_pic))
            print(np.random.choice(["Oh! Hello, Flipper. There you are.",
                                   "Hello, Flipper. Are you sleepy? I am always a little bit sleepy.",
                                   "Hi Flipper, here you are. You are so cute.",
                                   "Flipper is right here. Let's grab some treats."]))

        else:
            albert_activity = np.random.choice(albert_solo_activity_options)
            
            print(np.random.choice(["Sigh... Flipper is not here.",
                                   "'Flipper, where are you?' Albert whispers. No answer.",
                                   "No fluffy felines here."]))

        
    
    # If Albert found Flipper here, Albert and Flipper interact with each other.
    flipper_activity.set_happiness()
    flipper_activity.set_sleepiness()
    
    albert_activity.set_happiness()
    albert_activity.set_sleepiness()
    
    flipper.set_asleep()
    albert.set_asleep()

    # Print the following for testing. 
#     print()
#     print()
#     print(albert_activity)
#     print(albert.__repr__)
    
#     print()
#     print(flipper_activity)
#     print(flipper.__repr__)
    
    print("\n==========================================================================")
        
    
###############################################################
# Let's get started                                           #
###############################################################

# Locations
front_porch = Locations("Front Porch", False)
bedroom = Locations("Bedroom", True)
office = Locations("Office", True)
backyard = Locations("Backyard", False)

all_locations = [front_porch, bedroom, office, backyard]

# Our friends 
albert = Friend(name = "Albert", 
                happiness = 50,
                sleepiness = 60, 
                asleep = False, 
                location=office,
                previously_asleep = False)

flipper = Friend(name = "Flipper", 
                 happiness = 50, 
                 sleepiness = 50, 
                 asleep = False, 
                 location=office,
                 previously_asleep = False
                 )

# activities
a_work = Activity(friend = albert, 
                  verb = "work",
                  description = ["He received 50+ unread emails in the last hour.", 
                                "He has a conference call that he dreads. Ugh."],
                  happiness_mean = -30,
                  happiness_sd   = 2,
                  sleepiness_mean = 10,
                  sleepiness_sd   = 2)


a_watch_youtube = Activity(friend = albert, 
                  verb = "watch guitar videos on youtube",
                  description = ["He wants the modular synthesizers he just saw.", 
                                "How is this 10-year old guitar prodigy so good at music?!",
                                "He really enjoyed that movie trailer"],
                  happiness_mean = 0,
                  happiness_sd   = 3,
                  sleepiness_mean = 0,
                  sleepiness_sd   = 10)


a_play_guitar = Activity(friend = albert, 
                  verb = "play his guitar",
                  description = ["He can't get this part of the Bach right, so he keeps practicing.", 
                                "He plays pretty leisurely.",
                                "Turn up the volume on the amp!"],
                  happiness_mean = 8,
                  happiness_sd   = 4,
                  sleepiness_mean = -10,
                  sleepiness_sd   = 5)

a_continue_sleep = Activity(friend = albert, 
                  verb = "continue his nap",
                  description = ["Zzz"],
                  happiness_mean = 10,
                  happiness_sd   = 2,
                  sleepiness_mean = -80,
                  sleepiness_sd   = 5)

albert_solo_activity_options = [a_work, a_watch_youtube, a_play_guitar]

a_pet_cat = Activity(friend = albert, 
                  verb = "pet Flipper",
                  description = ["Flipper has such long and silky fur.", 
                                "Flipper's fur is warm from sitting in the sun all day."],
                  happiness_mean = 10,
                  happiness_sd   = 2,
                  sleepiness_mean = 10,
                  sleepiness_sd   = 2)

a_take_pics = Activity(friend = albert, 
                  verb = "take pictures of Flipper",
                  description = ["It is a mystery how she is so photogenic from all angles.", 
                                "You look gorgeous, Flipper!"],
                  happiness_mean = 10,
                  happiness_sd   = 2,
                  sleepiness_mean = 10,
                  sleepiness_sd   = 2)

albert_interactive_activity_options = [a_pet_cat, a_take_pics]

f_pets = Activity(friend = flipper, 
                  verb = "ask for some pets",
                  description = ["Flipper: *Purrrr*", 
                                "Flipper lied down on her side. She wants some belly rubs."],
                  happiness_mean = 30,
                  happiness_sd   = 1,
                  sleepiness_mean = 10,
                  sleepiness_sd   = 2)


f_chill = Activity(friend = flipper, 
                  verb = "chill and hang out",
                  description = ["She's intensely watches birds. She loves them.", 
                                "Enjoying some warmth, Flipper?",
                                "Her's eyes are closed, but she's listening for sure."],
                  happiness_mean = 30,
                  happiness_sd   = 1,
                  sleepiness_mean = 10,
                  sleepiness_sd   = 2)

f_fall_asleep = Activity(friend = flipper, 
                  verb = "take a nap",
                  description = ["Flipper appears to be fast asleep - but you kinda never know.", 
                                "How long can a cat sleep?",
                                "Shh... Wait, but her ear twitched, so maybe she's up."],
                  happiness_mean = 10,
                  happiness_sd   = 1,
                  sleepiness_mean = -50,
                  sleepiness_sd   = 5)

f_continue_sleep = Activity(friend = flipper, 
                  verb = "continue her nap",
                  description = ["Zzz..."],
                  happiness_mean = 10,
                  happiness_sd   = 1,
                  sleepiness_mean = -50,
                  sleepiness_sd   = 5)

flipper_interactive_activity_options = [f_pets, f_chill, f_fall_asleep]


# Flipper randomly does one of the following: Show her belly; purr; walk away


def play():
    while True: # Only accept one of the specified 
        user_direction = input('What should Albert do? [m]ove, [s]tay, or [q]uit playing. Or get [h]elp.\n').lower() # Convert input into lowercase 
        

        if user_direction in ["move", "m", "stay", "s"]:
            print("\n")
            consequences(user_direction)

        elif user_direction == "quit" or user_direction == "q":
            print("\nOkay, it's time for Albert to go pick up his wife - me!\n\nThank you for your help today.\nGood-bye!")
            time.sleep(3) # Wait for 3 seconds before quitting.
            sys.exit()

        elif user_direction == "help" or user_direction == "h":
            print("(HELP) Choose from three options:")
            print("    [m]ove - Move to a new location. If Flipper isn't here, let's go look for her.")
            print("    [s]tay - Stay here. Great option if you already found Flipper.")
            print("    [q]uit - End the game.\n")

        else:
            print("Albert didn't understand that. Try again!")


def start():
    # Provide the setting for the user. 
    
    print("--------------------------------------------------------------------------")
    print("Welcome to our house! \
    \nI went to work already. My husband Albert is working from home today.\n")
    
    print("He is working in the Office right now. The day's just begun and Albert's tired already. \
          \nWhere is Flipper? Petting her will make Albert so happy!\n")
    input("(Press [ENTER] to find out who Flipper is.)")
    print("\nFlipper is a sweet cat who technically belongs to our neighbors. \
    \nShe's a Calico and a princess.\
    \nAlbert loves Flipper and spending time with her makes him very happy.")
    
    print("Flipper loves Albert, too, but she is an outdoor cat and is always\
    \ntrying to catch the sunlight, so she'll come and go as she pleases.\n\n")
    
    print("Will you please take care of Albert today while I'm at work? Your job is easy.\
           \nJust help him decide whether to stay in the current spot or move somewhere else!\n\n")
    
    print("Let's play! :D Albert is currently in the Office. Flipper must be outside.\n")
    
    
    input("(Press [ENTER] to continue.)")
    
    print("==========================================================================")
    print("Choose from three options.\n")
    print("    [m]ove - Move to a new location. Maybe Flipper is there.")
    print("    [s]tay - Stay. Albert will choose what to do here.")
    print("    [q]uit - End the game.\n")
    print("==========================================================================")
    
    
    play()


            
def welcome(): # Main menu. 
    os.system('clear')
    print()
    
    for line in portrait:
        time.sleep(0.05)
        print(line)
    
    time.sleep(0.5)
    print("==========================================================================")
    print("FINDING FLIPPER")  
    print("a.k.a. An interactive, hyper-realistic biography of my husband, Albert, \
    \nand his favorite fluffy feline friend, Flipper.")
    print("==========================================================================")
    time.sleep(0.5)
    input("Press [ENTER] to play.")
    os.system('clear') 
    
    start()    
    
    

###############################################################
# Start the game when this file is run                        #
###############################################################
if __name__ == "__main__":
    
    # Start the game. 
    welcome()