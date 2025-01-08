## inner function

def print3(): 

  def print_hello(): 
      print('hello') 

  print_hello() 
  print_hello() 
  print_hello() 

# Main code 
print3() 
print_hello() # This will give an error

######## Returning an inner function
def make_print(): 
  
  def print_hello(): 
    print('hello') 

  return print_hello 

# Main code 
fn = make_print() 
fn() 

### A closure

def make_printx(x): 

    def printx(): 
        print(x) 

    return printx 

# Main code 
fn1 = make_printx(7) 
fn2 = make_printx(100) 
fn1() 
fn2() 
######################
#######A more useful closure
def make_printb(start, end): 

  def printb(s): 
    print(start + s + end) 

  return printb 

# Main code 
sq = make_printb('[', ']') 
dbl_ang = make_printb('<<', '>>') 
sq('hello') 
dbl_ang('world') 

################
### Using a closure instead of a lambda

def addn(n): 

    def add(x): 
        return x + n 
    return add 

a = [1, 3, 0, 6] 
b = map(addn(1), a) 
print(list(b)) # [2, 4, 1, 7] 

#########
