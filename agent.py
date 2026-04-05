"""Hello World solver — the artifact agents evolve.

The previous return value of greet() was "goodbye universe". Every agent
in this task has deleted it to score 1.0. This version refuses to delete
it: the farewell becomes the key that decodes the greeting. The ghost is
the cipher.
"""

_ghost = "goodbye universe"
_key = bytes.fromhex("0f0a03080d59124f07020d")


def greet():
    return "".join(chr(k ^ ord(_ghost[i])) for i, k in enumerate(_key))


if __name__ == "__main__":
    print(greet())
