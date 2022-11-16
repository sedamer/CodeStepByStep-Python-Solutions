def word_wrap3(a):
    with open(a) as f:

        lines = f.readlines()
        lines = [k.replace('\n', '') for k in lines]
        count = 0

        for i in range(0, len(lines)):
            if len(lines[i]) <= 60:
                print(lines[i], end="")

            else:
                texts = lines[i].split(" ")
                for text in texts:
                    if count+len(text)<=60:
                        print(text,end=" ")
                        count+=len(text)+1
                    else:
                        print()
                        print(text,end=" ")
                        count=len(text)+1

                count = 0
            print()
