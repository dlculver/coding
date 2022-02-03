#### creating wrapper definition from scratch. I think what I want to do is to take a string and make it into a list. Then join with new lines...

def wrap(string, max_width):
    list_blocks = []
    n = len(string)
    k = n//max_width
    for i in range(0,k+1):
        list_blocks.append(string[:max_width])
        string = string[max_width:]
        #return list_blocks
    return '\n'.join(list_blocks)




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
