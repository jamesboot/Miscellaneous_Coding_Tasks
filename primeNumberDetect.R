# Write a function, primeNumberDetector, that tests if a number, n is a prime number.


primeNumberDetector <- function(num) {
  if (num %in% c(2, 3, 5, 7)) {
    return(TRUE)
    
  } else if (num %% 2 != 0 &
             num %% 3 != 0 &
             num %% 4 != 0 &
             num %% 5 != 0 &
             num %% 6 != 0 &
             num %% 7 != 0 &
             num %% 8 != 0 &
             num %% 9 != 0) {
    return(TRUE)
    
  } else {
    return(FALSE)
    
  }
}

primeNumberDetector(23)







