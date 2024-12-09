#!/usr/bin/env python3

def binomial_coeff_OLD(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    """
    if k == 0:
        return 1

    if n == 0:
        return 0

    return binomial_coeff_OLD( n - 1, k ) + binomial_coeff_OLD( n - 1, k - 1 )


def binomial_coeff_v1(n, k):
    return 1 if k == 0 else (0 if n == 0 else binomial_coeff_v1( n - 1, k ) + binomial_coeff_v1( n - 1, k - 1 ))

def binomial_coeff_v2(n, k, memo={}):
    key = (n,k)  # Tuple for the key since tuples are immutable.
    value = memo[key] if key in memo else\
        (1 if k == 0 else (0 if n == 0 else binomial_coeff_v2( n - 1, k ) + binomial_coeff_v2( n - 1, k - 1 )))
    memo[(n,k)] = value
    return value

def main():
    n = 10
    k = 4
    print('-'*33, ' OLD ', '-'*32)
    start_time = time()
    value = binomial_coeff_OLD(n, k)
    end_time = time()
    print(value)
    print( "Elapsed time:", end_time - start_time )

    print('-'*33, ' V1 ', '-'*32)
    start_time = time()
    value = binomial_coeff_v1(n, k)
    end_time = time()
    print(value)
    print( "Elapsed time:", end_time - start_time )

    print( '-' * 33, ' V2 ', '-' * 32 )
    start_time = time()
    value = binomial_coeff_v2( n, k )
    end_time = time()
    print( value )
    print( "Elapsed time:", end_time - start_time )

    print( '-' * 25, ' V2 Already Cached ', '-' * 25 )
    start_time = time()
    value = binomial_coeff_v2( n, k )
    end_time = time()
    print( value )
    print( "Elapsed time:", end_time - start_time )


if __name__ == '__main__':
    from time import time
    main()