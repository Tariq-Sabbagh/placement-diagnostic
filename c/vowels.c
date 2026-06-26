// C-1: Count the vowels in a word, case-insensitively. See ../c.md for the full task.
// Replace this comment with a one-sentence description of your approach,
// and note one sample run (input word -> count printed).

#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char word[100];
  char vowels[5] = {'u', 'i', 'a', 'o', 'e'};
  int count = 0;
  scanf("%s", word);
  for(int i = 0; word[i]; i++){
  word[i] = tolower(word[i]);
//   printf("%c" , word[i]);
  for (int j = 0;j<5;j++)
  {
    //   printf("%c" , vowels[j]);
      if(word[i]==vowels[j])
      {
          count++;
      }
  }
}


  printf("%d" , count);
    return 0;
}
