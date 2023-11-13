import hashlib

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return hashlib.md5(content).hexdigest()

hello_md5 = calculate_md5('C:\Users\dinhkha\Downloads\hello.exe')  # Replace with actual path
erase_md5 = calculate_md5('C:\Users\dinhkha\Downloads\erase.exe')  # Replace with actual path

print(f'MD5 Hash for hello.exe: {hello_md5}')
print(f'MD5 Hash for erase.exe: {erase_md5}')
