def get_cs():
    word=input("Enter a string: \n")
    return word

def cs_to_lot(cs):
    lst=cs.split()
    return lst

def lot_to_cs(lot):
    str=" " #for spaces in between
    return (str.join(lot))

def main():
    cs=get_cs()
  
    lot=cs_to_lot(cs)  
    print(lot)
  
    cs=lot_to_cs(lot)  
    print(cs)

if __name__ == '__main__':
    main()