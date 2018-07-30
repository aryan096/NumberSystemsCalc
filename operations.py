# Converts binary to hexadecimal
# Given: 10010 ; Expect: 12
# Given: 10 ; Expect: 2
def binary_hex(binary):
    ans = hex(binary)
    return ans[2:]

# Converts binary to octal
# Given: 10010 ; Expect: 22
# Given: 10 ; Expect: 2
def binary_octal(binary):
    ans = oct(binary)
    return ans[2:]

# Converts octal to binary
# Given: 22 ; Expect: 10010
# Given: 2 ; Expect: 10
def octal_binary(octal):
    ans = bin(octal)
    return ans[2:]

# Converts decimal to binary
# Given: 18 ; Expect: 10010
# Given: 2 ; Expect: 10
def decimal_binary(decimal):
    ans = bin(decimal)
    return ans[2:]

# Converts hexadecimal to binary
# Given: 12 ; Expect: 10010
# Given: 2 ; Expect: 10
def hex_binary(hex):
    ans = bin(hex)
    return ans[2:]
