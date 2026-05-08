import os
import sys

def cleacreen():
    os.system('clear')

def header():
    print("==============================")
    print("   Created By Abhi pandey  ")
    print("==============================")

def update_system():
    print("\n[*] Updating packages...")
    os.system('pkg update && pkg upgrade -y')
    print("[+] System updated successfully.")

def install_essentials():
    print("\n[*] Installing Git, Curl, and Wget...")
    os.system('pkg install git curl wget -y')
    print("[+] Essentials installed.")

def show_sys_info():
    print("\n[*] System Information:")
    os.system('uname -a')
    os.system('df -h')

def main_menu():
    while True:
        clear_screen()
        header()
        print("[1] Update & Upgrade System")
        print("[2] Install Essential Tools (Git/Curl)")
        print("[3] Check Disk & System Info")
        print("[4] Access Python Shell")
        print("[Q] Exit")
        print("[5] Exit")
        choice = input("\nSelect an option: ").lower()

        if choice == '1':
            update_system()
            input("\nPress Enter to continue...")
        elif choice == '2':
            install_essentials()
            input("\nPress Enter to continue...")
        elif choice == '3':
            show_sys_info()
            input("\nPress Enter to continue...")
        elif choice == '4':
            os.system('python')
        elif choice == 'q':
            print("Exiting...")
            sys.exit()
       
       