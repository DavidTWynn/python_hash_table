from collections import Counter
from string import printable
import hashlib


def main():
    allowed_containers = 100

    hash_distribution = distributor(
        printable, allowed_containers, hash_function=DecimalHashes.sha256sum
    )

    display_counter(hash_distribution)

    print(f"Allowed containers {allowed_containers}")


def distributor(iterator, containers: int, hash_function=hash) -> Counter:
    """Takes an iterator and distributes them into containers.
    Returns a count of the containers and how many items are in each.
    Needs an integer result from the hash function."""
    new_container = []
    for item in iterator:
        container = hash_function(item) % containers
        new_container.append(container)

    return Counter(new_container)


def display_counter(counter: Counter):
    """Prints a histogram of a Counter object"""
    containers = counter.keys()
    for container in containers:
        print(f"Container {container}: ", end="")
        container_items = counter[container]
        for _ in range(container_items):
            print("▄", end="")
        print(f" ({container_items})")
    print(f"{len(list(containers))} total containers")


class DecimalHashes:
    """Collection of hash functions that returns a decimal result
    rather than hex."""

    def md5sum(string: str) -> str:
        """Takes a string and returns the decimal value of the md5sum."""
        hex = hashlib.md5(string.encode()).hexdigest()
        return int(hex, 16)

    def sha256sum(string: str) -> str:
        """Takes a string and returns the decimal value of the sha256sum."""
        hex = hashlib.sha256(string.encode()).hexdigest()
        return int(hex, 16)

    def sha512sum(string: str) -> str:
        """Takes a string and returns the decimal value of the sha512sum."""
        hex = hashlib.sha512(string.encode()).hexdigest()
        return int(hex, 16)


if __name__ == "__main__":
    main()
