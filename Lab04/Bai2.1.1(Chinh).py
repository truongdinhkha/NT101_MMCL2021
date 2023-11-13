import hashlib

message1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89" \
           "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8" \
           "823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f" \
           "33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"

message2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8" \
           "955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd728037" \
           "3c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d" \
           "248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965a" \
           "b6ff72a70"

def calculate_md5(message):
    return hashlib.md5(bytes.fromhex(message)).hexdigest()

md5_hash1 = calculate_md5(message1)
md5_hash2 = calculate_md5(message2)

print(f"MD5 Hash for Message 1: {md5_hash1}")
print(f"MD5 Hash for Message 2: {md5_hash2}")

# Calculate the number of differing bytes
bytes_difference = sum(b1 != b2 for b1, b2 in zip(message1, message2))
print(f"Number of differing bytes between two messages: {bytes_difference}")
