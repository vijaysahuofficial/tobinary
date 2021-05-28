#!/usr/bin/python3
import os, sys

banner = '''
Created By
######################################     
██╗   ██╗██╗     ██╗ █████╗ ██╗   ██╗
██║   ██║██║     ██║██╔══██╗╚██╗ ██╔╝
██║   ██║██║     ██║███████║ ╚████╔╝ 
╚██╗ ██╔╝██║██   ██║██╔══██║  ╚██╔╝  
 ╚████╔╝ ██║╚█████╔╝██║  ██║   ██║   
  ╚═══╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝                         
######################################                             
'''
print(banner, "\n")

binary_list = []
intruptted_msg = "Interrupted"

def binary_convert(a, *args):
    binary = bin(a).replace('0b','')
    x = binary[::-1]
    while len(x) < 8:
        x += '0'
    binary = x[::-1]
    return binary

def save(file, filename):
    print(file)
    path = 'output'
    if os.path.exists(path) == False:
        print("[-] output Folder not Found")
        os.mkdir(path)
        print("[+] output Folder Created Successfully")

    for i in file:    
        x = open(f'output/{filename}.txt', 'a')
        x.write(f'{i} ')
        x.close()
    print("File Saved at Output folder")

running = True

while running == True:
    try:
        text = input('Enter Text\n:>>> ')
    except KeyboardInterrupt:
        print(intruptted_msg)
        sys.exit(0)
    if text == 'exit':
        break    
    for i in text:
        x = ord(i)
        out = binary_convert(x)
        print(out, end=' ')
        binary_list.append(out)

    try:
        save_conf = input("\nDo you want to save the file (Y/N)\n:>>>").lower()
    except KeyboardInterrupt:
        print(intruptted_msg)
        sys.exit(0)

    if save_conf == 'y':
        try:
            f_name = input("\nEnter File Name \n:>>>")
        except KeyboardInterrupt:
            print(intruptted_msg)
            sys.exit(0)
        save(binary_list, f_name)
    else:
        pass

    try:
        user_confirmation = input('\nDo you want to Convert another text again? (Y/N) \n:default(Y)>>>').lower()
    except KeyboardInterrupt:
        print(intruptted_msg)
        sys.exit(0)
    
    if user_confirmation == 'y':
        running = True
    elif user_confirmation == '':
        running = True
    elif user_confirmation == 'n':
        running = False
    elif user_confirmation == 'exit':
        running = False
    else:
        print("\nSomething Went Wrong")
        running = False




