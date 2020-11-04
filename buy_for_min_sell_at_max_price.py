# buy at a min price and sell at a max profit.

# sample output: 
# you can buy at min:  5
# you can sell at max profit:  7

def sell_at_max (arr):
    if(len(arr)<1):
        return "length issues."
    
    max_profit = 0
    min = arr[0]

    for current_value in arr:
        
        if current_value < min:
            min = current_value

        current_profit = current_value - min
        
        if(current_profit > max_profit):
            max_profit = current_profit
    
    print("you can buy at min: ", min)
    print("you can sell at max profit: ", max_profit)

arr = [ 8, 9, 5, 6, 12, 10, 11 ]
sell_at_max(arr)
