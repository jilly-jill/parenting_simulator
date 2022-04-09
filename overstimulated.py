import time
import sys

def main():

    def print_style(text, delay=0.05):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)

    def opening():
        opening_lines = [f"\n'There's nothing more contagious than the laughter of young children... \n   " +
                  "It doesn't even have to matter what they're laughing about....'\n" +
                         "        ~ Crissi Jami\n"]
        for word in opening_lines:
            print_style(word + " ")

        lines = ["\n\nKids are AMAZING\n" +
                 "Amazing BUT exhausting...\n" +
                 "Not a parent? caretaker? guardian?...\n" +
                 "Come experience a slice of overload...\n\n"]
        for text in lines:
            print_style(text + " ")

        time.sleep(1)
        start = input("\nAre you ready to experience the fun? Y or N\n>> ").upper()
        if start.__contains__("Y") or start.__contains__("N"):
            if start == "N":
                punked_out = input("\nIt's okay to admit you can't handle it..\nAre you REALLY sure?\nY or N\n>> ").upper()
                if punked_out == 'Y':
                    print("\nI guess not all of us are cut from caffeine and masochism..\n")
                else:
                    print("\nTHAT'S more like it!\n")
                    time.sleep(1.2)
                    check_in()
            else:
                time.sleep(1.2)
                check_in()

    def breath():
        time.sleep(0.25)

    def check_in():
        print('On a scale from 1 to 10, with 1 being less and 10 being more:\n')
        check = input('How overstimulated are you?\n>> ')
        name = input('What does the kiddo call you?\n>> ').capitalize()
        overstimulated = int(check)
        still_overstimulated = True

        while check == '':
            input('How overstimulated are you?\n>> ')
        while name == '':
            input('What does the kiddo call you?\n>> ').capitalize()

        while still_overstimulated:

            while overstimulated >= 7:
                name_called = 0
                while name_called < 50:
                    print(f"{name}")
                    breath()

            if overstimulated >= 4 and overstimulated < 7:
                name_called = 0
                while name_called < 20:
                    print(f"{name}")
                    name_called += 1
                    breath()

            print(f"\n{name} I LOVE YOU\n".upper())
            break

        again = input("\n\nWould you like to try that again? Y or N\n>> ")
        for word in again:
            print_style(word + " ")
        if again.__contains__("Y"):
            check_in()
        elif again.__contains__("N"):
            print('I guess not all of us are cut from caffeine and masochism..')
        else:
            print_style(word + " ")

    opening()


if __name__ == '__main__':
    main()
