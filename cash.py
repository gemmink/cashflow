def notnumeric(pnum): #figure out if numeric in crude way
    if type(pnum) == int or type(pnum) == float:
        return 0
    else:
        return 1


class cashflow:
    def __init__(self,cost,cashf): #intilalize, takes cost, a cash flow in the form of list
        if notnumeric(cost):
            print("warning invalid cost")
        if type(cashf)==list:
            for i in cashf:
                if notnumeric(i):
                    print("warning invalid cashflow")
        else:
            print("invalid cashflow")
        self.cost = cost
        self.cashf = cashf
        self.pvr = -1
        self.irrvar=-1
    def pv(self,dis): #present value
        if self.pvr >= 0:
            return self.pvr
        i = 0
        cashsm =0
        for x in self.cashf: 
            cashsm+= x/(dis**i)
            i+=1
        self.pvr = cashsm
        return self.pvr
    def irr(self): #brute force calculation of IRR
        if self.irrvar > 0:
            return self.irrvar
        irr = 0
        cashsm = 0
        s=0
        for i in range(1,100000):
            irr = irr + .0001
            for x in self.cashf:
                cashsm+= x/(irr**s)
                s+=1
            if round(cashsm,1)== self.cost:
                print(irr)
                self.irrvar = irr
                return irr
            cashsm=0
            s=0
        self.irrvar = -3
        return 0 #if nothing happens return 0 as IRR
