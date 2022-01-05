# SuperPy

> "A Python command line tool for your supermarket business needs."

Run the file named `super.py` in your terminal with the `--help` argument to see a quick summary and reminder of the arguments you can use.

```
python super.py --help
```

# Documentation

## buy
Adds a product you buy from a supplier to your store's inventory.  
| arg       | description                      | format         |
| --------- | -------------------------------- | -------------- |
| -e        | expiration date of the product   | YYYY-MM-DD     |
| -n        | name of the product              | text           |
| -p        | price in euros payed to supplier | decimal number |


#### Example:
Buying a banana from a supplier for price € 0.50. The banana has an expiration date of december 31, 2021.

```
python super.py buy -n banana -p 0.50 -e 2021-12-31
```
This will add the banana to the list of bought products for your store.  
Note: The buy date will be automatically set to the program's 'current date', which should normally be today's date. See documentation on `setdate`.

```
    Product   banana     
─────────────────────────
        id:   1         
  buy date:   2021-12-28 
 buy price:   € 0.50    
 exp. date:   2021-12-31    
  ```

## Sell
Selling a product from your store's inventory to a customer.

| arg       | description                      | format         |
| --------- | -------------------------------- | -------------- |
| -n        | name of the product              | text           |
| -p        | price in euros payed by customer | decimal number |


#### Example:
Buying a banana from a supplier for price € 0.50. The banana has an expiration date of december 31, 2022.

```
python super.py buy -n banana -p 0.50 -e 2022-12-31
```
This will add the banana as a product to the list of bought products for your store:

```
    Product   banana     
─────────────────────────
        id:   16         
  buy date:   2022-01-05 
 buy price:   € 0.50    
 exp. date:   2022-12-31    
  ```