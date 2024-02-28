list1 = []
from random import randrange


stopper8 = 0
while stopper8 == 0:


    
    print ("Your songs are:")    
    for x in list1:
        print (x)


    
    print('''Enter 'add song' if you want to add a song to your playlist. Enter 'delete song' if you want to delete a song from your playlist. 
Enter 'shuffle' to print a shuffled version of your playlist.''')

    input1 = input()

    
  
  
    if input1 == "add song":
        adder = 1
        while adder == 1:
            print ("Please provide the name of the song you are adding.")
            input11 = input()
            list1.append(input11)
            for x in list1:
                print (x)
            print("Would like to add another song ? Yes/No")
            input111 = input()
            if input111 == "Yes":
                continue
            else:
                adder = 0
            print ("Your new playlist is:")
            for t in list1:
                print (t)

    
    
    elif input1 == "shuffle":
        stop = 1
        newlist = []
        while stop == 1:
            print(stop)
            appendcount = 0
            ran = randrange(0, len(list1) )
            for x in newlist:
                if x == list1[ran]:
                    break
                else:
                    appendcount += 1
            if appendcount == len(newlist):
                newlist.append(list1[ran])
            else:
                pass
                    
            if len(newlist) == len(list1):
                stop = 0
            else:
                pass
        print("Your Shuffled Playlist is:")
        print (newlist)

    
    
    elif input1 == "delete song":
        print ("What song would you like to delete enter the exact song.")
        input333 = input()
        list1.remove(input333)
        print ("Your new playlist is:")
        for g in list1:
            print (g)
    
    
    

    print("Would you like to do more things with your song list? Yes/No")
    input9 = input()
    if input9 == "Yes":
        pass
    else:
        etopper8 = 1
