import os
import sys

def clear_screen():
    os.system('clear')

def header():
    print("=" * 30)
    print("   TERMUX MASTER CONTROL   ")
    print("=" * 30)

def update_system():
    print("[*] Updating packages...")
    os.system('pkg update && pkg upgrade -y')
    print("[+] Done.")

def system_info():
    print("[*] Device Info:")
    os.system('uname -a')
    os.system('uptime')

def file_manager():
    print("\n--- Storage Overview ---")
    os.system('df -h')

def main_menu():
    while True:
        clear_screen()
        header()
        print("1. Update System")
        print("2. Check System Info")
        print("3. Storage Status")
        print("4. Install Common Tools (Git, Curl, Wget)")
        print("0. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == '1':
            update_system()
        elif choice == '2':
            system_info()
        elif choice == '3':
            file_manager()
        elif choice == '4':
            os.system('pkg install git curl wget -y')
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
