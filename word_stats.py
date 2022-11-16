def word_stats(x):
    with open(x, "r") as file:
        lines= file.read().split()
        ul =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
             ".", ",", "!", "?", "/"]
        
        s=0
        c=0
        for i in range(0,len(lines)):
            x= lines[i].lower()
            s+= len(lines[i])
            for k in range(0,len(ul)):
                if ul[k] in lines[i]:
                    c+=1
                    ul[k]= "9"
                    
        print(f"Total words    = {len(lines)}")
        print(f"Average length = {s/len(lines)}")
        print(f"Unique letters = {c}")
