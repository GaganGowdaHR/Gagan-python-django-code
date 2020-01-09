def binary_search(l,key):
    mid = len(l) // 2
    if not l:
        return False
    
    elif l[mid] == key:
        return True
    elif key < l[mid]:
        return(binary_search(l[:mid],key))
        
    else:
        return(binary_search(l[mid+1:],key))

if __name__ == "__main__":
    l = [100,200,300,400,500,600,700]
    key = 600

    print(binary_search(l,key))