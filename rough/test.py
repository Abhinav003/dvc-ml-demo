
import os

def main():
    print("Always running")
    with open(os.path.join("rough","test.txt"),"w") as f:
        f.write("This is a test file again.")
if __name__ == '__main__':
    main()