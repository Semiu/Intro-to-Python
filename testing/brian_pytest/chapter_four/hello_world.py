
def hello():
    with open("hello.txt", "w") as file_:
        file_.write("Hello World!\n")

if __name__ == "__main__":
    hello()