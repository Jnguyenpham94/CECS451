import sys


def filtering(x, b, c, d, f, e):
    _x = (float(x[0]) * float(b[0])) + (float(x[0]) * (1 - float(b[0])))
    _y = (float(x[1]) * (1 - float(b[0]))) + (float(x[1]) * float(b[0]))
    _x *= float(d[0])
    _y *= float(f[0])
    alpha = 1 / (_x + _y)
    _x *= alpha
    _y *= alpha
    xt = (_x, _y)
    return xt


def hmm(probs, evidence):
    x0 = (float(probs[0]), 1 - float(probs[0]))  # (x, not x)
    # print(probs)
    b = (probs[1], True)
    c = (probs[2], False)
    d = (probs[3], True)
    f = (probs[4], False)
    e = [evidence[0], evidence[1]]
    # print(e)
    #  filtering stuff below
    x1 = filtering(x0, b, c, d, f, e)
    print(f"{probs[0]},{probs[1]},{probs[2]},{probs[3]},{probs[4]},{e[0]},{e[1]}--><{x1[0]:.4f},{x1[1]:.4f}>")
    x2 = filtering(x1, b, c, d, f, e)
    state = max(x2[0], x2[1])
    if state == x2[0]:
        e.append('t')
    elif state == x2[1]:
        e.append('f')
    print(f"{probs[0]},{probs[1]},{probs[2]},{probs[3]},{probs[4]},{e[0]},{e[1]},{e[2]}--><{x2[0]:.4f},{x2[1]:.4f}>")


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
                eValues.append('t')
            elif i == 'f':
                eValues.append('f')
            else:
                probs.append(i)

    hmm(probs[0:5], (eValues[0], eValues[1]))  # line 1 from cpt.txt
    hmm(probs[5:10], (eValues[2], eValues[3])) # line 2 from cpt.txt


if __name__ == '__main__':
    main(sys.argv)
