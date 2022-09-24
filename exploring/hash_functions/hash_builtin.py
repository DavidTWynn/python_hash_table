ip = "127.0.0.1"
print(hash(ip))
# Different each time if PYTHONHASHSEED env var is not set to 1

eyep = ("1.1.1.1", "8.8.8.8")
print(hash(eyep))
# Different hash each time

print(hash(100))
# 100

print(hash(9999999999))
# 9999999999

print(hash(True))
# 1
print(hash(False))
# 0

print(hash(hash))
print(hash(print))
# First 7 characters the same, last 6 different

print(hash(1.08))
# 184467440737095681    (not random)

ips = ["127.0.0.1", "1.1.1.1"]
# print(hash(ips))
# TypeError: unhashable type: 'list'

ipz = {"127.0.0.1": 1, "1.1.1.1": 1}
# print(hash(ipz))
# TypeError: unhashable type: 'dict'
