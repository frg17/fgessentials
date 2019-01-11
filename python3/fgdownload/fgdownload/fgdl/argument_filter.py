def filter_arguments():
    import sys
    args = sys.argv
    l = len(args)
  
    userFilters = []
    if l == 4:
        userFilters.append((args[2], args[3]))

    if l == 6:
        userFilters.append((args[2], args[3]))
        userFilters.append((args[4], args[5]))


    if l < 2:
        print(r"py fgdl [-[se] [\d+]]")
        return -1
        
    for f in userFilters:
        if not (f[0] == "-s" or f[0] == "-e"):
            print("'{}' is not a valid filter". format(f[0]))
            return -1
        else:
            try:
                int(f[1])
            except:
                print("'{}' is not a valid filter value for '{}'".format(
                    f[1], f[0]
                ))
                return -1
    
    return userFilters



    