import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# The smallest number I could have seen is 5 and the largest was 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# The smallest number I could have seen is 3 and the largest was 9.
# Could line 2 have produced a 4?
# No. Because of the step of 2, line 2 could only produce odd numbers.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# The smallest number I saw was 2.6 and the largest was 4.8.

print(random.randrange(1, 100))