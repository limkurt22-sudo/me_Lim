# Assessment 3.2 - Array (dynamic version of ArrayLIM)

def main():
    name = input("Enter your last name: ").strip().upper() or "LIM"
    arr = [None] * len(name)   # fixed-size array sized to the name
    size = 0

    # ADD each letter
    for letter in name:
        arr[size] = letter
        size += 1
        print("Added", letter)
        print("Array:", arr[:size])

    # REMOVE each letter (from the last index)
    while size > 0:
        print("Removed", arr[size - 1])
        arr[size - 1] = None
        size -= 1
        print("Array:", arr[:size])

    print("Array is empty")


if __name__ == "__main__":
    main()
