# SuperPy

SuperPy is a Python command line tool for your supermarket business needs.

### Features summary:

| option                   | description                                       |
| ------------------------ | ------------------------------------------------- |
| [`buy`](#buy)            | adds a product to the list of bought products     |
| [`sell`](#sell)          | logs that a product has been sold                 |
| [`pull`](#pull)          | pulls products by expiration date                 |
| [`setdate`](#setdate)    | sets the date that the program perceives as today |
| [`sales`](#sales)        | generates a sales report with revenue and profit  |
| [`inventory`](#inventory)| shows the inventory on a particular date          |
| [`help`](#help)          | shows the argparse (built in) help message        |

# Documentation

## buy
Adds a product you buy from a supplier to your store's inventory.  
| arg  | description                      | input format         |
| ---- | -------------------------------- | -------------- |
| `-e` | expiration date of the product   | YYYY-MM-DD     |
| `-n` | name of the product              | text           |
| `-p` | price in euros payed to supplier | decimal number |


#### Example:
Buying a banana from a supplier for price € 0.30. The banana has an expiration date of december 31, 2021:

```
python super.py buy -n banana -p 0.30 -e 2021-12-31
```
This will add the banana to the file that contains the details of all bought products for your store.  
Note: The 'buy date' will be automatically set to the program's 'current date', which should normally be today's date. See documentation on [`setdate`](#setdate) .

```
    Product   banana     
─────────────────────────
        id:   1          
  buy date:   2021-12-28 
 buy price:   € 0.30     
 exp. date:   2021-12-31 
```

## sell
Sells a product with a specific name from your store's inventory to a customer.

| arg  | description                      | input format   |
| ---- | -------------------------------- | -------------- |
| `-n` | name of the product              | text           |
| `-p` | price in euros payed by customer | decimal number |

When you use `sell`, the program will try to find available products with the specified name "banana" from the list of bought products. If found, the product that has the earliest expiration date will be selected and logged as sold.
- Only products that not have been sold and have an expiration date of today or later will be considered available.
- If an available product has been found:
    - sale transaction details will be logged to the `sold.csv` file
    - product and sale transaction details will be showed
    - the number of available items with the same product name that are now left in inventory will be showed

#### Example:
Selling a banana to a customer for price € 0.50:

```
python super.py sell -n banana -p 0.50
```

Output:
```
    Product   banana     
─────────────────────────
        id:   1          
  buy date:   2021-12-28 
 buy price:   € 0.30     
 exp. date:   2021-12-31 
```
```
Product 'banana' with id 1 sold for € 0.50 on 2021-12-28
```
```
Number of available 'banana' items left is now: 0
```

## pull
Pulls all products from the inventory of current date that have an expiration date that is ***equal to or earlier than*** the specified date. Pulling will log the concerning products to `sold.csv` with a price of `0`.  
This feature can be used to quickly identify and 'remove' from inventory all products that should not be for sale anymore. 

| arg  | description                                                     | input format   |
| ---- | --------------------------------------------------------------- | -------------- |
| `-d` | date to compare to the expiration date of products in inventory |  YYYY-MM-DD    |


#### Example:
Pull all products with an expiration date of 2021-12-31 or earlier:

```
python super.py pull -d 2021-12-31
```

Output:  

*Pulled products*
| Id  | Name | Buy Date | Buy Price | Expiration Date |
| -: | - | - | -: | - |
| 1 | banana  | 12021-12-28  |   € 0.30 | 2021-12-31 |
```
Number of products pulled: 1
Total costs for pulled products: € 0.30
```


## setdate
Sets the date that the program perceives as today. The set date will be used to get and show relevant data in the program.

| arg  | description    | input format   |
| ---- | -------------- | -------------- |
| `-d` | date to be set | YYYY-MM-DD     |

#### Examples:
Set the date to december 27, 2022:

```
python super.py setdate -d 2022-12-27
```
Remove a previously set date and make the program use the local operating system date:

```
python super.py setdate -d local
```

## sales
Generates a sales report with revenue and profit. Date range needs to be specified.

| arg  | description         | input format  |
| ---- | ------------------- | ------------- |
| `-f` | from date           | YYYY-MM-DD    |
| `-t` | to date (exclusive) | YYYY-MM-DD    |


#### Example:
Show the sales report for the month December of 2021.

```
python super.py sales -f 2021-12-01 -t 2022-01-01
```

Output:
| From date  | To Date (excl.) | Items sold | Item Sell Price Average | Revenue (Sales) | Total Costs (Buy) | Profit (Revenue - Costs) |
| - | - | -: | -: |-: | -: | -: |
| 2021-12-01 | 2022-01-01  | 1  |   € 0.5 | € 0.50 | € 0.30 |  € 0.20 |


## inventory
Shows a product report of the inventory on a particular date.

| arg  | description               | input format  | input alternative      |
| ---- | ------------------------- | ------------- | ---------------------- |
| `-d` | date to show inventory of | YYYY-MM-DD    | today, t, yesterday, y |

Input can be a date (YYYY-MM-DD) or `today` (short: `t`)  or `yesterday` (short: `y`).  
If no input is given, the inventory of current date will be shown.

In the Expiration Date column, if the expiration date is later than tomorrow, the color will be green.  
There will be a colored warning if expiration date is:
 - <span style="color:gold">Tomorrow!</span> *(yellow)*
 - <span style="color:orange">Today!</span> *(orange)*
 - <span style="color:red">**Expired!**</span> *(red)*

#### Example:
Show inventory of today using the short input (`t`):
```
python super.py inventory t
```
Output:
| Id  | Name | Buy Date | Buy Price | Expiration Date |
| -: | - | - | -: | - |
| 1 | banana  | 12021-12-28  |   € 0.30 | 2021-12-31 |


## help
Shows the `argparse` module's (built in) help message the with a summary of which arguments can be used.
#### Example:
```
python super.py --help
```

Output:
```
usage: super.py [-h] [-n NAME] [-p PRICE] [-e EXPIRATION_DATE] [-d DATE] [-f FROM_DATE] [-t TO_DATE] function

super.py is a supermarket inventory and sales reporting application

positional arguments:
  function              options: buy, sell, pull, inventory, sales, setdate

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  name of a product
  -p PRICE, --price PRICE
                        price in euros (note: use decimal point as seperator for cents)
  -e EXPIRATION_DATE, --expiration_date EXPIRATION_DATE
                        expiration date of a product (use format YYYY-MM-DD)
  -d DATE, --date DATE  date to use with functions: inventory, pull, setdate (use format YYYY-MM-
                        DD)
  -f FROM_DATE, --from_date FROM_DATE
                        starting date for a date range (use format YYYY-MM-DD)
  -t TO_DATE, --to_date TO_DATE
                        end date (exclusive) for a date range (use format YYYY-MM-DD)
```