'''
GDP Finder Library

Author: Christian Alvarez
Date: Nov 3, 2021
Licience: MIT
'''

class GDPfinder:
    ## finds the nominal gdp 
    def nominalGDP(DurableGoods, NondurableGoods, Services, Structures, ChangeInInventories):
        ## calculate rGDP
        gdpReg = float(DurableGoods + NondurableGoods + Services + Structures + ChangeInInventories)
        ## convert to percentage
        pGDP = float((DurableGoods / gdpReg) * 100)

        return float(pGDP),  float(gdpReg)

    ## find the government spending amount 
    def govSpend(GDP, Consumpion, Investment, Exports, Imports):
        govSpend = float(GDP - Consumpion - Investment - (Exports - Imports))

        return float(govSpend)

    ## find the consumpion spending amount
    def consSpend(gdp, government, investment, exports, imports):
        consSpend = float(gdp - government - investment - (exports - imports))

        return float(consSpend)

    ## find the consumpion spending amount
    def investSpend(gdp, government, consumpion, exports, imports):
        investSpend = float(gdp - government - consumpion - (exports - imports))

        return float(investSpend)

    ## finds the total gdp 
    def totalGDP(Consumption, Investment, Government, Exports, Imports):
        ## calculate tGDP
        gdpTotal = float(Consumption + Investment + Government + (Exports - Imports))

        return float(gdpTotal)

    ## finds the real gdp 
    def realGDP(nominalGDP, priceIndex):
        ## find the real gdp
        realgdp = nominalGDP / (priceIndex / 100)

        return float(realgdp)

    ## finds the gdp per capita 
    def perCapita(realgdp, population):
        percapita = float(realgdp / population)

        return percapita

    ## finds the exchange rate 
    def exchangerate(foreignGDP, foreignValue, usValue):
        covertedgdp = float(foreignGDP / (foreignValue /usValue))

        return covertedgdp

    ## find the population based on the the gdp & the per capita amount
    def findPopulation(realgdp, perCapita):
        population = realgdp / perCapita
        return population

## needs debug
    ## finds the new percentage of the gdp
    """
    def newpercent(new_gdp, old_gdp):
        ## find the new percentage
        if new_gdp < old_gdp: ## if the old gdp is greater then the new gdp
            
        else: 
        
        return newGDPpercent
    """