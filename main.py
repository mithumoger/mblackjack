from art import logo
import os
def clear():
  os.system('clear')
clear()  
print(logo)
print("welcome to blackjack game!")
name=input("please enter your name")
clear()
print(f"hello {name} my name is mithilesh, its nice to meet you")
k=int(input("to enter the game press 1 to know the rules press 2"))
clear()
if(k==2):
  input("1: Never hit a hard 17 or above. PRESS 'ENTER'")
  clear()
  input("2: Never hold on an 11 or lower. PRESS 'ENTER'")
  clear()
  input("3:Never hit a 12-16 against a dealer 4, 5 or ,6.  PRESS 'ENTER'")
  clear()
  input("4: Always hit a 12-16 against a dealer 7 or higher. PRESS 'ENTER'")
  clear()
  input("5: Always hit on soft 17 or less. PRESS 'ENTER'")
  clear()
  input("good luck.PRESS ENTER")
  clear()
import random
dictionary={'ace':''' 
 _____
|A ^  |
| / \ |
| \ / |
|  .  |
|____V|''',"two":'''  
 _____               
|2    |                                
|     |
|     |
|  v  |
|____Z|''','three':'''  
 _____           
|3    | 
| v v |
|     |
|  v  |
|____E|''','four':'''  
 _____
|4    |
| v v |
|     |       
| v v |              
|____h|  ''','five':'''  
 _____
|5    |
| ^ ^ |
|  ^  |
| ^ ^ |
|____S|    ''','six':''' 
 _____
|6    |
| v v | 
| v v | 
| v v |
|____9| ''','seven':''' 
 _____
|7    |
| v v | 
|v v v|
| v v |
|____L|
        ''','eight':''' 
 _____
|8    | 
|v v v|
| v v |
|v v v|
|____8|
       ''','nine':''' 
 _____
|9    |
|v v v|
|v v v|
|v v v|
|____6|''','ten':''' 
 _____ 
|10 v |
|v v v|
|v v v|
|v v v|
|___0I|                     
         ''',"jack":''' 
 _____  
|J  ww| 
|   {)| 
|(v)% | 
| v % | 
|__%%[|''',"king":''' 
 _____         
|K  WW|          
| /\{)|                 
| \/%%| 
|  %%%|
|_%%%>|''',"queen":''' 
 _____  
|Q  ww| 
|   {(| 
|(v)%%| 
| v%%%| 
|_%%%O|                        
       '''}
keylist=list(dictionary.keys())
vallist=list(dictionary.values())
pc=[] 
dc=[]
for i in range(2):
  p=random.randint(0,12)
  pc.append(keylist[p])
  d=random.randint(0,12)
  dc.append(keylist[d])

sump=0
sumd=0
for i in range(len(pc)):
  if(pc[i]=='ace'):
    sump=sump+11
  if(dc[i]=='ace'):
    sumd=sumd+11  
  if(pc[i]=='two'):
    sump=sump+2
  if(dc[i]=='two'):
    sumd=sumd+2
  if(pc[i]=='three'):
    sump=sump+3
  if(dc[i]=='three'):
    sumd=sumd+3
  if(pc[i]=='four'):
    sump=sump+4
  if(dc[i]=='four'):
    sumd=sumd+4
  if(pc[i]=='five'):
    sump=sump+5
  if(dc[i]=='five'):
    sumd=sumd+5
  if(pc[i]=='six'):
    sump=sump+6
  if(dc[i]=='six'):
    sumd=sumd+6
  if(pc[i]=='seven'):
    sump=sump+7
  if(dc[i]=='seven'):
    sumd=sumd+7
  if(pc[i]=='eight'):
    sump=sump+8
  if(dc[i]=='eight'):
    sumd=sumd+8
  if(pc[i]=='nine'):
    sump=sump+9
  if(dc[i]=='nine'):
    sumd=sumd+9
  if(pc[i]=='ten'):
    sump=sump+10
  if(dc[i]=='ten'):
    sumd=sumd+10
  if(pc[i]=='king'):
    sump=sump+10
  if(dc[i]=='king'):
    sumd=sumd+10
  if(pc[i]=='queen'):
    sump=sump+10
  if(dc[i]=='queen'):
    sumd=sumd+10
  if(pc[i]=='jack'):
    sump=sump+10
  if(dc[i]=='jack'):
    sumd=sumd+10                                       
if(sump==21 or sumd==21):
  if(sump==21):
    print(f"your cards are:")
    for i in range(len(pc)):
      print(dictionary[pc[i]])
    print("dealers card are")
    for i in range(len(dc)):
      print(dictionary[dc[i]])  
    print("blackjack! you won")
    quit()
  else:
    print(f"your cards are:")
    for i in range(len(pc)):
      print(dictionary[pc[i]])
    print("dealers card are")
    for i in range(len(dc)):
      print(dictionary[dc[i]]) 
    print("its a blackjack for a dealer you lose")
    quit()
print(f"your cards are:")
for i in range(len(pc)):
    print(dictionary[pc[i]])
print("dealers card are")
for i in range(1):
    print(dictionary[dc[i]]) 
print(''' _____
|* * *|
| * * |
|* * *|
| * * |
|_____|''')     
          
def hit(pc,sump):
  p=random.randint(0,12)
  pc.append(keylist[p])
  if(pc[-1]=='ace'):
    sump=sump+11
    if(sump>21):
      sump=sump-10
  
  if(pc[-1]=='two'):
    sump=sump+2
  
  if(pc[-1]=='three'):
    sump=sump+3
  
  if(pc[-1]=='four'):
    sump=sump+4
  
  if(pc[-1]=='five'):
    sump=sump+5
  
  if(pc[-1]=='six'):
    sump=sump+6
  
  if(pc[-1]=='seven'):
    sump=sump+7
  
  if(pc[-1]=='eight'):
    sump=sump+8
  
  if(pc[-1]=='nine'):
    sump=sump+9
  
  if(pc[-1]=='ten'):
    sump=sump+10
  
  if(pc[-1]=='king'):
    sump=sump+10
  
  if(pc[-1]=='queen'):
    sump=sump+10
  
  if(pc[-1]=='jack'):
    sump=sump+10  
  if(sump==21):
    print(f"your cards are:")
    for i in range(len(pc)):
      print(dictionary[pc[i]])
    print("dealers card are")
    for i in range(len(dc)):
      print(dictionary[dc[i]]) 
    print("its a blackjack,you won")
    quit()
  if(sump>21):
    print(f"your cards are:")
    for i in range(len(pc)):
      print(dictionary[pc[i]])
    print("dealers card are")
    for i in range(len(dc)):
      print(dictionary[dc[i]]) 
    print("you bust") 
    quit()
  print(f"your cards are:")
  for i in range(len(pc)):
    print(dictionary[pc[i]])
  print("dealers card are")
  for i in range(1):
    print(dictionary[dc[i]]) 
  print(''' _____
|* * *|
| * * |
|* * *|
| * * |
|_____|''')
  return(sump)    
        
c=1
while(c==1):
  c=int(input("enter 1 to hit and 2 to hold"))
  clear()
  if(c==1):
    sump=hit(pc,sump)
  clear  
if(sumd<17):
  d=random.randint(0,12)
  dc.append(keylist[d])
  if(dc[-1]=='ace'):
    sumd=sumd+11
    if(sumd>21):
      sumd=sumd-10
  
  
  if(dc[-1]=='two'):
    sumd=sumd+2
  
  if(dc[-1]=='three'):
    sumd=sumd+3
  
  if(dc[-1]=='four'):
    sumd=sumd+4
  
  if(dc[-1]=='five'):
    sumd=sumd+5
  
  if(dc[-1]=='six'):
    sumd=sumd+6
  
  if(dc[-1]=='seven'):
    sumd=sumd+7
  
  if(dc[-1]=='eight'):
    sumd=sumd+8
  
  if(dc[-1]=='nine'):
    sumd=sumd+9
  
  if(dc[-1]=='ten'):
    sumd=sumd+10
  
  if(dc[-1]=='king'):
    sumd=sumd+10
  
  if(dc[-1]=='queen'):
    sumd=sumd+10
  
  if(dc[-1]=='jack'):
    sumd=sumd+10     
  if(sumd==21):
    print(f"your cards are:")
    for i in range(len(pc)):
      print(dictionary[pc[i]])
    print("dealers card are")
    for i in range(len(dc)):
      print(dictionary[dc[i]]) 
    print("its a blackjack for the dealer you lose")
    quit()  
  if(sumd>21):
    print(f"your cards are:")
    for i in range(len(pc)):
      print(dictionary[pc[i]])
    print("dealers card are")
    for i in range(len(dc)):
      print(dictionary[dc[i]]) 
    print("dealer busts") 
    quit()         
if(sump>sumd):
  print(f"your cards are:")
  for i in range(len(pc)):
    print(dictionary[pc[i]])
  print("dealers card are")
  for i in range(len(dc)):
      print(dictionary[dc[i]]) 
  print("you won")
  quit()
elif(sumd>sump):
  print(f"your cards are:")
  for i in range(len(pc)):
    print(dictionary[pc[i]])
  print("dealers card are")
  for i in range(len(dc)):
    print(dictionary[dc[i]]) 
  print("you lose")
  quit()
elif(sumd==sump):
  print(f"your cards are:")
  for i in range(len(pc)):
    print(dictionary[pc[i]])
  print("dealers card are")
  for i in range(len(dc)):
      print(dictionary[dc[i]]) 
  print("its a draw")
  quit()
  
  
    

  
  