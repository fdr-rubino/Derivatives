import scipy.optimize as optimize
import math as m
import numpy as np

class bond:
    """
    The formula used to compute the P of the bond is the one of the Annuity
    --------------
    coupon: coupon paid by the bond
    N: Number of payments the bond has to make until Maturity
    t: number of days from the last coupon payment
    T: 360 or 365 according to the convention used (if annual); 180 or 182.5 (if coupon is semiannual)
    rf: risk free
    spread: bond spread over the rf
    """
    def __init__(self, coupon, N, t, T):
        self.coupon = coupon
        self.N = N
        self.t = t
        self.T = T

    def bond_ytm(self, price, guess=0.05):
        ytm_func = lambda y: \
        ((self.coupon / y ) * (( (1 + y) ** (self.N - self.t/self.T)) - 1) / ( (1 + y) ** (self.N - self.t/self.T) ))\
        + 100/(1+y)**(self.N - self.t/self.T) - price
        return round(optimize.newton(ytm_func, guess), 4)

    def price(self, rf, spread):
        PV = ((self.coupon / (rf+spread)) * (( (1+rf+spread) ** (self.N - self.t/self.T)) - 1) /
              ( (1 +rf+spread) ** (self.N - self.t/self.T))) + \
             100/(1+rf+spread)** (self.N - self.t/self.T)
        return round(PV, 4)

    def price_flat(self, rf, spread):
        PV = ((self.coupon / (rf + spread)) * (((1 + rf + spread) ** (self.N - self.t / self.T)) - 1) /
              ((1 + rf + spread) ** (self.N - self.t / self.T))) + \
             100 / (1 + rf + spread) ** (self.N - self.t / self.T)
        AI = self.coupon * (self.t/self.T)  #this is the accrued interest matured until that time

        return round((PV - AI), 4)

    def duration(self, rf, spread):
        """ Compute the Macauley duration of a bond"""
        p_full = self.price(rf, spread)
        macauley_dur = []

        for n in range(1, self.N+1):
            if n < self.N:
                mac_dur = (n - self.t / self.T) * (
                (self.coupon / ((1 + rf + spread) ** (n - self.t / self.T)) / p_full))
                macauley_dur.append(mac_dur)
            else:
                mac_dur = (n - self.t / self.T) * (
                    ((100 + self.coupon) / ((1 + rf + spread) ** (n - self.t / self.T)) / p_full))
                macauley_dur.append(mac_dur)  #this is for the last payment

        return round(sum(macauley_dur), 4)

    def mod_duration(self, rf, spread):
        macauley = self.duration(rf, spread)
        return round(macauley/(1+rf+spread), 2)

    def price_sensitivity(self, rf, spread, delta_spread):
        mod_duration = self.mod_duration(rf, spread)
        delta_p = - mod_duration * delta_spread
        return round(delta_p * 100, 4)  #expressed in percentage

    def convexity(self, rf, spread):
        p_full = self.price(rf, spread)
        PV_minus  = ((self.coupon / (rf + spread - 0.001)) * (((1 + rf + spread - 0.001) ** (self.N - self.t / self.T)) - 1) /
              ((1 + rf + spread - 0.001) ** (self.N - self.t / self.T))) + \
             100 / (1 + rf + spread - 0.001) ** (self.N - self.t / self.T)

        PV_plus = ((self.coupon / (rf + spread + 0.001)) * (
                    ((1 + rf + spread + 0.001) ** (self.N - self.t / self.T)) - 1) /
                    ((1 + rf + spread + 0.001) ** (self.N - self.t / self.T))) + \
                   100 / (1 + rf + spread + 0.001) ** (self.N - self.t / self.T)

        conv = (PV_minus + PV_plus - 2*p_full) / ((0.001**2) * p_full)

        return round(conv, 4)  #PV_minus, PV_plus, p_full

    def adj_price_sensitivity(self, rf, spread, delta_spread):
        mod_duration = self.mod_duration(rf, spread)
        convexity = self.convexity(rf, spread)
        delta_p = - mod_duration * delta_spread + (0.5 * convexity * (delta_spread**2))
        return round(delta_p * 100, 4)



b = bond(5, 5, 0, 360)
print(b.duration(0.02, 0.04))
