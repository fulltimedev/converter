with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        str1 = line.split(':')
        str1 = str1[0]

        split = str1.split('@')
        str2 = split[0]

        cut_line = line.split(':')
        str3 = cut_line[-1]

        final = f'{str1}:{str2}:{str3}'
        outfile.write(final)
    print('Process finished!')
