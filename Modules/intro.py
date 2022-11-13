
from Modules import response
import colorama
from colorama import Fore



def introMsg():
    
    msg1 = '''
    
     /$$   /$$                     /$$              /$$$$$$  /$$                           /$$      
    | $$  | $$                    | $$             /$$__  $$| $$                          | $$      
    | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$       | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$
    | $$$$$$$$ |____  $$ /$$_____/| $$__  $$      | $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/
    | $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$      | $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ 
    | $$  | $$ /$$__  $$ \____  $$| $$  | $$      | $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ 
    | $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$      |  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
    |__/  |__/ \_______/|_______/ |__/  |__/       \______/ |__/  |__/ \_______/ \_______/|__/  \__/
                                                                                                    
                                                                                            v1.0
                                                                                                    
                                                                                            By Abdulaziz Almetairy
                                                                                            https://github.com/oh-az
                                                                                              
                                                                                                    
    '''
    print(Fore.GREEN + msg1)

def resultMsg():
    print(Fore.RED + "\n\n\nHashes with Alerts:     " , response.alert_count)
    print(Fore.YELLOW + "Hashes not found:       " , response.no_hash_count)
    print(Fore.GREEN + "Hashes with NO Alerts:  " , response.zero_count)
