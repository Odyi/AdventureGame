# Start of game
import time, sys
from colorama import Fore



tekst_hasighet = 0.06 # HASTIGHET PÅ TEKST
 
def tekst(bokstaver):
    for i in bokstaver:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(tekst_hasighet)


tekst('You stumble upon a weird stone, upon closer insepction you realize its a monument.') 
tekst("the writing etched on the monument states.")
tekst(f'{Fore.GREEN}"Do you want to enter the game."{Fore.RESET}')
tekst(f"{Fore.YELLOW}What do you choose YES or NO{Fore.RESET}")

Choice = input("> ")

if(Choice == "YES"):
    tekst("Before you can react.")
    tekst(f"{Fore.RED}BAM{Fore.RESET}")

elif(Choice == "NO"):
     tekst("You")

else:
      tekst("Invalid choice, please enter YES or NO.")





    