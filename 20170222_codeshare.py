# Codeshare session with Yuhong


# Code Challenge #1:

# input: array of integers
# input: target_sum
# return whether a pair in array will sum to target_sum

# ex: [3, 1, 6, -2] , target 1, 3 + -2 = 1

# brute force pseudocode
# use for loop to find sum of each pair
# starting with 3 each subsequent number
# if not find target sum, move onto next number in array
# so 2 + ...

# O(n^2) because nested array
def find_target_sum(nums, target_sum):
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if index1 != index2:
                if num1 + num2 == target_sum:
                    return True
    return False


# O(n^2) still though slighly less than previous response
def find_target_sum2(nums, target_sum):
    for index1 in xrange(len(nums)):
        if index1 + 1 < len(nums):
            for index2 in xrange(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target_sum:
                    return True
    return False


# O(nlogn) --> sort array, use binary search to find number for target_sum


# O(n) --> can create set or dictionary if already know value looking for
def find_target_with_set(nums, target_sum):
    nums_set = set(nums)
    for num in nums_set:
        num_to_find = target_sum - num
        if num_to_find in nums_set:
            return True
    return False


# Code Challenge #2

# Volleyball
# First team to reach 25 is the winner
# If both teams reach 24, then winning team needs to score 2 points in a row
# Given a score outcome, how many different games are possible?
# team a: 25, team b: 14, num_games_possible = ???
# bbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaa => 1 possible game
# babbbbbbbbbbaaaaaabaaaaaaaaaaaaaaaaaaaa => another game
# team a: 7, team b: 5 => not a full game, return 0

# dynamic programming or with combination/permutations