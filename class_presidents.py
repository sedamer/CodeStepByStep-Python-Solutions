def class_presidents(x):
    with open(x, "r") as file:
        lines = file.read().split()
        sVotes = []
        jVotes = []
        sNames = []
        jNames = []
        for i in range(0, len(lines), 3):
            if lines[i + 1] == "s":
                sVotes.append(lines[i + 2])
                sNames.append(lines[i])
            elif lines[i + 1] == "j":
                jVotes.append(lines[i + 2])
                jNames.append(lines[i])
        m = sVotes.index(max(sVotes))
        k = jVotes.index(max(jVotes))
        print(f"Sophomore Class President: {sNames[m]} ({max(sVotes)} votes)")
        print(f"Junior Class President: {jNames[k]} ({max(jVotes)} votes)")
