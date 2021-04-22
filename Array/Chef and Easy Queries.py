"""
CHEF AND EASY QUERIES

https://www.codechef.com/problems/CHEFEZQ

Chef published a blog post, and is now receiving many queries about it. 
On day i, he receives Qi queries. But Chef can answer at most k queries in a single day.
Chef always answers the maximum number of questions that he can on any given day (note however that this cannot be more than k). 
The remaining questions (if any) will be carried over to the next day.
Fortunately, after n days, the queries have stopped. 
Chef would like to know the first day during which he has some free time, i.e. the first day when he answered less than k questions.
"""

def chefAndEasyQueries(listQueries, maxQuery):
   carry = 0
   for index, value in enumerate(listQueries):
      carry += value
      if carry < maxQuery:
         print('Day chef will have free time: {}.'.format(index+1)) 
         return
      else:
         carry -= maxQuery
   print("Chef won't be free any day") 
   
k = int(input('Maximum number of queries to solve per day: '))
n = int(input('Number of days queries has to be solved: '))
listQueries = list(map(int,input("\nEnter the queries to be resolved per day: ").strip().split()))[:n] 
chefAndEasyQueries(listQueries, k)
