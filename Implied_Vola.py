########################
import math as m
from scipy import stats as s
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
from matplotlib import cm


# ------ Implied Volatility ---------

K=[265, 270, 275, 280]
p=[32.20, 36.43, 39.40, 40.95]
S0, r, T = 282.80, 0.01, 12/12

result_p = []
def sigma_impl(S0, r, T, guess=0.35):
    """
    Compute the implied vola from the list of Strike price K and the put price p
    -------------------
    for loop: using enumerate we can highlight the ith index and kth element from the list K
    sigma_fun: we create the function for resolving for sigma - inside we have the BS put price
    d1 and d2 terms: are expressed explicitely
    p[index]: let us retrieve the price of the put in correspondance to the Strike price iterate from above
    --------------------
    output: we create a list using the newton process, resolving for sigma and imposing sigma_fun = 0"""
    for index, k in enumerate(K):

        sigma_fun = lambda sigma: \
         k * m.exp(-r*T) * (1- s.norm.cdf((m.log(S0 / k) + (r - 0.5 * (sigma ** 2)) * T) / (sigma * m.sqrt(T)))) - \
         S0 * (1- s.norm.cdf((m.log(S0 / k) + (r + 0.5 * (sigma ** 2)) * T) / (sigma * m.sqrt(T)))) \
         - p[index]

        result = round(optimize.newton(sigma_fun, guess), 4)

        result_p.append(result)

    return result_p


impl_values = sigma_impl(S0, r, T)

d={'K': K, 'Mkt Put Price': p, 'Implied Vola' : result_p}
df_1 = pd.DataFrame(data=d)

print('\n')
print('-'*5, 'Implied Volatility AAPL', '-'*5)
#print('implied vola', result_p)
print(df_1)

vola_skew = plt.plot (result_p, K)
# plt.show(vola_skew)

#show all bounded together

# ---- Volatility Surface -------------
dict_p={}
time_vec = [1/12, 3/12, 6/12, 12/12]
# K= [265, 270, 275, 280]
p_1 =[7.41, 8.65, 10.35, 12.45]
p_3 =[11.50, 13.28, 15, 18.75]
p_6 =[20.83, 22.70, 25.95, 27]
p_12 =[32.20, 36.43, 39.40, 40.95]

def volatily_surface(S0, r):
    """
    Compute Vola Surface (of put options in  this case)
    --------------------------------
    For each interval of time specified above, we will run the newton optimization (for each strike
    price K). To do that, we use the market price of the put options @ 1m,3m,6m,12m specified in
    lists above.
    lista_res = important to store all the vola results;
    For each time period considered in T, create an empty list, then evaluate whether the lista_res
    has a certain lenght. If this length is 3 or less, for each k use the put price of the p_1 list (put price 1m).
    and store the result of each K-th iteration in lista_res.
    When all k are iterated, store the result in the dictionary and
    restart the process using the second time period in T.
    In this case the len(lista_res) > 3  & < 8;
    thus we use the p_3 (put price of 3m) for each K, in accordance with the time in which we are working.
    --------------------------------
    :param S0:
    :param r:
    :return: Dataframe of Volatility Surface (implied vola wrt T & K), and a vector containing all the results
    """
    lista_res = []
    for t in time_vec:
        l_provv = []

        if len(lista_res) < 4:
            for idx, k in enumerate(K):
                vola_surf = lambda sigma_surf: \
                    k * m.exp(-r * t) * \
                    (1 - s.norm.cdf((m.log(S0 / k) + (r - 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) - \
                    S0 * (1 - s.norm.cdf(
                        (m.log(S0 / k) + (r + 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) \
                    - p_1[idx]

                vola_surface = round(optimize.newton(vola_surf, 0.40), 4)
                lista_res.append(vola_surface)
                l_provv.append(vola_surface)

        elif len(lista_res) < 8:
            for idx, k in enumerate(K):
                vola_surf = lambda sigma_surf: \
                    k * m.exp(-r * t) * \
                    (1 - s.norm.cdf((m.log(S0 / k) + (r - 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) - \
                    S0 * (1 - s.norm.cdf(
                        (m.log(S0 / k) + (r + 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) \
                    - p_3[idx]

                vola_surface = round(optimize.newton(vola_surf, 0.40), 4)
                lista_res.append(vola_surface)
                l_provv.append(vola_surface)

        elif len(lista_res) < 12:
            for idx, k in enumerate(K):
                vola_surf = lambda sigma_surf: \
                    k * m.exp(-r * t) * \
                    (1 - s.norm.cdf((m.log(S0 / k) + (r - 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) - \
                    S0 * (1 - s.norm.cdf(
                        (m.log(S0 / k) + (r + 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) \
                    - p_6[idx]

                vola_surface = round(optimize.newton(vola_surf, 0.40), 4)
                lista_res.append(vola_surface)
                l_provv.append(vola_surface)

        elif len(lista_res) < 16:
            for idx, k in enumerate(K):
                vola_surf = lambda sigma_surf: \
                    k * m.exp(-r * t) * \
                    (1 - s.norm.cdf((m.log(S0 / k) + (r - 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) - \
                    S0 * (1 - s.norm.cdf(
                        (m.log(S0 / k) + (r + 0.5 * (sigma_surf ** 2)) * t) / (sigma_surf * m.sqrt(t)))) \
                    - p_12[idx]

                vola_surface = round(optimize.newton(vola_surf, 0.40), 4)
                lista_res.append(vola_surface)
                l_provv.append(vola_surface)


        dict_p[t] = l_provv

    surface_t = pd.DataFrame(dict_p)
    surface_table =surface_t.rename(columns= {time_vec[0]: "1 month", time_vec[1]: "3 months",
                                              time_vec[2]: "6 month", time_vec[3]: "12 months"},
                                    index= {0: K[0], 1: K[1], 2: K[2], 3: K[3]})


    print('\n',
          '------ Volatility Surface AAPL -----',
          '\n',
        surface_table,
          '\n',
          '\n',
          '------ Vola Surf Vector -----',
          '\n',
          lista_res)
    return surface_table


#volatily_surface(S0,r)

# Let's now plot the vola surface
df = volatily_surface(S0,r)  #redefine the output of the function
new_df =df.rename(columns= {"1 month":1, "3 months":3, "6 month":6,"12 months":12})

#impose the axis
x,y = np.meshgrid(new_df.columns.astype(float), new_df.index)
z = new_df.values

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
#rgb = LightSource(270, 45).shade(z, cmap=plt.cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
                       #linewidth=0, antialiased=False, shade=False)
ax.set_title('Volatility Surface');
ax.view_init(30, 55)
plt.show()