# SuperPy assignment Report

In this report of about 300 words I have described three technical of my implementation of the SuperPy application.

## 1. Rich module
In the SuperPy application I have implemented some of the classes from an external Python module named [Rich](https://rich.readthedocs.io) that can be used for displaying *rich* text with advanced styling and layout:

- [Console](https://rich.readthedocs.io/en/stable/console.html): advanced control over terminal formatting
- [Panel](https://rich.readthedocs.io/en/stable/panel.html): create borders around text or other renderables
- [Prompt](https://rich.readthedocs.io/en/stable/prompt.html): ask a user for input and loop until a valid response is received
- [Table](https://rich.readthedocs.io/en/stable/tables.html): tabular data displayed in the terminal
- [Style](https://rich.readthedocs.io/en/stable/style.html): text color and styling

 ## 2. Additional feature: sales report prompt
For the `sales` report function I thought some might like the ability to show details like revenue and profit for multiple date ranges in one table overview. I designed this feature so the user will be asked if another date range should be added to the report. In this way, for example, the sales results for different months or weeks can be compared.

 ## 3. Additional feature: pull products
I thought it would be nice to have a function in the program that can quickly identify and 'remove' from inventory all products that should not be for sale anymore. 

In a real world situation in a supermarket this could for example be done at the end of the day, so the next day can be started with a 'clean' inventory, without products that have expired or will expire soon. In supermarkets this activity is referred to as *pulling* products from sale. 

In SuperPy when using the `pull` command, the user can choose the date for which SuperPy will pull all products that have an expiration date up to and including that date.

I have designed the pull feature to show as output:
- an overview of the pulled products in a table
- how many products were pulled in total
- the total of costs of the pulled products

# Extra: suggestion of commands for demonstration
- In the git repository the `bought.csv` file already has some data to play with.
- The setdate command has been used to set the date to 2022-01-01 for demonstration purposes.
- The *NOTE! ...* message will be displayed if the current date is set to a date other than the local operating system date.

Try these commands consecutively for a demo of what the program can do:
```
python super.py inventory -d today
```
```
python super.py inventory -d yesterday
```
```
python super.py inventory -d 2021-12-22
```
```
python super.py buy -n apple -p 0.30 -e 2022-01-15
```
```
python super.py sell -n milk -p 1.09
```
```
python super.py pull -d 2022-01-01
```
```
python super.py inventory
```
```
python super.py sell -n pumpkin -p 3.00
```
```
python super.py sales -f 2021-12-22 -t 2022-01-02
```
```
python super.py setdate -d local
```