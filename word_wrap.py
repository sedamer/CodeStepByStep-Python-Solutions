def word_wrap(a):
    with open(a, "r" ) as file :
        lines = file.read().splitlines()
        for line in lines:
            myfunction(line)
def myfunction(line):
    s = len(line)
    i=0
    j=60
    while s >= 60 :
        print(line[i:j])
        s-=60
        i+=60
        j+=60
    while 0 <= s< 60 :
        print(line[i:])
        break
