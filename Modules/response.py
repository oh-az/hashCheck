import json
import time
from Modules import KEY
import colorama
from colorama import Fore

def responseCheck(lines):
    try:
        global counter,alert_count,no_hash_count,zero_count
        counter = 1
        alert_count = 0
        no_hash_count = 0
        zero_count = 0
        for line in lines:
            response = KEY.virustotal.get_file_report(line)
            json_data = json.loads(json.dumps(response))
            responseCode = json_data['results']['response_code']
        
            if responseCode == 1:
                    print(Fore.WHITE + "\n\n" + str(counter) + " Hash:    " + json_data['results']['md5'])
                    print("sha-1:  " + json_data['results']['sha1'])
                    
                    if str(json_data['results']['positives']) == "0":
                        print(Fore.GREEN + "Alerted on : ", str(json_data['results']['positives']) , "/" , str(json_data['results']['total']) + " Vendors")
                        zero_count += 1
                    else:
                        print(Fore.RED + "Alerted on : ", str(json_data['results']['positives']) , "/" , str(json_data['results']['total']) + " Vendors")
                        print(Fore.BLUE + "Link:  " + json_data['results']['permalink'])
                        alert_count += 1
            else:
                    print(Fore.YELLOW + "\n\n" + str(counter) + " Hash:    " , line.strip("\n"))
                    print("Alerted on : "+ "Hash Not in Database")
                    no_hash_count += 1
        
            counter += 1
            time.sleep(15)
    except:
        print("Error! Please make sure that your API key is valid and is in KEY.txt")
        
        
def resultMsg():
    print(Fore.RED + "\n\n\nHashes with Alerts:     " , alert_count)
    print(Fore.YELLOW + "Hashes not found:       " , no_hash_count)
    print(Fore.GREEN + "Hashes with NO Alerts:  " , zero_count)
        
