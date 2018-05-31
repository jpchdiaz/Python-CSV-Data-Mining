import re
#define where CSV is
datapath = "raw_data/paragraph_1.txt"

with open(datapath, 'r', encoding="UTF-8") as text:
    #read the file
    lines = text.read()
    print(lines)
    #word count
    words = len(lines.split(" "))
    #sentence count
    sentences = len(re.split("(?<=[.!?]) +", lines))
    #Average letter count
    wordlist = lines.split(" ")
    avgword = sum(len(word) for word in wordlist) / len(wordlist)
    #Average sentence length
    senlist = re.split("(?<=[.!?]) +", lines)
    avgsen = sum(len(sent.split()) for sent in senlist) / len(senlist)

#print to terminal
print("```")
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {words}")
print(f"Approximate Sentence Count: {sentences}")
print(f"Average Letter Count: {avgword}")
print(f"Average Sentence Length: {avgsen}")
print("```")
