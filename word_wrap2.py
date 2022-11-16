def word_wrap2(a,a1):
    with open(a) as f:
        with open(a1,"w")as out:
            lines=f.readlines()
            lines=[k.replace('\n','') for k in lines]
            count=0
            for i in range(0,len(lines)):
                if len(lines[i])>59:
                    for j in range(0,len(lines[i])):
                        out.write(lines[i][j])
                        count+=1
                        if count==60:
                            out.write("\n")
                            count=0
                    out.write("\n")
                    count=0
                else:
                    for k in lines[i]:
                        out.write(k)
                    out.write("\n")
