#coding=utf-8

def spinWords(args):
    List = args.split()
    L = []
    for i in List:
        if len(i) < 5:
            L.append(i)
        else:
            i = reversed(i)
            i = ''.join(i)
            L.append(i)
    return ' '.join(L)


if __name__ == '__main__':
    L = spinWords('This is another test')
    print(L)