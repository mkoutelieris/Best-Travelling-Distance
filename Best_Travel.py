"""
The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters
t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) 
and ls (list of distances, all distances are positive or null integers and this list has at least one element). 
The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, 
if that sum exists, or otherwise None.

Examples:

ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> None

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228
"""

import itertools

def choose_best_sum(t, k, ls):
    p_ls = []
    sum_dis = []
    
    for i in itertools.combinations(ls, k):
        p_ls.append(i)
    
    for i,val in enumerate(p_ls):
        sum = 0
        for z in val:
            sum += z
        sum_dis.append(sum)
    
    n = len(sum_dis)
    
    sum_dis.sort()
    ans = None
    
    for i in sum_dis:
        if(i <= t):
            ans = i
    
    print("Desired distance: ", t)
    print("Minimum distance: ", sum_dis[0])
    print("Maximum distance: ", sum_dis[n-1])
    print("Best desired distance: ", ans, "\n")

print("\n****Testing****\n")

xs = [50, 55, 57, 58, 60]
choose_best_sum(178, 3, xs)
choose_best_sum(227, 4, xs)
choose_best_sum(174, 5, xs)
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(230, 4, xs)
choose_best_sum(430, 5, xs)
choose_best_sum(430, 8, xs)