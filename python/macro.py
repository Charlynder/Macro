'''
Basic Macro Economics Library
@Discription: 

@Author: Christian Alvarez
@Date: April 6, 2022
@Lincense: MIT

'''

class graph:

    def linear(b, m, x):
        y = b + (m * x)
        return y
    
    def demand(qd, qs):
        qs = qd * p
        return p


class gdp: 
    ## find GDP (Expenditure Approach)
    def gdp(Consumption, Gross, Investment, Net):
        return Consumption + Gross + Investment + Net

    ## find GDP (Income Approach)
    def gdp(TotalNationalIncome, SalesTaxes, Depreciation, NetForeignFactorIncome):
        return TotalNationalIncome + SalesTaxes + Depreciation + NetForeignFactorIncome

    ## find nominal GDP
    def nominal(PrivateConsumption, GrossInvestment, GovernmentInvestment, Exports, Imports):
        return PrivateConsumption + GrossInvestment + GovernmentInvestment + (Exports - Imports)