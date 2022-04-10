import sys


def hmm(probs, evidence):
    x0 = (probs[0], 1 - float(probs[0]))
    # print(probs)
    b = (probs[1], True)
    c = (probs[2], False)
    d = (probs[3], True)
    f = (probs[4], False)
    e = [evidence[0], evidence[1]]
    # print(e)
    # print("0.5,0.7,0.3,0.9,0.2,t,t--><0.8834,0.1166>")
    # print("0.5,0.7,0.3,0.9,0.2,t,t,f--><0.1907,0.8093>")


#  ['0.5', '0.7', '0.3', '0.9', '0.2', 't', 't', '0.7', '0.8', '0.3', '0.2', '0.7', 't', 'f']
# .4f format
def main(args):
    #  process probs from txt file
    try:
        content = open(args[1], 'r').read()
        remove_chars = ":,{}'''"
        for chars in remove_chars:
            content = content.replace(chars, " ")
        content = content.split()
    except FileNotFoundError:
        print("File not found. Goodbye")
        exit()
    eValues = []
    probs = []
    for i in content:
        if type(i) is str:
            if i == 't':
                eValues.append(True)
            elif i == 'f':
                eValues.append(False)
            else:
                probs.append(i)
    # print(eValues)
    # print(probs)
    hmm(probs[0:5], (eValues[0], eValues[1]))
    hmm(probs[5:10], (eValues[2], eValues[3]))


if __name__ == '__main__':
    main(sys.argv)
