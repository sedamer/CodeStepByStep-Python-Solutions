def flip_lines(x):
    with open(x, "r") as file:
        c= file.read().splitlines()
        k = len(c)
        if len(c) % 2 ==0:
            for i in range(0,k,2):
                print((c[i+1]).upper())
                print((c[i]).lower())        
        else:
            for i in range(0,k-1,2):
                print((c[i+1]).upper())
                print((c[i]).lower())
            print((c[k-1]).upper())
