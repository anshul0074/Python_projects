print('Welcome to Tic Tac Toe!')


m=int(input('For single player press 1 ; For dual player press 2  '))

if m==2:
  import os
  import time 
  import random
 
  board =[" "," "," "," "," "," "," "," "," "," "]

  def print_board():
    print ("  |  |  ")
    print (""+board[1]+" |"+board[2]+" |"+board[3]+"")
    print ("  |  |  ")
    print ("--|--|--")
    print (""+board[4]+" |"+board[5]+" |"+board[6]+"")
    print ("  |  |  ")
    print ("--|--|--")
    print (""+board[7]+" |"+board[8]+" |"+
    board[9]+"")
    print ("  |  |  ")

  print_board()

  while True:
    os.system('cls')
    print_board()
    #turn of X;
    choice =input('Please choose empty space for X ')
    choice =int(choice)
    if board[choice]==" ":
       board[choice] ="X"
    else:
      print('Sorry space is not empty')
      time.sleep(1)

    if  (board[1]=="X" and board[2]=="X" and    board[3]         =="X")     or \
        (board[4]=="X" and board[5]=="X" and    board[6]=="X") or \
        (board[7]=="X" and board[8]=="X" and    board[9]=="X") or \
        (board[1]=="X" and board[4]=="X" and    board[7]=="X") or \
        (board[2]=="X" and board[5]=="X" and    board[8]=="X") or \
        (board[3]=="X" and board[6]=="X" and    board[9]=="X") or \
        (board[1]=="X" and board[5]=="X" and    board[9]=="X") or \
        (board[3]=="X" and board[5]=="X" and    board[7]=="X"):
        os.system('cls')
        print_board()
        print('X Won!')
        break

    os.system('cls')
    print_board()

    flag=True
    for i in range (1,10):
      if board[i]==" ":
        flag=False
        break

    if flag==True:
      print('Its a DRAW..')
      break

    #turn of O;  
    choice =input('Please choose empty space for O ')
    choice =int(choice)
    if board[choice]==" ":
      board[choice] ="O"
    else:
      print('Sorry space is not empty')
      time.sleep(1)

    if  (board[1]=="O" and board[2]=="O" and    board[3]         =="O")     or \
        (board[4]=="O" and board[5]=="O" and    board[6]=="O") or \
        (board[7]=="O" and board[8]=="O" and    board[9]=="O") or \
        (board[1]=="O" and board[4]=="O" and    board[7]=="O") or \
        (board[2]=="O" and board[5]=="O" and    board[8]=="O") or \
        (board[3]=="O" and board[6]=="O" and    board[9]=="O") or \
        (board[1]=="O" and board[5]=="O" and    board[9]=="O") or \
        (board[3]=="O" and board[5]=="O" and    board[7]=="O"):
        os.system('cls')
        print_board()
        print('O Won!')
        break
          
    flag=True
    for i in range (1,10):
      if board[i]==" ":
        flag=False
        break

    if flag==True:
      print('Its a DRAW..')
      break
    

elif m==1:
  import random
  import os
  import time 
 
  board =[" "," "," "," "," "," "," "," "," "," "]

  def print_board():
    print ("  |  |  ")
    print (""+board[1]+" |"+board[2]+" |"+board[3]+"")
    print ("  |  |  ")
    print ("--|--|--")
    print (""+board[4]+" |"+board[5]+" |"+board[6]+"")
    print ("  |  |  ")
    print ("--|--|--")
    print (""+board[7]+" |"+board[8]+" |"+
    board[9]+"")
    print ("  |  |  ")

  print_board()

  while True:
    os.system('cls')
    print_board()
    #turn of X;
    choice =input('Please choose empty space for X ')
    choice =int(choice)
    if board[choice]==" ":
       board[choice] ="X"
    else:
      print('Sorry space is not empty')
      time.sleep(1)

    if  (board[1]=="X" and board[2]=="X" and    board[3]         =="X")     or \
        (board[4]=="X" and board[5]=="X" and    board[6]=="X") or \
        (board[7]=="X" and board[8]=="X" and    board[9]=="X") or \
        (board[1]=="X" and board[4]=="X" and    board[7]=="X") or \
        (board[2]=="X" and board[5]=="X" and    board[8]=="X") or \
        (board[3]=="X" and board[6]=="X" and    board[9]=="X") or \
        (board[1]=="X" and board[5]=="X" and    board[9]=="X") or \
        (board[3]=="X" and board[5]=="X" and    board[7]=="X"):
        os.system('cls')
        print_board()
        print('X Won!')
        break

    os.system('cls')
    print_board()

    flag=True
    for i in range (1,10):
      if board[i]==" ":
        flag=False
        break

    if flag==True:
      print('Its a DRAW..')
      break
    #turn of O;  
    def cpu():
      choice =random.choice([1,2,3,4,5,6,7,8,9])
      if board[choice]==" ":
        board[choice] ="O"
      else:
        cpu()
    time.sleep(1)
    cpu()

    if  (board[1]=="O" and board[2]=="O" and    board[3]         =="O")     or \
        (board[4]=="O" and board[5]=="O" and    board[6]=="O") or \
        (board[7]=="O" and board[8]=="O" and    board[9]=="O") or \
        (board[1]=="O" and board[4]=="O" and    board[7]=="O") or \
        (board[2]=="O" and board[5]=="O" and    board[8]=="O") or \
        (board[3]=="O" and board[6]=="O" and    board[9]=="O") or \
        (board[1]=="O" and board[5]=="O" and    board[9]=="O") or \
        (board[3]=="O" and board[5]=="O" and    board[7]=="O"):
        os.system('cls')
        print_board()
        print('O Won!')
        break
  
    flag=True
    for i in range (1,10):
      if board[i]==" ":
        flag=False
        break

    if flag==True:
      print('Its a DRAW..')
      break

else:
  print('Invalid Input')
