def remove_duplicate_inplace(str):

    my_set = set([])
    read_stream = 0
    write_stream = 0

    while(read_stream < len(str)):
        if(str[read_stream] not in my_set):
            my_set.add(str[read_stream])
            str[write_stream] = str[read_stream]
            write_stream += 1
        read_stream += 1
    str[write_stream] = '\0'
    
    return str

str = [ 'D', 'A', 'D', 'B', 'A', 'C', 'D', 'A' ]

print ("original array: ", str)
print ("distinct characters: ", remove_duplicate_inplace(str))