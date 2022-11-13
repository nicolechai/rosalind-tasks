
k = 30
m = 24
n = 17
total_pop = k + m + n

rec_probability = ((n / total_pop) * ((n-1)/((n-1) + m + k))) + ((1/2) * (n/total_pop) * (m / (m + (n-1) + k))) + ((1/2) * (m/total_pop) * (n / (n + (m-1) + k))) + ((1/4) * (m/total_pop) * ((m-1) / (n + (m-1) + k)))

total_probability = 1 - rec_probability


print(total_probability)
