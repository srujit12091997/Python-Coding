def compress(chars):
    write, read = 0,0
    while (read<len(chars)):
        char = chars[read]
        count = 0
        while read<len(chars) and chars[read] == char:
            read +=1
            write +=1
        char[write] = char
        write +=1
        
        if count > 1:
            for c in str(count):
                char[write] = c
                write +=1
    return write
print(compress (chars = ["a","a","b","b","c","c","c"]))