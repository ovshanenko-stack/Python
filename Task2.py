print("Numbers in Range(10)")
prev_number = 0
#Loop through numbers in range(10) and calculate the sum of current number and previous number
for i in range(10):
        sum = prev_number + i
        print(f"cur_number {i} prev_number {prev_number} sum is: {sum} " )
        #update the previous number to current number for next iteration
prev_number = i