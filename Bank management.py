print("="*20)

customerNames = ['vanitha','hema','kavya','srikanya','dheeksha']
customerPins = ['0123','2575','7275','2312','5049']
customerBalances = ['10000','20000','45000','12000','50000']
deposition = 0
withdrawl = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0
# this statement below helps the program to run continuosly.
while True:
    # os.system("cls")
    print("====================================")
    print("----WELCOME TO TIMES BANK----"       )
    print("************************************")
    print("=<< 1. open a new account        >>=")
    print("=<< 2. withdraw money            >>=")
    print("=<< 3. Deposit Money             >>=")
    print("=<< 4. Check Customers & Balance >>=")
    print("=<< 5. Exit/Quit                 >>=")
    print("************************************")
    # the below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu:")
    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        # the line below will take no:of customers from the user
        NOC = eval(input("Number of Customers :"))

        i = i + NOC
        # the if condition will restrict the number of new account
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - NOC
        else:
            # the while loop will run according to the no:of customers
            while counter_1 <= i:
                # these few lines will take information from customer
                name = input("Enter Fullname:")
                customerNames.append(name)
                pin = str(input("please enter a pin of your choice:"))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("please input a value to deposit to start an account:"))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2],end=" ")
                print("-/Rs")
                counter_1 = counter_1+1
                counter_2 = counter_2+1
                print("\nYour name is added to customers system")
                print("your pin is added to customer system")
                print("your balance is added to customer system")
                print("----- NEW ACCOUNT CREATED SUCESSFULLY!----")
                print("\n")
                print("your name is available on the customers list now:")
                print(customerNames)
                print("\n")
                print("Note! please remember the Name and pin")
                print("======================================")
                # this statement below helps the user to go back to the start of the program(main menu)
                mainMenu = input("please press enter key to go back to main menu to perform amother function or exit....")
    elif choiceNumber =="2":
        j = 0
        print("Choice number 2 is selected by the customer")
        # this while loop will prevent the user using the account if the username or pin is wrong
        while j < 1:
            k = -1
            name = input("please input name:")
            pin = input("please input pin:")
            # this while loop will keep the function running when variable k is smaller than length of the
            #customerNames list.
            while k < len(customerNames) -1:
                k = k+1
                # these two if conditions find where both the name and pin matches.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j+1
                        #these few statement would show the balance taken from the list.
                        print("your current Balance:",end="")
                        print(customerBalances[k],end="")
                        print("-/Rs\n")
                        balance= (customerBalances[k])
                        # statement below would take the amount to withdraw from user.
                        withdrawl = eval(input("Input value to Withdraw:"))
                        # the if condition below would look whether the withdraw is greater than the balance
                        if withdrawl > balance:
                            #this statement below would take a deposition from the customer.
                            deposition = eval(input("please Deposit a higher value because your Balance mentioned above is not enough:"))

                            # these few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end="")
                            print("-/Rs\n") # 1000-500=500
                            balance = balance - withdrawl
                            print("-\n")
                            print("------WITHDRAWL SUCCESSFULL!------")
                            customerBalances[k]= balance
                            print("Your New Balance:",balance,end="")
                            print("-/Rs\n\n")
                        else:
                             # else condition mentioned above is to do withdrawl if the balance is greater than the 
                             # withdrawl amount.
                             balance= balance - withdrawl
                             # these few statement would update the values in the list and show it to the customer.
                             print("\n")
                             print("--------WITHDRAWL SUCCESSFULL!")
                             customerBalances[k]= balance
                             print("Your New Balance:",balance,end=" ")
                             print("-/Rs\n\n")
                    if j < 1:
                        # the if condition above would work when the pin or the name is wrong
                        print("Your name and pin does not match!\n")
                        break
                    # this statement below helps the user to go back to the start of the program(main menu).
                    mainMenu = input("please press enter key to go back to main menu to perform another function or exit...")
                    

    elif choiceNumber =="3":
        print("Choice number 3 is selected by the customer")
        n=0
        #the while loop below would work when the pin or username is wrong
        while n < 1:
            k = -1
            name = input("please input name:")
            pin = input("please input pin:")
            # the while loop below will keep the function running to find the correct user.
            while k < len(customerNames) -1:
                k = k+1
                # the two if conditions below would find whether both the pin and name is correct
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n+1
                        # these statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        # this statement below takes the deposition from the customer.
                        deposition = eval(input("Enter the value you want to deposit:"))
                        balance = balance + deposition # 1000+500=1500
                        customerBalances[k]= balance
                        print("\n")
                        print("-------DEPOSITION SUCCESSFULL!------")
                        print("Your New Balance:", balance, end=" ")
                        print("-/Rs\n\n")
                        if n < 1:
                            print("Your name and pin does not match! \n")
                            break
                        # this statement below helps the user to go back to the start of the program(main menu)
                        mainMenu = input("please press enter key to go back to main menu to perform another function or exit....")
    elif choiceNumber =="4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below:")
        print("\n")
        # the while loop below will keeping running until all the customers and balances are shown
        while k <= len(customerNames)-1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =",customerBalances[k], end =" ")
            print("-/Rs")
            print("\n")
            k = k+1
            # this statement below helps the user to go back to the start of the program(main menu).
            mainMenu = input("please press enter key to go back to main menu to perform another function or exit....")

    elif choiceNumber== "5":
        # these statements would be just showed to the customer
        print("choice number 5 is selected by the customer")
        print("THANK YOU FOR USING OUR BANKING SYSTEM!")
        print("\n")
        print("come again")
        print("BYE BYE..")
        break
    else:
        # this else function above would work when a wrong function is chosen
        print("Invalid option is selected by the customer")
        print("please Try again!")
        # this statement below helps the user to go back to the start of the program(main menu)
        mainMenu = input("please press enter key to go back to main menu to perform another function or exit....")






                    

                             
                        
                         

                        
                                    

                             


                    
            





                       
