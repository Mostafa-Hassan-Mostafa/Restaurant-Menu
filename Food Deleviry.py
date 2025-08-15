#Resturant Menu
print("""  Resturant Menu
      1.El Talaa Duet Offer 172 LE
Your choice of 2 talaa chicken or beef sandwiches, medium fries and 1 can of soda
      2.King El Sa3ada 149 LE
Single sandwich with one piece of chicken served with medium fries, coleslaw and 1 can of soda
      3.Wrap El Sa3ada 216 LE
4 wrap sandwiches spicy or original
      4.Wrap Box 158 LE
Spicy wrap sandwich or original, 1 piece of spicy or original chicken served with medium fries, coleslaw and 1 can of soda
""")
#Accepting user input
item = input("Choose offer number (1,2,3,4) from the menu: ")
if item in ['1','2','3','4'] :
    quantity=int(input("Enter offer Quantity: "))
#The process
    if item=='1' :
        item_name="El Talaa Duet Offer"
        price=172
    elif item=='2' :
        item_name="King El Sa3ada"
        price=149
    elif item=='3' :
        item_name="Wrap El Sa3ada"
        price=216
    elif item=='4' :
        item_name="Wrap Box"
        price=158
    Total=price*quantity
    Tax=Total*0.10
    Delivery_fees=15
    Final_price=Total+Tax+Delivery_fees
#Dispaly the output
    output=f"                Receipt                       " \
       f"\n              Date:12/11/2024           " \
       f"\nItem:{item_name} \tPrice:{price} \tQuantity:{quantity}" \
       f"\nTotal:{Total} \nTax:{Tax} \nDelivery:{Delivery_fees} \nFinal:{Final_price}" \
       f"\nThank You for ordering from us"
    print(output)
else:
     print("You should choose form 1,2,3 or 4")