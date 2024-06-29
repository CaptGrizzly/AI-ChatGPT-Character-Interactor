import os
import subprocess
from colorama import init, Fore, Style

def format_name(name):
    """Capitalize each part of the name for display."""
    return ' '.join(word.capitalize() for word in name.split())

def main():
    # try:
        print(Fore.BLUE + "\n\nWelcome to the AI Characters App!\nPlease type the name of the character you would like to talk to:")
        while True:  # Start an infinite loop
            character_name = input(Fore.BLUE + "Name: ").strip().lower()
            script_name = character_name.replace(" ", "_") + ".py"

            characters_folder = os.path.join(os.path.dirname(__file__), "characters")
            script_path = os.path.join(characters_folder, script_name)

            if character_name == "exit" or character_name == "quit" or character_name == "q" or character_name == "e":
                print(Fore.BLUE + "Thank you for using the AI Character App!")
                break

            if character_name == ".character template":
                print(Fore.RED + "\nError: Character Template not usable. Please select a new Character\n")
                continue
            
            # Define the path to the characters directory relative to this script
            characters_folder = os.path.join(os.path.dirname(__file__), "characters")
            script_path = os.path.join(characters_folder, script_name)

            # Check if the file exists
            if os.path.isfile(script_path):
                # Use subprocess to run the Python script
                formatted_character_name = format_name(character_name)
                print(Fore.GREEN + f"\nLaunching {formatted_character_name}...\n\n")
                try:
                    subprocess.run(['python', script_path], check=True)
                except subprocess.CalledProcessError as e:
                    print("Failed to execute the script:", e)
                break  # Exit the loop after successful launch
            else:
                print(Fore.RED + "\nError: No such character found. Please check the name and try again.\n")
    # except Exception as e:
    #     print("An error occurred:", str(e))
    # input("Press Enter to exit...")

if __name__ == "__main__":
    main()
