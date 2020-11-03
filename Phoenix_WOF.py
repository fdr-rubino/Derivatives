import math as m
# import matplotlib.pyplot as plt
import random
import numpy as np
import time
start_time = time.time()

# ST = S0 * m.exp((mu - (sigma**2) / 2) + (sigma * m.sqrt(T) * random.random()) )
#mu is set as it were the rf; I preferred to replace it with r here
S1, K1, r, sigma_1, T = 19, 18, 0.02, 0.4, 5
S2, K2, r, sigma_2, T = 19, 18, r, 0.4, T
H1 = S1 * 0.60
H2 = S2 * 0.60

trials = 1000
#put = []
#put_perc = []
# --------------------- ZCB Pricer ----------------------------
swap5Y = -0.0032  #alternatively to the EUR3m 
EUR3m = -0.0022
Bank_spread5Y= 0.0058
r_rate = EUR3m + Bank_spread5Y

def ZCB(maturity=T):
    zcb = 100 / ((1+r_rate) ** maturity)
    return round(zcb, 4)

ZCB_price = ZCB(maturity=T)

# --------------------- PDI Pricer: MC Simulation ----------------------------

def montecarlo_pricer (S1,S2):
    """ It uses a montecarlo simulation. ST is generated via the exponential GBM.
    An if statement is commenced inside the for, in order to compute the value of the put
    depending on the result of ST. All the results are appended in the list put.
    Then an average put price is computed"""

    list_put = []
    list_put_percent = []

    for i in range(1000):
        put = []  #after the first "MC-1000 simulation", clean the put vector
        put_perc = []  #after the first "MC-1000 simulation", clean the put perc vector

        for t in range(trials):
            ST_1 = S1 * m.exp(((r - (sigma_1 ** 2) / 2) * T) + (sigma_1 * random.normalvariate(0, 1) * m.sqrt(T)))
            ST_2 = S2 * m.exp(((r - (sigma_2 ** 2) / 2) * T) + (sigma_2 * random.normalvariate(0, 1) * m.sqrt(T)))

            if (ST_1/S1) < (ST_2/S2) and ST_1 < H1:  #I have to compare the performance
                p = (K1 - ST_1) * m.exp(-r * T)
                p_percent = (p / S1) * 100

            elif (ST_2/S2) < (ST_1/S1) and ST_2 < H2:
                p = (K2 - ST_2) * m.exp(-r * T)
                p_percent = (p / S2) * 100

            else:
                p = 0
                p_percent = 0

            put.append(p)
            put_perc.append(p_percent)

        put_price = sum(put) / len(put)  #at the end of each "MC-1000 simulation", compute mean put price
        put_percent = (sum(put_perc) / len(put_perc))  #at the end of each "MC-1000 simulation", compute mean put percentage price

        list_put.append(put_price)  #append the mean put price computed to a list
        list_put_percent.append(put_percent)  #append the mean put price perc computed to a list
        #then, repeat again the "MC-1000 simulation", and do the same until when we reach 1000 times

    avg_put = np.mean(list_put)
    std_put = np.std(list_put)
    avg_put_perc = np.mean(list_put_percent)

    return avg_put, avg_put_perc,std_put

    #print(f'\n'
          #f'------ Montecarlo Pricing PDI --------- ')
    #print(f'Put Price: {avg_put: .4f} €'
          #f'\n'
          #f'Put  %   : {avg_put_perc: .4f} %'
          #f'\n'
          #f'Std of Results: {std_put: .4f}'
          #f'\n'
          #f'Std of Results in %: {std_put_perc: 4f}'
          #)



PDI_EUR, PDI_percent, std_MC = montecarlo_pricer(S1, S2)


# --------------------- Strip of  Digits ----------------------------

Time = [1,2,3,4,5]
A= 0.02  #coupon that I want to be paid in case digit call > H
def digit_call (A):
    """
    :param A: insert the coupon you want to be paid
    :return: price of digital call option
    """
    d_option = []  #final list in which we'll store the opt after after each set of 1000 MC simulation

    for year in Time:
        digit = []  #dummy list for each repetition of MC simulation

        for t in range(trials):
            ST_1 = S1 * m.exp(((r - (sigma_1 ** 2) / 2) * year) + (sigma_1 * random.normalvariate(0, 1) * m.sqrt(year)))
            ST_2 = S2 * m.exp(((r - (sigma_2 ** 2) / 2) * year) + (sigma_2 * random.normalvariate(0, 1) * m.sqrt(year)))

            if ST_1 > H1 and ST_2 > H2:
                opt_dig = A * m.exp(-r * year)

            else:
                opt_dig = 0

            digit.append(opt_dig)

        digit_price = round(np.mean(digit),4)  #compute the mean price of the 1000 MC simulation
        d_option.append(digit_price)  #store the mean price in the final list (d_option) defined at start

    return d_option, round(sum(d_option),5)

    #digital = np.mean(d_option)   #compute the mean of the 1000 results after each set of 1000 MC simulation
    #digital_std = np.std(d_option)

    #print(f'\n'
          #f'--------------------------------------'
          #f'\n'
          #f'Option Digit price --> {(digital) * 100 :.4} %'
          #f'\n'
          #f'Std Dev Pricing   ---> {(digital_std) * 100 :.2} %'
          #f'\n'
          #)

    #return round(digital * 100, 4)

d_option, cost_of_strip = digit_call(A)

print(f'\n'
      f'-----------  ZCB Price  -------------- \n'
      f'ZCB Price: {ZCB_price} % \n \n'
      f'------ Montecarlo Pricing PDI --------- \n'
      f'PDI Price:    {PDI_EUR: .4f} € \n'
      f'PDI  Price %: {PDI_percent: .4f} % \n'
      f'Std of Results:{std_MC: .4f} \n \n'
      f'----------- Strip of Digits ----------- \n'
      f'Price of single digit for each year \n'
      f'{d_option} \n \n'
      f'Price Strip of Digits: {(cost_of_strip) * 100 :.4} % \n \n \n'
      f'-- Price of the Structure: Phoenix WOF ----------- \n'
      f'Reoffer: {ZCB_price + (cost_of_strip) * 100 - PDI_percent: .4} %'
      )

#print("--- %s seconds ---" % (round(time.time(),4) - round(start_time,4)))


