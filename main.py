def greet(user_name):
    return f"Hello {user_name}!"

def main():
    userName = input("Hi there!\nI'm todo, what's your name =>")
    print(greet(userName))

if __name__ == "__main__":
    main()