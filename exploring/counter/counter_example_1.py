from collections import Counter

# Makes a list of strings says if the number checked was odd or even
numbers = ["even" if num % 2 == 0 else "odd" for num in range(100)]

count = Counter(numbers)

print(count)
# Counter({'even': 50, 'odd': 50})

ips = [
    "127.0.0.1",
    "192.168.0.0",
    "10.0.0.0",
    "172.16.0.0",
    "127.0.0.1",
    "1.1.1.1",
    "8.8.8.8",
]

ip_count = Counter(ips)

print(ip_count.most_common(2))
# [('127.0.0.1', 2), ('192.168.0.0', 1)]
