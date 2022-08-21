# Home price webscraper zillow.com

Given a list of US home addresses inside an excel file, the program will go online and mimic the actions of a human to get the price estimates. It will also generate a new excel file with the prices for each address.

The project started from a freelancer.com request. A client was looking for someone to webscrape the zillow price estimator for a bunch of addreses.


I left an example input .xlsx and output. but basically it looks like:

INPUT file:
|OWNER 1 LABEL NAME| PROPERTY ADDRESS | PROPERTY CITY | PROPERTY STATE | PROPERTY ZIP CODE | Zestimate |
| ---------------- | ---------------- | ------------- | -------------- | ----------------- | --------- |
|    John Doe      | 53 Marguerite Dr |    Neskowin   |       OR       |        97149      |           |
|    John Doe2     | Somewhere in US  |    Nocity12   |       MA       |        65109      |           |
|    John Doe3     | Again in the US  |    Sometown   |       NY       |        02146      |           |
|    John Doe4     | Still in the US  |  Another city |       MN       |        75412      |           |


OUTPUT file:
|OWNER 1 LABEL NAME| PROPERTY ADDRESS | PROPERTY CITY | PROPERTY STATE | PROPERTY ZIP CODE | Zestimate |
| ---------------- | ---------------- | ------------- | -------------- | ----------------- | --------- |
|    John Doe      | 53 Marguerite Dr |    Neskowin   |       OR       |        97149      | 2,252,000 |
|    John Doe2     | Somewhere in US  |    Nocity12   |       MA       |        65109      | 1,925,000 |
|    John Doe3     | Again in the US  |    Sometown   |       NY       |        02146      |   950,000 |
|    John Doe4     | Still in the US  |  Another city |       MN       |        75412      | 6,524,000 |


During the scraping process, in the terminal information is printed regrading the duration per process, at which iteration the program is and an ETA in minute.
See the example terminal output below:

```python
Program will start in 10 seconds. Please access 
https://www.zillow.com/how-much-is-my-home-worth/

duration:  4.554298 seconds, iteration 1 / 199. ETA 15 mins
duration:  4.558668 seconds, iteration 2 / 199. ETA 14 mins
duration:  4.549930 seconds, iteration 3 / 199. ETA 14 mins
duration:  4.545249 seconds, iteration 4 / 199. ETA 14 mins
duration:  4.544992 seconds, iteration 5 / 199. ETA 14 mins
duration:  4.540376 seconds, iteration 6 / 199. ETA 14 mins
duration:  4.530943 seconds, iteration 7 / 199. ETA 14 mins
duration:  4.519912 seconds, iteration 8 / 199. ETA 14 mins
duration:  4.557332 seconds, iteration 9 / 199. ETA 14 mins
duration:  4.546223 seconds, iteration 10 / 199. ETA 14 mins
duration:  4.561372 seconds, iteration 11 / 199. ETA 14 mins
duration:  4.564254 seconds, iteration 12 / 199. ETA 14 mins
duration:  4.566027 seconds, iteration 13 / 199. ETA 14 mins
duration:  4.557139 seconds, iteration 14 / 199. ETA 14 mins
duration:  4.550050 seconds, iteration 15 / 199. ETA 13 mins
duration:  4.554814 seconds, iteration 16 / 199. ETA 13 mins
duration:  4.556885 seconds, iteration 17 / 199. ETA 13 mins
duration:  4.551654 seconds, iteration 18 / 199. ETA 13 mins
duration:  4.540095 seconds, iteration 19 / 199. ETA 13 mins
duration:  4.549372 seconds, iteration 20 / 199. ETA 13 mins
duration:  4.556773 seconds, iteration 21 / 199. ETA 13 mins
duration:  4.562690 seconds, iteration 22 / 199. ETA 13 mins
duration:  4.535247 seconds, iteration 23 / 199. ETA 13 mins
duration:  4.559623 seconds, iteration 24 / 199. ETA 13 mins
duration:  4.561735 seconds, iteration 25 / 199. ETA 13 mins
duration:  4.547571 seconds, iteration 26 / 199. ETA 13 mins
duration:  4.564267 seconds, iteration 27 / 199. ETA 13 mins
duration:  4.536597 seconds, iteration 28 / 199. ETA 12 mins
duration:  4.557407 seconds, iteration 29 / 199. ETA 12 mins
duration:  4.561116 seconds, iteration 30 / 199. ETA 12 mins

```