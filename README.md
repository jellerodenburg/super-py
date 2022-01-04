# SuperPy

> "A Python command line tool for your supermarket business needs."

Run the file named `super.py` in your terminal with the `--help` argument to see a quick summary and reminder of the arguments you can use.

```
python super.py --help
```

# Options

## Buy
Adds a product you buy from a supplier to your store's inventory.  
| arg       | description                      | format         |
| --------- | -------------------------------- | -------------- |
| -e        | expiration date of the product   | YYYY-MM-DD     |
| -n        | name of the product              | text           |
| -p        | price in euros payed to supplier | decimal number |


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

## Sell
Adds product you buy from suppliers to your store's inventory.  
| arg       | description                      | format         |
| --------- | -------------------------------- | -------------- |
| -e        | expiration date of the product   | YYYY-MM-DD     |
| -n        | name of the product              | text           |
| -p        | price in euros payed to supplier | decimal number |


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