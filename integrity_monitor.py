import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

print("SHA256 Hash:")
print(file_hash)
