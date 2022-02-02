print("Welcome To Our Book Store .....")

class books:
    def __init__(self,cardNo,name):
        self.cardNo=cardNo
        self.name=name
    
    def integers(self):
         print("Please Choose Which Book Will You Like To Read And Purchase :-")
         print("We Have These Books Available Now, 1)The Harry Potter And The Sorceror's Stone  2)National Geographic  3)Rise Of British Empire - The Ultimate Rule 4)Computer Graphics And All About Computers 5) Adventures Of Tom Sawyer 6)Vikram And Betal ")
         case=int(input("Enter The Book Number You Want To Read :- "))

         if(case>6):
            print("Invalid Book Number. Enter Number Between 1 & 6 Only")
            case=int(input("Enter The Book Number You Want To Read :- "))
          
         if(case<1):
            print("Invalid Book Number. Enter Number Between 1 & 6 Only")
            case=int(input("Enter The Book Number You Want To Read :- "))




         if(case==1):
            answerV=("The Harry Potter And Sorceror's Stone")
            print("You have purchased "+answerV)
            print("That will be 980 Rupees.")
            amount=int(input("Pay The Above Amount Here :  "))
            if amount<980:
                print("Inappropriate Amount !!!!!")
                amount=int(input("Please Pay Again: "))
                if amount<980:
                    print("Inappropriate Amount !!!!!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>980:
                    new_amount=amount-980
                    print( "Thank you. Your change is Rupees "+str(new_amount))
                else:
                    print("Thank you !! Your Books Will Be Soon Delivered To You In 2-3 days")
          
     
         elif(case==2): 
            answerV=("National Geographic")
            print("You have purchased ."+answerV)
            print("That will be 1209 Rupees.")
            amount=int(input("Pay The Above Amount Here : "))
            if amount<1209:
                print("Inappropriate Amount !!!!!")
                amount=int(input("Please Pay Again: "))
                if amount<1209:
                    print("Inappropriate Amount !!!!!")
                    amount=int(input("Please Pay Again: "))
                    
                elif amount>1209:
                    new_amount=amount-1209
                    print( "Thank you. Your change is Rupees"+str(new_amount))
                else:
                    print("Thank you !! Your Books Will Be Soon Delivered To You In 2-3 days")

            


         elif(case==3):
            answerV=("Rise Of British Empire - The Ultimate Rule")
            print("You have purchased "+answerV)
            print("That will be 246.")
            amount=int(input("Pay: "))
            if amount<246:
                print("Inappropriate Amount !!!!!")
                amount=int(input("Please pay again: "))
                if amount<246:
                    print("Inappropriate Amount !!!!!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>246:
                    new_amount=amount-246
                    print( "Thank you. Your change is Rupees"+str(new_amount))
                else:
                    print("Thank you !! Your Books Will Be Soon Delivered To You In 2-3 days")
         elif(case==4):
            answerV=("Computer Graphics And All About Computers")
            print("You have purchased "+answerV)
            print("That will be 560.")
            amount=int(input("Pay: "))
            if amount<560:
                print("Inappropriate Amount !!!!!")
                amount=int(input("Please pay again: "))
                if amount<560:
                    print("Inappropriate Amount !!!!!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>560:
                    new_amount=amount-560
                    print( "Thank you. Your change is Rupees"+str(new_amount))
                else:
                    print("Thank you !! Your Books Will Be Soon Delivered To You In 2-3 days")

         elif(case==5):
            answerV=("Adventures Of Tom Sawyer")
            print("You have purchased "+answerV)
            print("That will be 270.")
            amount=int(input("Pay: "))
            if amount<270:
                print("Inappropriate Amount !!!!!")
                amount=int(input("Please pay again: "))
                if amount<560:
                    print("Inappropriate Amount !!!!!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>270:
                    new_amount=amount-270
                    print( "Thank you. Your change is Rupees"+str(new_amount))
                else:
                    print("Thank you !! Your Books Will Be Soon Delivered To You In 2-3 days")

         elif(case==6):
            answerV=("Vikram And Betal")
            print("You have purchased "+answerV)
            print("That will be 199")
            amount=int(input("Pay: "))
            if amount<199:
                print("Inappropriate Amount !!!!!")
                amount=int(input("Please pay again: "))
                if amount<199:
                    print("Inappropriate Amount !!!!!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>199:
                    new_amount=amount-199
                    print( "Thank you. Your change is Rupees"+str(new_amount))
                else:
                    print("Thank you !! Your Books Will Be Soon Delivered To You In 2-3 days")
    

            


def main():
    name=input("Enter Name : ")
    card_number=input("Insert Card Number: ")
    print("Welcome "+name+"!"+"To Our Book Store . I Hope That You Will Enjoy Your Visit ..")
    new_user=books(card_number, name)

    if card_number.strip().isdigit():
        new_user.integers()
        
    else:
        print("Please Enter Your Card Number !! It Should Be In Numbers ")
        card_number=input("Insert Card Number: ")
        if card_number.strip().isdigit():
            new_user.integers()

    
if __name__=="__main__":
    main()