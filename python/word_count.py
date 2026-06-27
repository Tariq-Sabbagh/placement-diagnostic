# Task 1: Word Frequencies. See ../python.md for the full task.
# Replace this comment with a one-sentence description of your approach.
#
# Reads word_count_input.txt (next to this file) and prints the 3 most
# frequent words, most frequent first, as "word: count".


def main():
    # TODO: read python/word_count_input.txt, tally each lowercased word
    # (strip surrounding punctuation), and print the top 3.
    word = open("word_count_input.txt")
    string = word.read().lower()
    string = string.replace(',' ,'')
    string = string.replace('.','')
    words = string.split()
    dic = {key: 0 for key in words}
    for w in words:
        dic[w]+=1
        # print(dic[w])
    
    diclist = list(dic.items())
    n = len(diclist)
    # print(diclist)
    for i in range(n-1):
      for j in range(n-i-1):
        if diclist[j][1] < diclist[j+1][1]:
          diclist[j], diclist[j+1] = diclist[j+1], diclist[j]
        elif diclist[j][1] == diclist[j+1][1]:
           if diclist[j][0][0] > diclist[j+1][0][0]:
              diclist[j], diclist[j+1] = diclist[j+1], diclist[j]
    
    for i in range(3):
     print(diclist[i][0])


if __name__ == "__main__":
    main()
