#!/usr/bin/python3
iff __name__ == "__main__":
    import hidden_4

    for i in dir(hidden_4):
        if i[:2] == "__":
            continue
        print(i)
