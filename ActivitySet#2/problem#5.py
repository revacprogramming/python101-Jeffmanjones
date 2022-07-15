def get_cs():
    word=input("Enter a string: \n")
    return word

def cs_to_dict(cs):
    d=dict()
    d={(a:=i.split("="))[0]:a[1] for i in cs.split(";")}
    return d
    #dictionary comprehension

def dict_to_cs(d):
    #convert a dictionary to connect string
    pass
  
def main():
    cs = get_cs()
    print(cs)
    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)

if __name__ == '__main__':
    main()