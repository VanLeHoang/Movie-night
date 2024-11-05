#this is an app to randomly recommend a movie/show to watch everyday based on your input
import time
import random

def banner(s):
    #print banner
    l = len(s) + 6
    print()
    print("=" * l, f'{s:^{l}}', "=" * l, sep = "\n")
    
def typing(s):
    #typewriter effect
    speed = list(map(lambda x: x/100, range(1,11)))
    t = 0
    print()
    for i in s:
        t = t % len(speed)
        if i == " ":
            time.sleep(speed[t])
        print(i, end = '', flush = True)
        time.sleep(speed[t])
        t += 1
    print()        
    
def menu():
    typing("What would you want to do?\n"
           "\t1 - Add to watch list\n"
           "\t2 - View watch list\n"
           "\t3 - Choose a movie\n"
           "\t4 - Close app\n"
           "\t(choose 0 to return to the main menu)")
    print("Enter your command: ", end = '')
    return input().rstrip()
def add():
    typing("Please enter the name of your show or movie\n"
            "(Choose 0 to return to menu or 4 to quit)")
    print("Your input: ", end = '')
    return [input().rstrip().title()]
    
def watchlist():
    banner("YOUR WATCH LIST")
    l = max(map(len,movies)) + 7
    print(f'\n{"Title":{l}}{"Episodes":^11}')
    for title in movies:
        print('_' * (l + 11))
        print(f'{title:11}{movies[title]:^11}')

def randommovie():
    typing("The movie you should watch tonight is...")
    seed = random.randrange(len(movies))
    typing(list(movies)[seed])

if __name__ == '__main__':
    movies = {}
    banner("WELCOME TO MOVIE NIGHT")
    typing("!!! This is the app that help you choose a random movie to watch, you can also add and view your watch list !!!")
    n = menu()
        
    while True:
        if n not in ['0','1','2','3','4']:
            print("\n\t! Your command is INCORRECT, please try again !")
            n = menu()
        if n == '0':
            print("\n" + '-' * 30)
            print("\n\t- You have returned to the main menu -")
            n = menu()
        if n == '4':
            typing("Thank you for using, have a great one !!!")
            break
        if n == '1':
            print("\n" + "-" * 30)
            m = add()
            while m[0] in movies and m[0] not in ['0','4']:
                print("\n\t! This entry is already exist, please try again !")
                m = add()
            if m[0] in ['0','4']:
                n = m[0]
                continue
            typing(f'How many episodes does "{m[0]}" have? (please type a number)')
            print("Your input: ", end = '')
            while len(m) == 1:
                try:
                    m.append(int(input().rstrip()))
                except:
                    print("\n\t! The number of episodes is INCORRECT, please try again !")
                    typing(f'How many episodes does "{m[0]}" have? (please type a number)')
                    print("Your input: ", end = '')
            typing(f'\t- You have successfully added "{m[0]}" with {abs(m[1])} episode(s)-')
            movies[m[0]] = abs(m[1])
            print("\nWould you like to add another one? (Y/N): ", end = '')
            yn = input().rstrip()
            if yn == 'Y' or yn == 'y':
                n = '1'
            else:
                n = '0'
        if n == '2':
            print("\n" + "-" * 30)
            if movies:
                watchlist()
                n = '0'
            else:
                print("\n\t! Your watch list is empty, please add a movie !")
                n = '1'
        if n == '3':
            print("\n" + "-" * 30)
            randommovie()
            n = "0"
