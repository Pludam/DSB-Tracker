import time


def timeit(func): 
    '''Decorator that reports the execution time.'''
  
    def wrap(*args, **kwargs): 
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
          
        print(f"{func.__name__}: {end-start}s") 
        return result 
    return wrap 

def format_line(func): 
    '''Decorator that prints an formatting line.'''
  
    def wrap(*args, **kwargs): 
        result = func(*args, **kwargs) 
        print("-------------------------------------------------") 
        return result 
    return wrap 