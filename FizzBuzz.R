# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print Fizz instead of the number and...
# for the multiples of five print Buzz. 
# For numbers which are multiples of both three and five print FizzBuzz.

numbers <- c(1:100)

for (x in numbers) {
  if (x%%3 == 0 & x%%5 == 0) {
    print('FizzBuzz')
  } else if (x%%3 == 0 & x%%5 != 0) {
    print('Fizz')
  } else if (x%%3 != 0 & x%%5 == 0) {
    print('Buzz')
  } else {
    print(x)
  }
}


