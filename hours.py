def hours(a = input()):
    with open (a, "r") as file:
        content =file.readlines()
        print(f"Input file? {a}")
        for line in content :
            process_employee(line),
            
def process_employee(line):
    parts=line.split()
    id =parts[0]
    isim=parts[1]
    sum = 0
    count = 0
    for i in range (2, len(parts)):
        sum+= float(parts[i])
        count+=1
        
    avg=round(sum/count, 1)
    print(isim+" (ID#"+str(id)+") worked "+ str(round(sum , 1))+" hours" +" ("+str(avg)+"/day)")
