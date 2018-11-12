


#

def check_fn():
    user_in = input("Enter yes/no  ").strip()
    while user_in != 'YES':
        if user_in == 'YES':
            print('Accepted')
            continue
        elif user_in == 'yes':
            print(user_in.upper())
            break
        else:
            print("invalid input.. pls enter again")
            check_fn()


check_fn()