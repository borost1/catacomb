choices=["a", "b", "c", "d"]
key = False or True
class Screen:
    def __init__(
            self,
            title="Sample screen",
            description="Sample description",
            choices=["a", "b", "c", "d"]
    ):
        self.title = title,
        self.description = description
        self.choices = choices

    def show_title(self):
        print("==============================")
        print(self.title)
        print("==============================")





intro_screen()



    def intro_screen(self):
        print("You have  4 doors to choose from! These doors are labeled with 4 letters for some reason, a, b, c, d.")
       userInput = input()
    while userInput not in choices:
        print("choose between a, b, c, d")
    if userInput == "a":
        spike_room()
    if userInput == "b":
        sphinx_room()
    if userInput == "c":
        nice_room()
    if userInput == "d":
        secret_room()

class Screen:
    def spike_room(self):
        print("You see the endless nothingness in front of you, you can go back or jummp")
    userInput = input()
    while userInput not in choices:
        print("choose between a and b")
    if userInput == "a":
        print("You fell into a void of thousand spikes, your life has finally come to an end")
        __init__()
    if userInput == "b":
        intro_screen()


class Screen:
    def sphinx_room(self):
        print("A shadow-like figure appears as you walk into the next room. It looks like something you saw in Egypt years ago, maybe smaller")
        print("It opens it's mouth, but you hear the voice as if it was your own thought")
        print("If you can answer a question I might let you through! So my question is: ")


class Screen:
    def nice_room(self):
        print("This is a nice room, the temperature is OK and there is no leakage. I could stay here, but should probably move on")
        print("Where do you want to go?")
    userInput = input()
    while userInput not in choices:
        print("choose between a, b, c, d")
    if userInput == "a":

    if userInput == "b":

    if userInput == "c":

    if userInput == "d":


class Screen:
    def secret_room(self):
        if key not in self.inventory:
            print("This room wouldn't open")


def make_negative( number ):
    number = ()
    negative_number = number - number - 1
    if number < 0:
        print("This is already a negative number.")
    else:
        print(negative_number)