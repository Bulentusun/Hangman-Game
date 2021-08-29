import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

Hayvanlar = "kedi,köpek,kuş,civciv,timsah,aslan,ceylan,geyik,tavşan".split(",")
Sehirler  = "Adana,Bursa,Izmit,Kocaeli,Bolu,Nevşehir,Istanbul,Tekirdağ".split(",")
Meyveler  = "Elma,Kiraz,Armut,Kivi,Kavun,Portakal,Greyfurt,Erik,İncir".split(",")
Sebzeler  = "Marul,Salatalık,Roka,Kıvırcık,Domates,Biber,Patlıcan,Pırasa".split(",")

print("Welcome to  H A N G M A N ")
print(" 1 : Hayvanlar\n 2 : Sehirler \n 3 : Meyveler \n 4 : Sebzeler")
choice = input("Please choose a category: ")

word_list = []
try:
    choice = int(choice)
except:
    print("You enter a invalid character ")
    choice = int(input("Please choose a category: "))

if choice == 1:
    word_list = Hayvanlar
    print(word_list)
elif choice == 2:
    word_list = Sehirler
    print(word_list)
elif choice == 3:
    word_list = Meyveler
    print(word_list)
elif choice == 4:
    word_list = Sebzeler
    print(word_list)

chosen_word = random.choice(word_list).lower()

display = []
for x in range(len(chosen_word)):
    display += "_"
end_of_game = True
lives = 6
while end_of_game:
    guess = input(" Guess a letter ").lower()

    for position in range(len(chosen_word)) :
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = False
            print("\n** Game over **\n  * You lose * \n\n")

    if "_" not in display:
        end_of_game = False
        print("*** Congratulations ***\n  * You Win *")

    print(display)
