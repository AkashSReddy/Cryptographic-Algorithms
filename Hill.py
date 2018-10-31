import numpy as np

def encrypt(matrix, words):
    check_param(matrix, words)
    cipher = ''
    length = len(matrix)
    matrix = np.array(matrix)
    words = words.lower()
    arr = [ord(i) - ord('a') for i in words]
    count = 0
    for ch in words:
        if str.isalpha(str(ch)):
            cipher += chr(sum(matrix[count % length] * arr) % 26 + ord('a'))
            count += 1
    return cipher



def decrypt(matrix, words):
    cipher = ''
    length = len(matrix)
    matrix = (np.linalg.inv(matrix) + 26) % 26
    words = words.lower()
    arr = np.array([ord(i) - ord('a') for i in words], dtype=int)
    count = 0
    for ch in words:
        if str.isalpha(str(ch)):
            number = sum(matrix[count % length] * arr) % 26
            cipher += chr(int(str(number)[:-2]) + ord('a'))
            count += 1
    return cipher



def check_param(matrix, words):
    if len(matrix) * len(matrix) != \
            sum([len(matrix[i]) for i in range(len(matrix))]):
        print("Error:")
        quit()
    elif len(matrix) != len(words):
        print("Error")
        quit()
    try:
        np.linalg.inv(matrix)
    except Exception, e:
        print("Error:  " + str(e))
        quit()


if __name__ == '__main__':

    secret = [[8, 6, 9, 5],
              [6, 9, 5, 10],
              [5, 8, 4, 9],
              [10, 6, 11, 4]]
    text = "hill"

    ciphertext = encrypt(secret, text)

    print(ciphertext)

    print(decrypt(secret, ciphertext))