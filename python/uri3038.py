while True:
    try:
        string = str(input()).replace('@', 'a').replace('&', 'e').replace('!', 'i').replace('*', 'o').replace('#', 'u')
        print(string)
    except EOFError:
        break
