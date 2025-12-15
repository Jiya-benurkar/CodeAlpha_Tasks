import random

words_list=["game","hangman","winter","python","programs"]

word_to_be_guessed=random.choice(words_list)

guessed_word=["_"]*len(word_to_be_guessed)

guessed_letters=[]

incorrect_guess_limit=6
attempts_left=incorrect_guess_limit

print("Welcome to Hangman!🎮")

print("Guess the word, one letter at a time")
print("You have",attempts_left,"attempts\n")

while attempts_left>0 and "_" in guessed_word:
  print("Word so far:"," ".join(guessed_word))
  print("Letters Guessed so far:",guessed_letters)
  letter_guessed=input("Enter a letter:").lower()
  
  if len(letter_guessed)!=1 or not letter_guessed.isalpha():
     print("Please enter a single alphabet\n")
     continue
  
  if letter_guessed in guessed_letters:
     print("You have Already Guesssed this Letter!\n")   
     continue
  
  guessed_letters.append(letter_guessed)

  if letter_guessed in word_to_be_guessed:
     print("Correct Letter Guessed!!✅\n")
     for i in range(len(word_to_be_guessed)):
        if word_to_be_guessed[i]==letter_guessed:
           guessed_word[i]=letter_guessed

  else:
    attempts_left=attempts_left-1
    print("Wrong Guess!❌")
    print("Attempts Left:",attempts_left)      

if "_" not in guessed_word:
   print("Yayy!🥳")
   print("^_^You have guessed the word:",word_to_be_guessed)
else:
   print("Game Over!💀 You were unable to guess the word :(")
   print("The correct word was:",word_to_be_guessed)



