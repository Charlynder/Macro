'''
GDP Finder API

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

        return str(pGDP) + '% - $' + str(gdpReg)

    ## find the government spending amount 
    def govSpend(GDP, Consumpion, Investment, Exports, Imports):
        govSpend = float(GDP - Consumpion - Investment - (Exports - Imports))

        return "$" + str(govSpend)

    ## find the consumpion spending amount
    def consSpend(gdp, government, investment, exports, imports):
        consSpend = float(gdp - government - investment - (exports - imports))

        return "$" + str(consSpend)

    ## find the consumpion spending amount
    def investSpend(gdp, government, consumpion, exports, imports):
        investSpend = float(gdp - government - consumpion - (exports - imports))

        return "$" + str(investSpend)

    ## finds the total gdp 
    def totalGDP(Consumption, Investment, Government, Exports, Imports):
        ## calculate tGDP
        gdpTotal = float(Consumption + Investment + Government + (Exports - Imports))

        return "$" + str(gdpTotal)

    ## finds the real gdp 
    def realGDP(nominalGDP, priceIndex):
        ## find the real gdp
        realgdp = nominalGDP / (priceIndex / 100)
        return "$" + str(round(realgdp, 1))

    ## finds the new percentage of the gdp
    def newpercentGDP(new_gdp, old_gdp):
        ## find the new percentage
        if new_gdp < old_gdp:
            newGDPpercent = ((- new_gdp) / old_gdp) * 100
        else:
            newGDPpercent = ((new_gdp - old_gdp) / old_gdp) * 100
        
        return str(int(newGDPpercent)) + "%"