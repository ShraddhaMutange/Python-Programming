def main():
    Marks = [78,90,56,98,77]

    for no in Marks:
        print(no)

    Marks[2] = 59               # no error

    print("-" * 15)
    for no in Marks:
        print(no)               # [78, 90, 59, 98, 77]


if (__name__ == "__main__"):
    main()