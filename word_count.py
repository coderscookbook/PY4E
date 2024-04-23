# Import Modules
import timeit
import time
from   collections import defaultdict

# Main code
def main():
  
    # name   = input('Enter file:') # using python3, change to line below
    name   = input('Enter file:')
    handle = open(name)
    #counts = dict()
    counts = defaultdict(int)
    
    # Create a dictionary of unique words and their count
    for line in handle:
        words = line.split()
        for word in words:
            #counts[word] = counts.get(word,0) + 1
            counts[word] += 1

    print(counts)
    word_count = None
    big_count  = None
    big_word   = None
    for word,count in counts.items():
        if big_count is None or count>big_count:
            big_word  = word
            big_count = count

    # print(big_word, big_count)
    print("Word : ", big_word)
    print("Count: ", big_count)

    

if __name__ == "__main__":
    main()