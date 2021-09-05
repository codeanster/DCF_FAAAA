class FA_dataset():
    def __init__(self,api_key,ticker):
        self.api_key = api_key
        self.ticker = ticker
        self.df_save_path = f'data/{ticker}_7_Years.csv'
   
        import FundamentalAnalysis as fa
        import pandas as pd
        
        years = ['2014','2015','2016','2017','2018','2019','2020']
        api_key = self.api_key
        ticker = self.ticker
        # Collect the Balance Sheet statements
        balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")

        # Collect the Income Statements
        income_statement_annually = fa.income_statement(ticker, api_key, period="annual")

        # Collect the Cash Flow Statements
        cash_flow_statement_annually = fa.cash_flow_statement(ticker, api_key, period="annual")

        #values for the balance sheet
        total_current_assets = balance_sheet_annually[years].loc['totalCurrentAssets']
        total_assets = balance_sheet_annually[years].loc['totalAssets']
        total_current_liabilities = balance_sheet_annually[years].loc['totalCurrentLiabilities']
        total_liabilities = balance_sheet_annually[years].loc['totalLiabilities']
        retained_earnings = balance_sheet_annually[years].loc['retainedEarnings']
        total_stockholders_equity = balance_sheet_annually[years].loc['totalStockholdersEquity']

        #values for the income statement
        revenue =  income_statement_annually[years].loc['revenue']
        cost_of_revenue = income_statement_annually[years].loc['costOfRevenue']
        gross_profit = income_statement_annually[years].loc['grossProfit']
        gross_profit_ratio = income_statement_annually[years].loc['grossProfitRatio']
        interest_expense = income_statement_annually[years].loc['interestExpense']
        depreciation = income_statement_annually[years].loc['depreciationAndAmortization']
        operating_income = income_statement_annually[years].loc['operatingIncome']
        operating_income_ratio = income_statement_annually[years].loc['operatingIncomeRatio']
        net_income = income_statement_annually[years].loc['netIncome']
        net_income_ratio = income_statement_annually[years].loc['netIncomeRatio']
        eps = income_statement_annually[years].loc['eps']
        number_of_shares = income_statement_annually[years].loc['weightedAverageShsOut']

        #values for the cashflow statement
        dividends = cash_flow_statement_annually[years].loc['dividendsPaid']
        capital_expenditures = cash_flow_statement_annually[years].loc['capitalExpenditure']
        stock_repurchased = cash_flow_statement_annually[years].loc['commonStockRepurchased']
        debt_repayment = cash_flow_statement_annually[years].loc['debtRepayment']
        free_cash_flow = cash_flow_statement_annually[years].loc['freeCashFlow']
        net_cash_operating = cash_flow_statement_annually[years].loc['netCashProvidedByOperatingActivities']
        net_cash_investing = cash_flow_statement_annually[years].loc['netCashUsedForInvestingActivites']
        net_cash_finance = cash_flow_statement_annually[years].loc['netCashUsedProvidedByFinancingActivities']
        property_and_plant_investments = cash_flow_statement_annually[years].loc['investmentsInPropertyPlantAndEquipment']

        #create dataframe with data collected
        df = pd.DataFrame()
        df['total_current_assets'] = total_current_assets
        df['total_assets'] = total_assets
        df['total_current_liabilities'] = total_current_liabilities
        df['total_liabilities'] = total_liabilities
        df['retained_earnings'] = retained_earnings
        df['total_stockholders_equity'] = total_stockholders_equity
        df['revenue'] = revenue
        df['cost_of_revenue'] = cost_of_revenue
        df['gross_profit'] = gross_profit
        df['gross_profit_ratio'] = gross_profit_ratio
        df['interest_expense'] = interest_expense
        df['depreciation'] = depreciation
        df['operating_income'] = operating_income
        df['operating_income_ratio'] = operating_income_ratio
        df['net_income'] = net_income
        df['net_income_ratio'] = net_income_ratio
        df['eps'] = eps
        df['number_of_shares'] = number_of_shares
        df['dividends'] = dividends
        df['capital_expenditures'] = -capital_expenditures
        df['stock_repurchased'] = stock_repurchased
        df['debt_repayment'] = debt_repayment
        df['free_cash_flow'] = free_cash_flow
        df['net_cash_operating'] = net_cash_operating
        df['net_cash_investing'] = net_cash_investing
        df['net_cash_finance'] = net_cash_finance
        df['propery_and_plant_investments'] = property_and_plant_investments

        #save dataframe
        df.to_csv(f'data/{ticker}_7_Years.csv')
        print(df)
        print(f'Created df: data/{ticker}_7_Years.csv')
        return
  
    def plot_metrics(self):
        import plotly.express as px
        import pandas as pd
        metrics = ['net_income','operating_income','number_of_shares','revenue','capital_expenditures','total_stockholders_equity']
        df = pd.read_csv(self.df_save_path)
        df.rename(columns={'Unnamed: 0':'year'},inplace=True)

        fig = px.line(title=self.ticker)

        for metric in metrics:
            fig.add_scatter(x = df['year'], y = df[metric] , name = metric)

        fig.show()
        return 