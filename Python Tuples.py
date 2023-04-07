if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = ()
    
    for i in integer_list:
      
        y = list(t)
        y.append(i)
        t = tuple(y)
    
    hash_value = hash(t)
    print(hash_value)
