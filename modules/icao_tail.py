import sys

if __name__ == "__main__":
    val = sys.argv[1].upper()
    
    if val[0] == 'N': # N-Number
        res = n_to_icao(val)
    elif val[0] == 'A': # icao
        res = icao_to_n(val)
    else:
        invalid_parameter()

    if res is None:
        invalid_parameter()
    print(res)