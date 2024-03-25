from collections import deque


def is_palindrome(value):
    q = deque()

    for s in value:
        if s != " ":
            q.append(s.lower())

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


if __name__ == "__main__":
    for i in ["asdf", "abba", "ababa", "abbaa"]:
        print(i, end=" - ")
        print("is palindrome" if is_palindrome(i) else "is not palindrome")
