def get_cs():
    word=input("Enter a string")
    return word

def cs_to_lot(cs):
    lst=cs.split()
    return lst

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)

if __name__ == '__main__':
    main()

#done