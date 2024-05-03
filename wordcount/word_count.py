# Import Modules
#import timeit
#import time
from   collections import defaultdict               #Method 2

# Main code
def main():
  
    # Variables
    name   = input('Enter file:')
    handle = open(name)
    #counts = dict()                                #Method 1
    counts = defaultdict(int)                       #Method 2

    # Create a dictionary of unique words and their count
    for line in handle:
        words = line.split()
        for word in words:
            #counts[word] = counts.get(word,0) + 1  #Method 1
            counts[word] += 1                       #Method 2

    #print(counts)                                  #TESTING ONLY
    
    # Find word with most counts and its count
    # word_count = None
    big_count  = None
    big_word   = None
    for word,count in counts.items():
        if big_count is None or count>big_count:
            big_word  = word
            big_count = count

    # print(big_word, big_count)                    #TESTING ONLY
    print("Word : ", big_word)
    print("Count: ", big_count)
    #END PROGRAM

if __name__ == "__main__":
    # Run main code
    main()
    print("End Program")

    # TODO: Testing timers 
    #test_code = main()
    #time_taken = timeit.timeit(stmt=test_code, number=1000)
    #print("Time to Execute: ", time_taken)
