'''
Basic MacroEconomics Library
Author: Christian Alvarez
Date: Nov 3, 2021
Licience: MIT
'''


## the name of the library is "Econ"
class Econ:
    ## finds the nominal gdp 
    def nominalGDP(DurableGoods, NondurableGoods, Services, Structures, ChangeInInventories):
        ## calculate rGDP
        gdpReg = float(DurableGoods + NondurableGoods + Services + Structures + ChangeInInventories)
        return float((DurableGoods / gdpReg) * 100),  float(gdpReg)

    ## find the government spending amount 
    def govSpend(GDP, Consumpion, Investment, Exports, Imports):
        return float(GDP - Consumpion - Investment - (Exports - Imports))

    ## find the consumpion spending amount
    def consSpend(gdp, government, investment, exports, imports):
        return float(gdp - government - investment - (exports - imports))

    ## find the consumpion spending amount
    def investSpend(gdp, government, consumpion, exports, imports):
        return float(gdp - government - consumpion - (exports - imports))

    ## finds the total gdp 
    def totalGDP(Consumption, Investment, Government, Exports, Imports):
        return float(Consumption + Investment + Government + (Exports - Imports))

    ## finds the real gdp 
    def realGDP(nominalGDP, priceIndex):
        return float(nominalGDP / (priceIndex / 100))

    ## finds the gdp per capita 
    def perCapita(realgdp, population):
        return float(realgdp / population)

    ## finds the exchange rate 
    def exchangerate(foreignGDP, foreignValue, usValue):
        return float(foreignGDP / (foreignValue / usValue))

    ## find the population based on the the gdp & the per capita amount
    def findPopulation(realgdp, perCapita):
        return realgdp / perCapita

## needs debug
    ## finds the new percentage of the gdp
    """
    def newpercent(new_gdp, old_gdp):
        ## find the new percentage
        if new_gdp < old_gdp: ## if the old gdp is greater then the new gdp
            
        else: 
        
        return newGDPpercent
    """

    ## find the trade Balance
    def tradeBalance(goods, services, incomePayment, unilateralTransfer):
        return (goods) + (services) + (incomePayment) + (unilateralTransfer)
    def tradeBalanceA(goods, services, incomePayment, unilateralTransfer):
        return (goods) + (services) + (incomePayment)


    ## find the saving value
    def findSavings(trade, savings, investment, government, difference):
        return trade + government - investment - (savings + difference)


    def findInvestment(trade, savings, investment, government, difference):
        return savings + government - investment - (trade + difference)