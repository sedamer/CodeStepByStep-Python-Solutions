def input_stats(x):
    with open(x , "r") as file:
        lines = file.read().splitlines()
        s = 0
        c = len(lines)
        v=1
        l = []
        for i in range(len(lines)):
            a = str(lines[i])
            m= len(a)
            print(f"Line {v} has {m} chars")
            s+=m
            v+=1
            l.append(m)
        print(f"{c} lines; longest = {max(l)}, average = {s/c}")
