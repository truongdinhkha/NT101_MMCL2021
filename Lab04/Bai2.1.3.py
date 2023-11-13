import hashlib

def calculate_sha1(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return hashlib.sha1(content).hexdigest()

sha1_hash1 = calculate_sha1(r'E:\HocKi5\AnToanMang\shattered-1.pdf')  # Replace with actual path
sha1_hash2 = calculate_sha1(r'E:\HocKi5\AnToanMang\shattered-2.pdf')  # Replace with actual path

print(f'SHA-1 Hash for shattered-1.pdf: {sha1_hash1}')
print(f'SHA-1 Hash for shattered-2.pdf: {sha1_hash2}')
