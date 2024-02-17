def reverse_string(s):
    split_string = [*s]

    return ''.join(split_string[::-1])


print(reverse_string("hello"))
