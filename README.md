# zillow.com-home-price-webscraper

Given a list of US home addresses inside an excel file, the program will go online and mimic the actions of a human to get the price estimates. It will also generate a new excel file with the prices for each address.

The project started from a freelancer.com request. A client was looking for someone to webscrape the zillow price estimator for a bunch of addreses.


I left an example input .xlsx and output. but basically it looks like:

INPUT file:


```
|OWNER 1 LABEL NAME| PROPERTY ADDRESS | PROPERTY CITY | PROPERTY STATE | PROPERTY ZIP CODE | Zestimate |
|==================|==================|===============|================|===================|===========|
|     John Doe     | 53 Marguerite Dr |    Neskowin   |       OR       |        97149      |
|------------------|------------------|---------------|----------------|-------------------|-----------|
|    John Doe2     | Somewhere in US  |    Nocity12   |       MA       |        65109      |
|------------------|------------------|---------------|----------------|-------------------|-----------|
|    John Doe3     | Again in the US  |    Sometown   |       NY       |        02146      |
|------------------|------------------|---------------|----------------|-------------------|-----------|
|    John Doe4     | Still in the US  |  Another city |       MN       |        75412      |
|------------------|------------------|---------------|----------------|-------------------|-----------|
```
