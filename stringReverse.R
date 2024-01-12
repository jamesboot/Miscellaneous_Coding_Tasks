# Write a function that will take a given string and reverse the order of the words. 
# “Hello world” becomes “world Hello” and 
# “May the Fourth be with you” becomes “you with be Fourth the May”

string <- 'Hello world'

stringReverse <- function(string) {
  
  string_v <- strsplit(string, split = ' ')[[1]]
  
  paste(rev(string_v), collapse = ' ')
  
}

stringReverse('Hello world')

stringReverse("May the Fourth be with you")
