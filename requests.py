from queue import Queue
from time import sleep


queue = Queue()


def id_builder():
    id = 0

    def generate():
        nonlocal id
        id += 1
        return id

    return generate


get_id = id_builder()


def generate_request():
    id = get_id()
    queue.put(id)
    print(f"New request id: {id}")


def process_request():
    if queue.empty():
        print("Queue is empty")
    else:
        id = queue.get()
        print(f"Processing request id: {id}")
        sleep(1)
        print(f"Request {id} processed successfully")


def main():
    while True:
        generate_request()
        process_request()

        if input("\n\nContinue? (y/n): ").lower() != "y":
            break
        print("\n")


if __name__ == "__main__":
    main()
