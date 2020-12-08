wordDict = {"ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready"],
            "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"],
            "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"],
            "blank": ["wait", "right", "okay", "middle", "blank"],
            "nothing": ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing"],
            "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes"],
            "what": ["uhhh", "what"],
            "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh"],
            "left": ["right", "left"],
            "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"],
            "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"],
            "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"],
            "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"],
            "press": ["right", "middle", "yes", "ready", "press"],
            "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"],
            "you are": ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"],
            "your": ["uh uh", "you are", "uh huh", "your"],
            "you're": ["you", "you're"],
            "ur": ["done", "u", "ur"],
            "u": ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"],
            "uh huh": ["uh huh"],
            "uh uh": ["ur", "u", "you are", "you're", "next", "uh uh"],
            "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"],
            "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"],
            "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"],
            "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"],
            "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"],
            "like": ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like"]}
while True:
    words = input("Enter the words: ").split(", ")
    base = words[0].lower()
    if base == "yes" or base == "nothing" or base == "led" or base == "they are":
        second = words[3].lower()
        for word in wordDict[second]:
            if word in words:
                print(word)
                break
    elif base == "ur":
        second = words[1].lower()
        for word in wordDict[second]:
            if word in words:
                print(word)
                break
    elif base == "first" or base == 'okay' or base == 'c':
        second = words[2].lower()
        for word in wordDict[second]:
            if word in words:
                print(word)
                break
    elif base == "blank" or base == 'read' or base == 'red' or base == 'you' or base == "you're" or base == 'their':
        second = words[4].lower()
        for word in wordDict[second]:
            if word in words:
                print(word)
                break
    elif base == "reed" or base == 'leed' or base == "they're":
        second = words[5].lower()
        for word in wordDict[second]:
            if word in words:
                print(word)
                break
    elif base == "display" or base == 'says' or base == 'no' or base == 'lead' or base == 'hold on' or base == 'you are' or base == 'there' or base == 'see' or base == 'cee':
        second = words[6].lower()
        for word in wordDict[second]:
            if word in words:
                print(word)
                break
    