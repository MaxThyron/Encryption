from random import randint, random
import functions

def encrypt():
    single_matrix_size = get_message_length()
    matrix = create_scrypt_matrix(single_matrix_size)
    print()
    key, grid = generate_key(matrix)
    encrypted_message = encrypt_message(key, grid)
    print()
    functions.print_matrix(encrypted_message)

def get_message_length():
    while True:
        print("Options for message length (in symbols):\n1) 16\n2) 36\n3) 64\n")
        try:
            message_length_index = int(input("Choose (1, 2, 3)> ")) - 1
            if message_length_index < 0 or message_length_index > 2:
                raise ValueError
        except ValueError:
            print("\nWrong length value. Please, repeat your answer.\n")
            continue
        else:
            break

    message_length = [16, 36, 64]

    single_matrix_size = int((message_length[message_length_index] / 4) ** (1 / 2))

    return single_matrix_size

def create_scrypt_matrix(single_matrix_size):
    quarters = []

    for i in range(4):
        quarters.append(functions.create_matrix(single_matrix_size))

    for quarter_index in range(1,4):
        for rotate_count in range(quarter_index):
            functions.rotate_matrix(quarters[quarter_index])

    quarters[2], quarters[3] = quarters[3], quarters[2]

    matrix = build_matrix(quarters)

    return matrix

def build_matrix(quarters):
    matrix = []

    for length in range(2):
        for i in range(len(quarters[0])):
            line = []
            for k in range(length * 2, length * 2 + 2):
                for j in range(len(quarters[0])):
                    line.append(quarters[k][i][j])
            matrix.append(line)

    return matrix

def generate_key(matrix):
    n = len(matrix)
    numbers = []
    
    for i in range((n // 2) ** 2):
        numbers.append(i + 1)

    grid = functions.create_null_matrix(n)

    while len(numbers) != 0:
        x = round(random() * (n - 1))
        y = round(random() * (n - 1))
        if matrix[x][y] != "#" and numbers.count(matrix[x][y]) != 0:
            numbers.remove(matrix[x][y])
            matrix[x][y] = "#"
            grid[x][y] = 1

    key = []

    for i in range(len(grid)):
        binary = 0
        for j in range(len(grid[i])):
            binary += grid[i][j] * 2 ** (7-j)
        key.append(binary)

    return key, grid

def get_message(length):
    while True:
        try:
            print(" " * (13 + length) + ">|")  
            message = list((input("Enter message> ")).lower())
            message_length = len(message)
            if message_length > length:
                raise ValueError

        except ValueError:
            print("\nYour message's length is too big, make it", length ** 2, "symbols or less.\n")
            continue

        else:
            return message

def encrypt_message(key, grid):
    print("Generated key: ", end ="")
    functions.print_key(key)
    key_length = len(key)

    message = get_message(key_length ** 2)

    for i in range(len(message)):
        if message[i] == " ":
            message[i] = "-"

    if len(message) != key_length ** 2:
        if len(message) != key_length ** 2 - 1:
            message.append("-")
        message.append("-")
        for i in range(key_length ** 2 - len(message)):
            message.append(chr(randint(97, 122)))

    message.reverse()

    n = len(grid)
    scrypt = []
    for i in range(n):
        scrypt.append(["#"] * n)

    while len(message) != 0:
        for j in range(n):
            for i in range(n):
                if grid[i][j] == 1:
                    scrypt[i][j] = message.pop(0)

        functions.rotate_matrix(grid)

    return scrypt

if __name__ == "__main__":
    encrypt()
