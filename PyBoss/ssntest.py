testkey = ["123-45-6789", "987-65-4321", "555-55-5555"]

def censor(ssnkey):
    asterisks = "***-**"
    for i in range(len(ssnkey)):
        words = list(ssnkey[i])
        del(words[0])
        del(words[0])
        del(words[0])
        del(words[0])
        del(words[0])
        del(words[0])
        ssnkey[i] = "".join(words)
        ssnkey[i] = asterisks + ssnkey[i]
        print(testkey)

censor(testkey)
