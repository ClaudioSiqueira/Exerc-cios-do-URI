def main():
    s1 = input()
    s2 = input()
    if s1 > s2:
        s1, s2 = s2, s1
    print(s1)
    print(s2)

if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break