word="cyber"
reversed=""

for i in range(len(word)-1,-1,-1):
    reversed+=word[i]
print(reversed)

# for i in range(len(word)-1, 0):
# range(start, stop) does not count backwards by default — and range(start, stop) excludes stop.

# Also, the step is missing — so Python tries to count up, not down.



# To loop backwards, use range(start, stop, step) with a negative step.
# for i in range(len(word)-1, -1, -1):
# start = len(word) - 1 (last index)

# stop = -1 (because stop is exclusive — you want to include index 0)

# step = -1 (count backwards)

