import sys


# .4f format
def main(args):
    try:
        content = open(args[1], 'r').read()
        remove_chars = ":,{}'''"
        for chars in remove_chars:
                content = content.replace(chars, " ")
        content = content.split()
    except:
        print("File not found. Goodbye")
        exit()
    print(content)
    # print("0.5,0.7,0.3,0.9,0.2,t,t--><0.8834,0.1166>")
    # print("0.5,0.7,0.3,0.9,0.2,t,t,f--><0.1907,0.8093>")


if __name__ == '__main__':
    main(sys.argv)
