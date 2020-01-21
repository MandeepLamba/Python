def eval_loop():
    str = ""
    while str != 'done':
        str=input("Enter String: ")
        if(str == 'done'):
            break
        print(eval(str))