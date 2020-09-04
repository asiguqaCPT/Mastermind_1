import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    list = []
    for i in range(4):
        list.append(random.randint(1,8))
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    
    u_input = input('Input 4 digit code: ')
    
    while True:
        if len(u_input) != 4:
            print('Please enter exactly 4 digits.')
            u_input = input('Input 4 digit code: ')
            continue
        break
    
    control_var = True
    while control_var:
        for i in u_input:
            i = int(i)
            if i not in range(1,9):
                print('Please enter exactly 4 digits.')
                u_input = input('Input 4 digit code: ')
                break
            else:
                control_var = False
                continue
        
    pass

if __name__ == "__main__":
    run_game()
