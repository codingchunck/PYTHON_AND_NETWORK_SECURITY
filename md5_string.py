import hashlib

str2hash = input(" input string = ")

result = hashlib.md5(str2hash.encode())
print("The hash is : ", end ="")
print(result.hexdigest())

