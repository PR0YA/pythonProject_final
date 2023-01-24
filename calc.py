import numpy_financial as npf
from prettytable import PrettyTable
from input import *

class Calculator:
    def __init__(self, rate, cash, t):
        self.rate = rate
        self.cash = cash
        self.t = t
        self.ci = []
        self.ci2 = []
        self.tempmass = []
        self.irrmass = []
        self.pv = 0.0
        self.roisr = 0.0
        self.roi = 0.0
        self.npv = 0.0
        self.irr = 0.0
        self.pi = 0.0
        self.pdp = 0.0

    def output_1(self):
        out = PrettyTable()
        out.field_names = ["Инвестиции.", "Срок.", "Коэффициент.", "PV.", "NPV.", "PBP.", "PI.", "IRR.", "ROI."]
        out.add_row(
            [str(self.cash), str(self.t), str(self.rate), str(self.pv), str(self.npv), str(self.pdp), str(self.pi),
             str(self.irr), str(self.roi)])
        print(out)

    def massinput(self):
        print("Ввод массива")
        i = 0
        while i < self.t:
            self.ci.append(float(input()))
            i = i + 1

    def mass(self,temp):
        i = 0
        while i < self.t:
            self.ci=temp
            i = i+1

    def mass2(self):
        i = 0
        while i < self.t:
            self.ci2.append(0)
            i = i + 1

    def pvrass(self):
        i = 0
        while i < self.t:
            self.pv += round((self.ci[i]) / pow(1 + self.rate, i + 1), 2)
            self.ci2[i] = (self.ci[i]) / pow(1 + self.rate, i + 1)
            i = i + 1

    def roistr(self):
        i = 0
        while i < self.t:
            self.roisr += self.ci[i]
            i = i + 1

    def roirass(self):
        self.roi = round((self.roisr / self.t) / ((self.cash - 0) / 2), 2)

    def npvrass(self):
        self.npv = round(self.pv - self.cash, 2)

    def irrmassiv(self):
        self.irrmass=self.ci.copy()
        self.irrmass.insert(0,-self.cash)

    def irrrass(self):
        self.irr = round(npf.irr(self.irrmass), 2)

    def pirass(self):
        pipol = 0
        piotr = 0
        i = 0
        while i < self.t:
            if self.ci2[i] < 0:
                piotr += self.ci2[i]
                i = i + 1
            else:
                pipol += self.ci2[i]
                i = i + 1

        self.pi = round(pipol / (self.cash + (-piotr)), 3)

    def pdprass(self):
        i = 0
        while i < self.t:
            self.tempmass.append(0)
            i = i + 1
        self.tempmass[0] =-self.cash+self.ci2[0]

        i = 1
        while i < self.t:
            self.tempmass[i] = self.tempmass[i - 1] + self.ci2[i]
            i = i + 1

        i = 0
        k = 0
        while i < self.t:
            if self.tempmass[i] > 0:
                k = i
                break
            i = i + 1

        self.pdp = round(-self.tempmass[k - 1] / self.ci2[k] + k, 2)