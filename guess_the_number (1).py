import random
while True:
   player = -1
   attempts = 0
   computer = random.randint(1,50)
   while(player != computer):

      player = int(input("guess the number:"))
      attempts += 1
 
      if player > computer:
        print("lower number please")
    
      elif player < computer:
        print("higher number please")

      elif player == computer:
        print(f"you guessed it correct in {attempts} attempts, congratulations!" )
   play_again = input("do you want to play game again- (yes/no):")
   if play_again != "yes":
     break
