import functions

def translate(key, scrypt):
    grid = []

    for i in range(len(key)):
        grid.append(change_base(key[i]))    

    message = []
    for k in range(4):        
        for j in range(len(scrypt)):
            for i in range(len(scrypt)):
                message = add_message(grid[i][j], scrypt[i][j], message)
        functions.rotate_matrix(grid)

    message.reverse()
    message = ''.join(message)            

    return message

def add_message(current, encrypted, message):
    if current == 1:
        if encrypted == '-': 
            if len(message) != 0 and message[len(message) - 1] == ' ':
                message = message[len(message) + 1:]
            message.append(' ')                                
        else:
            message.append(encrypted)                           

    return message

def change_base(number):
    binary = []

    while number != 0:
        binary.append(number % 2)
        number = number // 2

    while len(binary) != 8:
        binary.append(0)

    binary.reverse()

    return binary

def decrypt():
    key = list(map(int, input('Enter the key for decryption> ').split()))
    print()

    size = int(len(key) / 2)

    print('Input scrypt pattern:')
    print()
    scrypt = []

    for i in range(size*2):
        scrypt.append(list(input().split()))
    print()
        
    print('Translated message:')
    print()
    print(translate(key, scrypt))

if __name__ == "__main__":
    decrypt()
