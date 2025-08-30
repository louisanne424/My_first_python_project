bucketlist = []
while True:
    print('\nBUCKETLIST MENU')
    print('1. Add activities')
    print('2. View my Bucketlist')
    print('3. Update my Bucketlist')
    print('4. Remove item from Bucketlist')
    print('5. Exit app\n')
    choice = input('kindly enter the corresponding number to navigate the app').strip()

    if choice == '1':

        while True:
            wish = input('enter your bucketlist activity(type done when finished) >').lower()
            if wish == 'done':  
                break
            bucketlist.append(wish)
        if not bucketlist:
                print('\nyour bucketlist is empty')
        else:
                print('bucketlist updated successfully\n')



    elif choice == '2':
        print('\nthis is your bucketlist.....')
        if not bucketlist:
                print('\nyour bucketlist is empty\n')
        else:
            for i, item in enumerate(bucketlist,start=1):
                print(f'\n{i}.{item}')



    elif choice == '3':
        print('\nkindly add the new activities on your list (type done when finished)')
        while True:
            new_list = input('>').lower()
            if new_list == 'done':
                break
            bucketlist.append(new_list)
          
        


        
    elif choice == '4':
        New_task = input('enter task to remove').lower()
        if New_task in bucketlist:
                bucketlist.remove(New_task)
                print('\nyayyyy you completed yet another task you are awesome')
            
        else:
            print('\nitem not found')




    elif choice == '5':
        print('Goodbye!\n')
        break
    else:
        print('invalid selection')
