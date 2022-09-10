def add(c,x,y):
    return x+y
def sub(c,x,y):
    return x-y
def mult(c,x,y):
    return x*y
def div(c,x,y):
    return x/y
def exp(c,x,y):
    return x**y
def perc(c,x,y):
    #this is a function to calculate chance of success on a x sided die to roll
    #greater than y
    return ((x+1.0)-y)/x
def perm(c,x,y):
    #this is a function to calculate permutations
    ret_val = 1
    for i in range(0,int(y)):
        ret_val *= x
        x -= 1
    return ret_val
def comb(c,x,y):
    denom = 1
    r = int(y)
    if r < 0:
        r*=1
    while r != 0:
        denom *= r
        r-=1
    return perm(c,x,y)/denom
#this is the array where we store the notation for our functions
#all functions that are used by the program need to take two arguments, x and y and be writen in the form
# xSy where s is the symbol that represents the function, stored in the notation array
f_arr = [('+',add),('-',sub),('*',mult),('/',div),('^',exp),('s',perc),('p',perm),('c',comb)]
def check_outer(expr,parenth=['(',')']):
    #this function checks to see if a given expression is surrounded COMPLETY by parenthasis
    inside = 0
    elen = len(expr)
    for i in range(-1,elen):
        if expr[i] == parenth[0]:
            inside += 1
        elif expr[i] == parenth[1]:
            inside -= 1
        elif inside == 0:
            #the reason this is else is so it doesnt fire if our last charicter is parenthasis
            #we are currently outside of parenthasies, so return false
            #becuse the entire expression is not inside of parenthasis
            print('NOT SURROUNDED')
            return False
    print(inside)
    #we never made it out of the currlys so we were allways inside parenthasis
    print('SURROUNDED')
    return True
def strip_outer(expr,parenth=['(',')']):
    if check_outer(expr):
        #there is a pair of outside parenthasis, strip them and return the next stripped version in the chain 
        return strip_outer(expr[1:-1])
    else:
        #there are no parenthasys on the outsides of the expression
        return expr 
def parse_single_type(args,x):
    return float(x)
def parse(expr,
        arr=f_arr,
        main_type=parse_single_type,
        carry_args=[],
        parenth=['(',')']):

    #strip the outer parenthasis that way if the program sends us a parenthasised expression
    #we can use it like a normal one
    expr = strip_outer(expr,parenth)
    print(expr)

    inside = 0
    for i in range(0,len(arr)):
        for j in range(0,len(expr)):
            if expr[j] == parenth[0]:
                inside+=1
            elif expr[j] == parenth[1]:
                inside -= 1
            elif expr[j] == arr[i][0] and inside == 0:
                return arr[i][1](carry_args,
                        parse(expr[0:j],
                                arr,
                                main_type,
                                carry_args,
                                parenth),
                        parse(expr[j+1:len(expr)],
                                arr,
                                main_type,
                                carry_args,
                                parenth))
    #we found no funtion symbols in the expresion, return an intager to exit the recursion series
    return main_type(carry_args,expr)
if __name__ == '__main__':
    ansr = input('(main)> ')
    while ansr != 'q':
        print(parse(ansr))
        ansr = input('(main)> ')