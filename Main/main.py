import requests
import inquirer
import subprocess
from colorama import Fore, init
import os
init(autoreset=True)
def updateUser(choice) -> None:
    if choice == "No":
        pass
    else:
        result = subprocess.run(
        ["git", "pull"], 
        cwd= os.getcwd(),
        capture_output=True, 
        text=True, 
        check=True
    )
    print("Success:", result.stdout)
        
def getUserUpdateChoice() -> String:
    answer = inquirer.prompt([
        inquirer.List("confirm", message="Continue?", choices=["Yes", "No"])
    ])

    return answer["confirm"]

def debugPrint(message:str) -> None:
    print(f"[{Fore.LIGHTCYAN_EX}*{Fore.RESET}] {message}")

def getUserVersion() -> String:
    cwd = os.getcwd()
    with open(f"{cwd}/version.txt", 'r') as f:
        current_version = f.read()
        debugPrint(f"Your current version is {current_version}")
        return current_version

print(f"{Fore.LIGHTCYAN_EX}Checking version..")
try:
    url = "https://raw.githubusercontent.com/l1nc0lnwtff/TunerX/refs/heads/main/version.txt"
    r = requests.get(url)
    version = r.text.strip()
    debugPrint(f"The current (Updated) version of the program is: {version}")
    user_version = getUserVersion()
    if version != user_version:
        debugPrint(f"The user version ({user_version}) does not match the programs latest version! ({version})")
        debugPrint(f"Would you like to update?")
        choice_user = getUserUpdateChoice()
        updateProject(choice_user)
except Exception as e:
    print(f"{e}")