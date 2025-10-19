
import sys

def help(text=None, delay=0.033):
    print(" welcome to brandon! a fun bot right in your terminal!")
    print(space)
    print(" here are the commands you can use:")
    print(space)
    print("help - shows this message")
    print(space)
    print("about - shows info about the bot")
    print(space)
    print("exit - exits the bot")
    print(space)
    print("PacerTest - The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.")

def about(text, delay=0.03):
    print("brandon v0.1")
    print("made by m3g4byt3s")
    print("a fun bot right in your terminal.")
    return

def exit(text, delay=0.03):
    sys.exit("Brandon is exiting...")

def pacerTest(text, delay=0.03):
    print("The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.")

space = " "

# Main loop
def main():
    print("Hi! I'm Brandon, your personal command bot!")  # <-- greeting here
    print("Type 'help' to see what I can do.")
    
    while True:
        cmd = input("Enter a command:").lower()
        if cmd in commands:
            commands[cmd]
        else:
            print("Unknown command! Type 'help' to see available commands.")

# Start the bot
if __name__ == "__main__":
    commands = {
        "help": help,
        "about": about,
        "exit": lambda: sys.exit("Brandon is shutting down..."),
        "pacerTest": pacerTest
    }
    main()
