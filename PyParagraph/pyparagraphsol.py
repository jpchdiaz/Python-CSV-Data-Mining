#define where CSV is
datapath = "raw_data/paragraph_1.txt"

with open(datapath, 'r', encoding="UTF-8") as text:
    #read the file
    lines = text.read()
    print(lines)
    #word count
    words = len(lines.split(' '))
    print(f"Word Count: {words}")
    #sentence count

    #letter count per word

    #sentence length in words
