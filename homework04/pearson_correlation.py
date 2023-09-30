import math
from statistics import mean

def pearson_correlation(list1, list2):
    x_mean = mean(list1)
    t_mean = mean(list2)
    num = 0
    den1 = 0
    den2 = 0
    for i in range(len(list1)):
        num += (list1[i] - x_mean)*(list2[i] - t_mean)
        den1 += (list1[i] - x_mean)**2
        den2 += (list2[i] - t_mean)**2
    r = num / (math.sqrt(den1)* math.sqrt(den2))
    return r

list1 = [1,2,4,7,8]
list2 = [3,7,8,7,90]

# Apply the pearson correlation coefficient
corr = pearson_correlation(list1, list2) 
print('Pearsons correlation: %.3f' % corr)
