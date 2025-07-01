def print_name(i,N):
    if i > N:
        return
    print("Sanju")
    print_name(i+1, N)
print_name(1,5)