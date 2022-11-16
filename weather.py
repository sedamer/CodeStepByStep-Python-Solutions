x = str(input("Input file? "))
with open(x, "r") as file:
    lines = file.read().split()
    prev = float(lines[0])
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ":",
            ")"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    mystring= []
    mynum= []
    for i in range(1, len(lines)):
        for k in range(0, len(alph)):
            if alph[k] in lines[i]:
                mystring.append(lines[i])
                lines[i]=""
        for x in range(0, len(nums)):
            if nums[x] in lines[i]:
                mynum.append(lines[i])
                lines[i] = ""
    for i in range(0, len(mynum)):
        a = float(mynum[i])
        b = float(a - prev)
        print(f"{prev} to {a}, change = {round(b,1)}")
        prev=a

