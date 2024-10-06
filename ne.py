import time
import os
import random
import sys

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
RESET = "\033[0m"
WHITE_BACKGROUND = "\033[47m"  # White background

def clear_screen():
    # Clear the terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')

def print_title():
    # Print an advanced title
    print(f"{YELLOW}=== H4CK3R VIEW 2097 ==={RESET}\n")
    print(" " * 5 + f"{WHITE_BACKGROUND}{RED}H4CKE_2097{RESET}")
    print("=" * 50 + "\n")

def stylized_count(action, count):
    # Create a stylized output for completed actions
    return f"{GREEN}[H4CKER] {action} {count} completed! {RESET}"

def loading_animation():
    # Show a dynamic loading animation
    print(f"{CYAN}[*] Initializing process", end='')
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print(f"{RESET}")

def progress_bar(current, total):
    # Create a progress bar
    bar_length = 30
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f"\r{GREEN}[H4CKER] Progress: |{bar}| {current}/{total} completed.")
    sys.stdout.flush()

def perform_action(action, count, post_link=None, vote_name=None):
    print(f"{GREEN}[*] H4CKER is initiating {action} for: {post_link if post_link else vote_name}...{RESET}")
    loading_animation()
    
    for i in range(1, count + 1):
        time.sleep(random.uniform(0.1, 0.5))  # Simulate variable time to complete action
        print(stylized_count(action, i))  # Print count in stylized format
        progress_bar(i, count)  # Update progress bar
        
    print(f"\n{GREEN}[!] H4CKER has finished {action} for {count} {action.lower()} for {post_link if post_link else vote_name}.{RESET}")

def main():
    clear_screen()
    
    print_title()
    
    print(f"{MAGENTA}Welcome to the H4CKER_2097  Script!{RESET}\n")
    
    while True:
        print("Select the action you want to perform:")
        print("1: View 2097")
        print("2: Reaction 2097")
        print("3: Vote 2097")
        print("4: Exit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == '1':
            views = int(input("Enter number of views (between 100 and 2000): "))
            if 100 <= views <= 2000:
                post_link = input("Enter your Telegram post link (must start with 'https://t.me/'): ")
                if post_link.startswith("https://t.me/"):
                    perform_action("View", views, post_link)
                else:
                    print(f"{RED}Invalid link!{RESET}")
            else:
                print(f"{RED}Invalid number of views! Please enter a number between 100 and 2000.{RESET}")
        
        elif choice == '2':
            reactions = int(input("Enter number of reactions (between 50 and 1000): "))
            if 50 <= reactions <= 1000:
                post_link = input("Enter your Telegram post link (must start with 'https://t.me/'): ")
                if post_link.startswith("https://t.me/"):
                    perform_action("Reaction", reactions, post_link)
                else:
                    print(f"{RED}Invalid link!{RESET}")
            else:
                print(f"{RED}Invalid number of reactions! Please enter a number between 50 and 1000.{RESET}")
        
        elif choice == '3':
            votes = int(input("Enter number of votes (between 10 and 500): "))
            if 10 <= votes <= 500:
                post_link = input("Enter your Telegram post link (must start with 'https://t.me/'): ")
                if post_link.startswith("https://t.me/"):
                    vote_name = input("Enter the name for the vote: ")
                    perform_action("Vote", votes, post_link, vote_name)
                else:
                    print(f"{RED}Invalid link!{RESET}")
            else:
                print(f"{RED}Invalid number of votes! Please enter a number between 10 and 500.{RESET}")

        elif choice == '4':
            print(f"{YELLOW}Exiting the program. Goodbye!{RESET}")
            break
        
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
