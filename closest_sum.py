
# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

nums = [-1, 2, 1, -4]
target = 1
for i in nums[1:]:
    for j in nums:
        if j==i:
            pass 
        else:  
            res = j+1
            res_tes = i+j+res
            if  i+j+res_tes == 2:
                print i,j,res_tes
 
