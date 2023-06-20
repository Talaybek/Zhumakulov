def xor(a, b):
    result = ''
    for i in range(len(a)):
        code = ord(a[i]) ^ ord(b[i % len(b)])
        result += chr(code)
    return result

def xor_decipher(a, b):
    result = ''
    for i in range(len(a)):
        code = ord(a[i]) ^ ord(b[i % len(b)])
        result += chr(code)
    return result

input_a = input()
encryption_b = input()
encrypted_a = xor(input_a, encryption_b)
print(encrypted_a)
decryption_b = input()
decrypted_a = xor_decipher(encrypted_a, decryption_b)
print(ecrypted_a)
