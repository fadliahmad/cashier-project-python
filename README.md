# cashier-project-python

# Project Background

This is a course project. The story of this project: Friend of mine need a program that will help him to build a program that will help him grow his business. The program is a simple self-service cashier program in his supermarket that has features: 
- Customers can directly input the items purchased, the number of items purchased, and the price of the items purchased and other features.
- Customers who are not in the city can buy goods from the supermarket.

Executive summary: 

🔧 What I do:

    ⚙️ Create functions in cashier_functions.py that later will used in main.py. 
    ⚙️ Create a program in main.py. 
    📥 Importing the function cashier_function.py that we have created into main.py. 

🎯 What I want to get: 

    A program that have features: 
    
      🛒 Add item to the cart
          - Adding item to the cart including item details like total item and item price
      🖊️ Update items
          - If the user has mistakenly input the item(s) and item(s) details, they can change the inputted item(s) and the details
          - Contains updating item name, total item, and item price
      ❌ Delete items 
          - If the user has mistakenly input the item(s) and item(s) details, they can delete the inputted item(s) and the details
          - Contains delete items, and reset transactions
      🔍 Check the cart 
          - Show the inputted item(s) that is already in the cart, and showing the total price for the item(s) they have inputted
      ✔️ Check out the order
          - Show the total price of all inputted item(s), showing the discount the user will get based on the condition below, and then showing the discounted price
            - Discount condition:
            User will get 5% discount for purchases above Rp 200000
            User will get 6% discount for purchases above Rp 300000
            User will get 7% discount for purchases above Rp 500000
   
   # Flow Chart 
   ![Cashier Project drawio](https://user-images.githubusercontent.com/67184366/231992641-5c6f0e12-1a94-4f40-b461-82f6e31a977e.png)

   
   # Test Case
   
* Main Menu 
![image](https://user-images.githubusercontent.com/67184366/231978112-95b68bd2-36b6-4c05-9e05-9a8ad6cdcba1.png)

* Input Items 
![image](https://user-images.githubusercontent.com/67184366/231978550-f1275a34-b881-4a71-b19d-9428e870ac2c.png)

* Update barang 
![image](https://user-images.githubusercontent.com/67184366/231981937-e53fe1e4-e536-4fcc-8b18-391e9a5849dc.png)
    * In this case, we will try update number of item 
    ![image](https://user-images.githubusercontent.com/67184366/231982361-57d0748a-5b58-4352-8346-211cb0b7d732.png)

* Delete Items
    * Before we delete some item, we need to try to add another item to cart
    ![image](https://user-images.githubusercontent.com/67184366/231982781-f2ea0e81-8653-48bd-8431-1b0ed38c52ba.png)

    * After we got two items in cart, so we can try to delete one of them 
    ![image](https://user-images.githubusercontent.com/67184366/231982984-94f4fd25-660f-42d1-be1c-f76e46d23877.png)
    ![image](https://user-images.githubusercontent.com/67184366/231983122-e0270ac9-b9ef-4b25-85ff-1d8cfb26a213.png)

* Check cart
    * After deleted 1 item, lets check again our cart
    ![image](https://user-images.githubusercontent.com/67184366/231983360-85e6fd72-ea07-433e-a89d-105b4fb1458c.png)

* Check out our order 
![image](https://user-images.githubusercontent.com/67184366/231983520-a7e822df-223d-450f-be03-f63481ed4430.png)









