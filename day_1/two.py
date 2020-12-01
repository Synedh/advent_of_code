# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?
entries = [int(line) for line in open('input.txt').readlines()]
for i in entries:
    for j in entries:
        for k in entries:
            if i + j + k == 2020:
                print(j * i * k)
                exit()
