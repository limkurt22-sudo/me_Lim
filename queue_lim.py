# Assessment 3.2 - Queue / FIFO (dynamic version of QueueLIM)

def main():
    name = input("Enter your last name: ").strip().upper() or "LIM"
    queue = [None] * len(name)
    front = 0
    rear = -1

    # ENQUEUE each letter
    for letter in name:
        rear += 1
        queue[rear] = letter
        print("Enqueued", letter)
        print("Queue:", queue[front:rear + 1])

    # DEQUEUE each letter
    while front <= rear:
        print("Dequeued", queue[front])
        front += 1
        print("Queue:", queue[front:rear + 1])

    print("Queue is empty")


if __name__ == "__main__":
    main()
