import hashlib


string_to_check = "password"
md5out = hashlib.md5(string_to_check.encode()).hexdigest()

print(md5out)
# 5f4dcc3b5aa765d61d8327deb882cf99


def md5sum(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()


print(md5sum("password"))
# 5f4dcc3b5aa765d61d8327deb882cf99


def sha256(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()


print(sha256("password"))
# 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
