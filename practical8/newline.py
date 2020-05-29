# Devise a python code-snippet function to remove newline characters from a file.

def remove_newline(filename):
    try:
        contant = open(filename,'r').readlines()
        w_file = open(filename,'w')
        for i in contant:
            print(i.rstrip(), file = w_file, end=' ')
    except Exception as e:
        print(e)
    
remove_newline('mix.txt')
