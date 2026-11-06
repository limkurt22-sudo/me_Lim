# Assessment 3.2 - Stack / LIFO (dynamic version of StackLIM)

def main():
    name = input("Enter your last name: ").strip().upper() or "LIM"
    stack = [None] * len(name)
    top = -1

    # PUSH each letter
    for letter in name:
        top += 1
        stack[top] = letter
        print("Pushed", letter)
        print("Stack:", stack[:top + 1])

    # POP each letter
    while top >= 0:
        print("Popped", stack[top])
        top -= 1
        print("Stack:", stack[:top + 1])

    print("Stack is empty")


if __name__ == "__main__":
    main()
