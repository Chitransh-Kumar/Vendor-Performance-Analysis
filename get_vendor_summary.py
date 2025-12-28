import pandas as pd
import sqlite3
import logging


def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index= False)

logging.basicConfig(
    filename= "logs/get_vendor_summary.log",
    level= logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode= "a"
)

def create_vendor_summary(conn):
    # This function will merge the various tables and get the overall summary and adds new columns to the resultant data
    vendor_sales_summary= pd.read_sql_query(""" with FreightSummary as (select VendorNumber, SUM(Freight) as FreightCost 
    from vendor_invoice group by VendorNumber), 
    
    PurchaseSummary as (select p.VendorName, p.VendorNumber, p.Brand, p.PurchasePrice,p.Description, pp.Volume, pp.Price as ActualPrice,
    SUM(p.Quantity) as TotalPurchaseQuantity, SUM(p.Dollars) as TotalPurchaseDollars 
    from purchases p join purchase_prices pp on p.Brand=pp.Brand 
    where p.PurchasePrice>0
    group by p.VendorName, p.VendorNumber, p.Brand order by TotalPurchaseDollars),
    
    SalesSummary as (select VendorNo, Brand, SUM(SalesDollars) as TotalSalesDollars, 
    SUM(SalesPrice) as TotalSalesPrice, SUM(SalesQuantity) as TotalSalesQuantity, SUM(ExciseTax) as TotalExciseTax 
    from sales group by VendorNo, Brand) 
    
    select ps.VendorName, ps.VendorNumber, ps.Brand, ps.PurchasePrice, ps.ActualPrice, ps.Volume, ps.TotalPurchaseQuantity, 
    ps.TotalPurchaseDollars, ss.TotalSalesDollars, ss.TotalSalesPrice, ss.TotalSalesQuantity, ss.TotalExciseTax, fs.FreightCost
    from PurchaseSummary as ps left join SalesSummary as ss on ps.VendorNumber= ss.VendorNo and ps.Brand= ss.Brand
    left join FreightSummary as fs on ps.VendorNumber= fs.VendorNumber order by ps.TotalPurchaseDollars desc
    
    """,conn)

    return vendor_sales_summary

def clean_data(df):
    # This function cleans data as well creates new columns in the resultant table

    # Changing data type to Float
    df['Volume']= df['Volume'].astype('float64')

    # Missing values are filled with 0
    df.fillna(0, inplace=True)

    # Trailing whitespaces are removed from categorical columns
    df['VendorName']= df['VendorName'].str.strip()

    # Creating new columns for better analysis
    df['GrossProfit']= df['TotalSalesDollars']- df['TotalPurchaseDollars']
    df['ProfitMargin']= round((df['GrossProfit'] / df['TotalSalesDollars'])*100,2)
    df['StockTurnover']= round(df['TotalSalesQuantity'] / df['TotalPurchaseQuantity'],4)
    df['SalestoPurchaseRatio']= round(df['TotalSalesDollars'] / df['TotalPurchaseDollars'],3)

    return df

if __name__== '__main__':
    # creating database connection
    conn = sqlite3.connect('inventory.db')
    
    logging. info('Creating Vendor Summary Table ..... ')
    summary_df = create_vendor_summary(conn)
    logging. info(summary_df.head())
    
    logging. info('Cleaning Data ..... ')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())
    
    logging. info('Ingesting data ..... ')
    ingest_db(clean_df,'vendor_sales_summary', conn)
    logging. info('Completed')