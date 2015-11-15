errno = None

def return_code_demo(data):
    if len(data) == 0:
        errno = 1
        return -1
    if len(data) > 1000:
        errno = 2
        return -1

    print("do something useful...")
    return 0

if __name__ == "__main__":
    return_code_demo("")
    return_code_demo("a"*2000)
    return_code_demo("aaa")
