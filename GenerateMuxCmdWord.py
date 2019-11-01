

def genCmdWord(RT, TrRcv, SA, wc):
    output = (RT << 11) | (TrRcv << 10) | (SA << 5) | wc
    print('Msg ' + str(SA) + ': ' + str(hex(output)))



if __name__ == '__main__':
    while True:
        rt = int(input("Enter RT #: "))
        tr = int(input("Enter Tr (1) or Rcv (0): "))
        sa = int(input("Enter SA: "))
        wc = int(input("Enter WC: "))
        genCmdWord(rt, tr, sa, wc)
        print("\n")
        
    
