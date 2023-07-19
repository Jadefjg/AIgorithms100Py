def list_Flatten(src):
    tmp = []
    for i in src:
        if type(i) is not list:
            tmp.append(i)
        else:
            tmp.extend(list_Flatten(i))
    return tmp


if __name__=="__main__":
    src = [1,2,3,[4,5,6],[7,8,9,[10,11,12]]]
    a = list_Flatten(src)
    print(a)