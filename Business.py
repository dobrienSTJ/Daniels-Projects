#'Business Accounts Learning Aid' Version 1.0
#This program was created,developed and Published by Daniel O'Brien through 'Open Coding' in St. Josephs Secondary School Rush. He can be contacted on Github @dobrienSTJ
#The Consoles used in the development were IDLE 3 for Windows 7 Home Version and Pythonista 3.0 on iPad for iOS 9.2
#THe Programming Language used was Python 3.5.1
#This software is freely available under open source/creative commons license to personal and commercial user on Gist by Github @ https://gist.github.com/dobrienSTJ/ec5769f40c04e63214b73d1ce6b3625c
#A native Python (.py) File can be found @ https://drive.google.com/a/stjosephsrush.com/file/d/0B9C83zgJFhw7bFJaLWJIR3pFMHc/view?usp=sharing
#© Daniel O' Brien 2016 @ https://gist.github.com/dobrienSTJ
#A useful Help/Support Document can be found @ https://drive.google.com/a/stjosephsrush.com/file/d/0B9C83zgJFhw7dTFXVzM3Y0xoTVE/view?usp=sharing
#This program is constantly being developed and improved and version history can be freely viewed
#Please send any suggestions for improvements/changes in the program/code development on the Github comments!
def business_accounts():
    print("The first value you enter into the Trading Account is the Sales")
    total_sales=(int(input("Please enter your Sales")))
    print("Now that you have entered your sales value please enter any sales returns you may have, if you have none just enter 0")
    salesreturns=(int(input("Please enter your sales returns")))
    sales = total_sales-salesreturns
    print("Less Cost Of Sales")
    print("We have now got our Total Sales so we will move onto calculating how much money was spent on buying stock for the business")
    opening_stock=(int(input("Please enter your Opening Stock")))
    total_purchases=(int(input("Please enter your Purchases")))
    purchasesreturns=(int(input("Please enter your Purchases Returns")))
    purchases = total_purchases-purchasesreturns
    carriage_in=(int(input("Please enter your Carriage In")))
    import_duties=(int(input("Please enter your Total Import Duties")))
    cost_of_goods_available_for_sale = opening_stock+purchases+carriage_in+import_duties
    print("We now have our 'Cost of Goods Available For Sale' we will use the Closing Stock to get our 'Cost Of Sales' as it is stock we have not sold, while the")
    closing_stock=(int(input("Please enter your Closing Stock")))
    cost_of_sales = cost_of_goods_available_for_sale-closing_stock
    print (cost_of_sales)
    print("We now hav0e our Cost Of Sales(the full cost of selling all the goods in the year), We now take that away from the Total sales to find out the Gross Profit")     
    print("COST OF GOODS AVAILABLE FOR SALE - CLOSING STOCK")
    gross_profit = sales-cost_of_sales
    print("We now have our Gross Profit, printed below")
    print (gross_profit)
    print("Now that we have our Gross profit we can ADD our GAINS and TAKE AWAY our Expenditure Below in the next piece of code")
    adjustments = ["Expenses","Gains"]
    print (adjustments)
    for item in adjustments:
        if item == "Expenses":
            print("For Expenses DUE is ADDED and PREPAID is SUBTRACTED")
        if item == "Gains":
            print("For Gains DUE is ADDED and PREPAID is SUBTRACTED")

    print("Please remember these rules as hey are very important!")
    rent_receivable=(int(input("Please enter any Rent Receivable")))
    debtors=(int(input("Please enter any debtors fees")))
    tax_rebate=(int(input("Please enter any tax rebate fees")))
    due_gains=(int(input("Please enter any 'Due' for all of gains")))
    prepaid_gains=(int(input("Please enter any 'Prepaid' for all of gains")))
    gains = rent_receivable+debtors+tax_rebate+due_gains-prepaid_gains
    print("We have now added Gains to the Gross Profit and will continue with the Expenditure")
    print("GROSS PROFIT + GAINS")      
    net_profit = gross_profit+gains
    print("Less Expenditure")
    print("We now take away Expenditure from the Gross profit!")
    print("GROSS PROFIT - EXPENDITURE")
    print("Expenditure = Wages, Carriage Out, Rent, Eletricity, Fuel, Gas, Insurance, Computers, Telephones, Broadband etc.")
    wages=(int(input("Please enter any wages")))
    carriage_out=(int(input("Please enter any Carriage Out")))
    rent=(int(input("Please enter any Rent")))
    eletricity=(int(input("Please enter any Eletricity")))
    fuel=(int(input("Please enter any Fuel")))
    gas=(int(input("Please enter any Gas")))
    insurance=(int(input("Please enter any Insurance")))
    computers=(int(input("Please enter any Computers")))
    telephones=(int(input("Please enter any Telephones")))
    broadband=(int(input("Please enter any Broadbands")))
    bank_overdraft=(int(input("Please enter any Bank Overdraft Fees")))
    due_expenses=(int(input("Please enter any 'Due' for all of expenses")))
    prepaid_expenses=(int(input("Please enter any 'Prepaid' for all of expenses")))
    expenditure = wages+carriage_out+rent+eletricity+fuel+gas+insurance+computers+telephones+broadband+bank_overdraft+due_expenses+prepaid_expenses
    net_profit = net_profit-expenditure
    print("We have now added up all of our Expenses so will take this away from the Gross Profit")
    print (net_profit)
    print("Less Dividends")
    print("We will now take away Dividends and add Profit And Loss Balance")
    print("NET PROFIT+PROFIT AND LOSS BALANCE-DIVIDENDS")
    profit_and_loss_balance=(int(input("Please enter the Profit and Loss Balance")))
    percentage_dividends=(int(input("Please enter the percentage of dividends")))
    dividends = net_profit/100*percentage_dividends
    reserves = net_profit-dividends+profit_and_loss_balance
    print (reserves)
    print("We now have the Reserves which is the end of the Trading,Profit and Loss Appropiation account")
    print("We will now move onto the Balance Sheet which is written out in Record Book 3")
    print("First we will add the Fixed Assets, Below")
    print("We will also add on any depreciation on the fixed assets, if there is any....")
    print("'any fixed asset'-DEPRECIATION")
    motor_vehicles=(int(input("Please enter any Motor Vehicle assets")))
    motor_vehicles_depreciation=(int(input("Please enter any Derpreciation")))
    motor_vehicles = motor_vehicles-motor_vehicles_depreciation
    land=(int(input("Please enter any Land assets")))
    land_depreciation=(int(input("Please enter any Derpreciation")))
    land = land-motor_land_depreciation
    buildings=(int(input("Please enter any bulding assets")))
    buildings_depreciation=(int(input("Please enter any Derpreciation")))
    buildings = buildings-buildings_depreciation
    equipment=(int(input("Please enter any Equipment assets")))
    equipment_depreciation=(int(input("Please enter any Derpreciation")))
    equipment = equipment-equipment_depreciation
    machinery=(int(input("Please enter any Machinery assets")))
    machinery_depreciation=(int(input("Please enter any Derpreciation")))
    machinery = machinery-machinery_depreciation
    fixtures_fittings=(int(input("Please enter any Fixtures/Fittings assets")))
    print("We have added up all the Fixed Assets so we will no move onto the Current Assets")
    print("We are now at the Current Assets which you will input below")
    fixed_assets = motor_vehicles+land+builings+equipment+machinery+fixtures_fittings
    current_assets = debtors+closing_stock
    creditors=(int(input("Please enter any Creditors")))
    current_liabilties = bank_overdraft+creditors
    print("We now have added up all the Current Liabilties")
    working_capital = current_assets-current_liabilties
    print("We will now calculate the Working Capital be the calculations below")
    print("CURRENT ASSETS-CURRENT LIABILTIES")
    net_assets = fixed_assets+working_capital
    print("We have now have the Net Assets after getting the Working Capital")
    print("WORKING CAPITAL+FIXED ASSETS")
    print (net_assets)
    print("We will now find out how the business was financed by inputting the authorised and issued shares of the company")
    print("Financed By: Ordinary Share Capital")
    authorised=(int(input("Please enter the Authorised Shares")))
    issued=(int(input("Please enter the Issued Shares")))
    capital_employed = issued+reserves
    print("We now have the final part of the Balance sheet, the Capital Employed, Calculations Below")
    rint("ISSUED SHARES+RESERVES(from Trading Account)")
    print (capital_employed)
    print("I hope this Business Accounts learning aid has helped you learn something new, ask your Business Teacher if you have any further questions!!!!!!")

print(" _____________________ ")
print("|  _________________  |")
print("| | PROGRAM NAME    | |")
print("   Business Accounts   ")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")
print(" by Daniel O'Brien 2016")
print("Programed On Python 3.5.1")
print("Welcome to the Trading, Profit and Loss Appropiation Account and Balance Sheet Calculation Program")
business_accounts()
print("Thank You for using the program, I hope it has helped you in any way possible on learning Business Accounts!!")
end_of_program=input("END OF PROGRAM")
#©Daniel O'Brien 2016, Free for Open Source Programing use from gist.github.com
#All Info at start of Program or on Help Docs
