# Eurozone Economic Data Analysis
This repository contains Jupyter notebooks that visually analyze Eurozone's Economic data as provided by [the Eurostat](https://ec.europa.eu/eurostat/web/main/data/database), [the ECB](https://data.ecb.europa.eu), the [OECD](https://stats.oecd.org), and [Yahoo-Finance](https://finance.yahoo.com/). The analysis is carried out using [Pandas](https://pandas.pydata.org), [Matplotlib](https://matplotlib.org/stable/index.html) and a combination of [Eurostat](https://pypi.org/project/eurostat/), [SDMX](https://sdmx1.readthedocs.io/en/latest/), and [yfinance](https://pypi.org/project/yfinance/) libraries for data retrieval via APIs.

So far I created the following notebooks (following a given link lets you see the most recent run of its notebook, I aim to refresh results monthly):
* [Analysis of consumer prices inflation, wage inflation, level of risk-free interest rates, and GDP](./HICP_and_ECB_Rates.ipynb), plus [a similar analysis for the the US by way of comparison](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/CPI_and_Fed_Funds_Rates.ipynb)
* [Analysis of Eurozone Past, Current, and Future Riskfree Rates](Current_Riskfree_Rates_Eurozone.ipynb), plus [a similar analysis for the US](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/Current_Riskfree_Rates.ipynb)
* [Analysis of Participation, Employment, Unemployment, Job-vacancy, and Unfilled Vacancies to Population Rates](./Unemployment_and_Participation_Rates_Eurozone.ipynb), plus [a similar analysis for the US by way of comparison](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/Unemployment_and_Participation_Rates.ipynb)
* [Analysis of Eurozone Money Supply](./Money_Supply_Eurozone.ipynb), plus [a similar analysis for the US](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/Money_Supply.ipynb)
* [Analysis of Quantitative Easing and Tapering by the ECB](./Quantitative_Easing_and_Tapering_Eurozone.ipynb)
* [Analysis of Eurozone GDP, its composition by industry, and trends in its make-up](./GDP_Composition_Eurozone.ipyn), plus [a similar analysis for the US](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/GDP_Composition.ipynb)
* [Analysis of Eurozone Labor productivity (incl. comparison with that in the US)](./Labor_Productivity.ipynb)
* [Analysis of disposable income and savings rates of Eurozone individuals](./Disposable_Income_and_Savings_Eurozone.ipynb), plus [a similar analysis for the US](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/Disposable_Income_and_Savings.ipynb)
* [Analysis for Stoxx Europe 600 Banks Index](./Stock_Market_Stoxx_Europe_Banks.ipynb) & [Analysis for the AEX Index](./Stock_Market_NL.ipynb), plus [a similar analysis of US Stock Market, including various metrics on the S&P 500 Index](https://github.com/ilchen/US_Economic_Data_Analysis/blob/main/Stock_Market.ipynb)

## Requirements
You'll need python3 and pip. `brew install python` will do if you are on macOS. You can even forgo installing anything and run these notebooks in Google cloud, as I outline below.

In case you opt for a local installation, the rest of the dependencies can be installed as follows:
```commandline
python3 -m pip install -r requirements.txt
```
**NB**: I use Yahoo-Finance data in the `Current_Riskfree_Rates_Eurozone.ipynb` notebook. I switched fully to [yfinance](https://pypi.org/project/yfinance/) for working with Yahoo-Finance data due to its better maintenance and frequent new releases.

## How to run locally
If you want to run the notebooks locally on your laptop, clone the repo and `cd` into its directory, e.g.:
```commandline
git clone -l -s https://github.com/ilchen/EU_Economic_Data_Analysis.git
cd EU_Economic_Data_Analysis
```
run one of the below commands depending on which notebook you are interested in:
```commandline
jupyter notebook HICP_and_ECB_Rates.ipynb
```
or
```commandline
jupyter notebook Current_Riskfree_Rates_Eurozone.ipynb
```
or
```commandline
jupyter notebook Unemployment_and_Participation_Rates_Eurozone.ipynb
```
or
```commandline
jupyter notebook Money_Supply_Eurozone.ipynb
```
or
```commandline
jupyter notebook Quantitative_Easing_and_Tapering_Eurozone.ipynb
```
or
```commandline
jupyter notebook GDP_Composition_Eurozone.ipynb
```
or
```commandline
jupyter notebook Labor_Productivity.ipynb
```
or
```commandline
jupyter notebook Disposable_Income_and_Savings_Eurozone.ipynb
```
or
```commandline
jupyter notebook Stock_Market_Stoxx_Europe_Banks.ipynb
```
or
```commandline
jupyter notebook Stock_Market_NL.ipynb
```

## How to run in Google cloud
You can also run these notebooks in Google cloud. This way you don't need to install anything locally. This takes just a few seconds:
1. Go to [Google Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) in your browser
2. In the modal window that appears select `GitHub`
3. Enter the URL of this repository's notebook, e.g.: `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/HICP_and_ECB_Rates.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Current_Riskfree_Rates_Eurozone.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Unemployment_and_Participation_Rates_Eurozone.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Money_Supply_Eurozone.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Quantitative_Easing_and_Tapering_Eurozone.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/GDP_Composition_Eurozone.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Labor_Productivity.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Disposable_Income_and_Savings_Eurozone.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Stock_Market_Stoxx_Europe_Banks.ipynb`
or `https://github.com/ilchen/EU_Economic_Data_Analysis/blob/main/Stock_Market_NL.ipynb`
5. Click the search icon
6. Enjoy  
  In some of the notebooks I make use of additional python code I developed (e.g. `Current_Riskfree_Rates_Eurozone.ipynb`) or dependencies that are not by default provisioned in Google Colaboratory. When running these notebooks in Colaboratory, it's important to clone this repository and `cd` to it. I crated a commented out cell at the beginning of these notebooks to make it easier. Please don't forget to uncomment its content and run it first. E.g. here's one from `Current_Riskfree_Rates_Eurozone.ipynb`:
  ```commandline
# Uncomment if running in Google Colaboratory, otherwise the import of the curves module in the cell below will fail
#!git clone -l -s https://github.com/ilchen/EU_Economic_Data_Analysis.git cloned-repo
#%cd cloned-repo

# Install the latest version of pandas-datareader and yfinance
# !pip install pandas-datareader -U
# !pip install yfinance -U
  ```
