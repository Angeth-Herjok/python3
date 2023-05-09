# 1.Write a Python program that takes a list of strings as input and
#  outputs the number of times each string appears in the list, 
# using a dictionary and conditional statements.
def count_times(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(count_times(["Hello","hey","hey","hi","Hello","hey"]))

# 2.Write a Python program that takes a list of numbers as input and 
# outputs the median of the numbers 
def median_number(number):
    x=len(number)
    index=x//2
    if x % 2:
        return sorted(number)[index]
    return sum(sorted(number)[index-1:index+1])/2
print(median_number([1,2,5,4,3]))


#3. Write a Python program that takes a list of numbers as input and 
# outputs the second largest number in the list using conditional statements and a for loop.
# def second_largest(nums):
    
    
# print(second_largest([2,3,4,7,6,8,9]))

# 4.Write a Python program that takes a year as input and determines if it is a leap year

def leap_year(year):
        if year % 4==0:
            if year % 100==0:
                if year % 400==0:
                    print("Year is a leap year")
                else:
                    print("Year is not a leap year")
print(leap_year(2000))


# 5.Write a Python program that takes a string as input and checks if it is a palindrome 
# (reads the same forwards and backwards), ignoring spaces and punctuation.
word="john"
word=input("Enter word:")
reversed_word=(word[::-1])
if word==reversed_word:
    print("Is palindrome")
else:
    print("Is not a palindrome")

