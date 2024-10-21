"""
Solutions to module VA 1
Student: Agnes Leth
Mail:
"""
from time import process_time as pc

def exchange1(a, coins):
    if a == 0:
        return 1 #found a valid way to exchange
    elif a<0 or coins == []:
        return 0 #no valid exchange
    else:
        return exchange1(a, coins[1:]) + exchange1(a-coins[0], coins)

def exchange(a, coins, memo = None) -> int: 
    """ Count possible way to exchange a with the coins in coins. Use memoization"""
    if memo == None:
        memo = {}
        
    def _exchange(a, coins):
        if a == 0:
            return 1 #found a valid way to exchange
        elif a<0 or coins == []:
            return 0 #no valid exchange
        
        if (a, len(coins)) in memo:
        #    print(f'Used memo: {a, len(coins)}')
            return memo[(a, len(coins))]
        
       # print(f'Did not use memo: {a, len(coins)}')

        result = _exchange(a-coins[0], coins) + _exchange(a, coins[1:])
        memo[(a, len(coins))] = result
        return result
    
    return _exchange(a, coins)

def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if not l1 and not l2:
        return []
    elif l1 == []:
        return l2.copy() #must use copy
    else:
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])


def main():
    print('\nCode that demonstates my implementations\n')
    a = 1000
    coins = [100, 50, 10, 5, 1]
    print(exchange(a, coins))
    
    start = pc()
    for i in range(20):
        exchange(10000, coins)
    stop = pc()

    print(f"Avg time: { (stop-start)/ 20}")


    l1 = ['a', 'b', 'c']
    l2 = [2, 4, 6, 'x', 10]
    print(zippa(l1, l2))



if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 
a = 1000: Avg time: 0.0008646000000000001 
a = 2000: Avg time: 0.0016495500000000003

What happens if you try to calculate e.g. 10000?
  
"""
