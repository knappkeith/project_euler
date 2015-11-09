# -*- coding: utf-8 -*-
# from stopwatch import clockit as _clockit
from lib.timer_laps import LapWatch as _LapWatch
import sys as _sys


def problem_001(num=1000):
    """
    If we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    total = 0
    for i in range(3, num):
        if _divisible_by(i, 3):
            total += i
        elif _divisible_by(i, 5):
            total += i
    return total


def problem_001_v2(num=1000):
    return sum([x for x in range(3, num) if x % 3 == 0 or x % 5 == 0])


def problem_002(max_num=4000000):
    """
    Each new term in the Fibonacci sequence is generated by adding
    the previous two terms. By starting with 1 and 2, the first 10
    terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.
    """
    fib = _build_fib(max_num)
    total = 0
    for i in fib:
        if _divisible_by(i, 2):
            total += i
    return total


def problem_003(num=600851475143):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    all_factors = _get_factors(num)
    for i in all_factors:
        if _is_prime(i[1]):
            return i[1]
    for i in range(len(all_factors) - 1, 0, -1):
        if _is_prime(all_factors[i][0]):
            return all_factors[i][0]


def problem_004(max_num=999, min_num=100):
    """
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 (91X99)

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    palas = []
    for i in range(max_num, min_num, -1):
        for j in range(max_num, min_num, -1):
            num_str = str(i * j)
            is_pala = True
            for k in range(0, len(num_str) / 2):
                if num_str[k] != num_str[-(k+1)]:
                    is_pala = False
                    break
            if is_pala:
                palas.append(i*j)
    return max(palas)


def problem_005(num_range=range(1, 21)):
    """
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?
    """
    highest = num_range[-1]
    result_found = False
    cnt = 1
    while not result_found:
        try_num = cnt * highest
        for i in num_range:
            if not _divisible_by(try_num, i):
                break
        else:
            return try_num
        cnt += 1


def problem_005_v2(num_range=range(1, 21)):
    pos_factor = list(num_range)
    for i in range(len(num_range)-1, 1, -1):
        temp_fact = _get_factors(num_range[i])
        for j in range(1, len(temp_fact)):
            try:
                pos_factor.remove(temp_fact[j][0])
            except:
                pass
            try:
                pos_factor.remove(temp_fact[j][1])
            except:
                pass
    pos_factor.remove(1)
    return problem_005(pos_factor)


def problem_006(max_num=100):
    """
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of
    the first ten natural numbers and the square of the sum
    is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of
    the first one hundred natural numbers and the square of the sum.
    """
    sum_squares = 0
    squared_sum = 0
    for i in range(1, max_num + 1):
        sum_squares += i * i
        squared_sum += i
    return (squared_sum * squared_sum) - sum_squares


def problem_006_v2(max_num=100):
    total_sum = sum(range(1, max_num+1))
    result = 0
    for i in range(1, max_num + 1):
        result += i * (total_sum - i)
    return result


def problem_007(nth_prime=10001):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10,001st prime number?
    """
    prime_cnt = 0
    cur_num = 2
    while prime_cnt != nth_prime:
        if _is_prime_quick(cur_num):
            prime_cnt += 1
        cur_num += 1
    return cur_num - 1


def problem_007_v2(nth_prime=10001):
    only_prime = []
    primes = _get_all_primes(int(nth_prime / 0.05))
    for prime in primes:
        if prime != 0:
            only_prime.append(prime)
    return only_prime[nth_prime - 1]


def problem_008(num_digits=13):
    """
    The four adjacent digits in the 1000-digit number that have
    the greatest product are 9 × 9 × 8 × 9 = 5832.

    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number
    that have the greatest product. What is the value of this product?
    """
    import numpy

    num_str = "73167176531330624919225119674426574742355349194934" + \
              "96983520312774506326239578318016984801869478851843" + \
              "85861560789112949495459501737958331952853208805511" + \
              "12540698747158523863050715693290963295227443043557" + \
              "66896648950445244523161731856403098711121722383113" + \
              "62229893423380308135336276614282806444486645238749" + \
              "30358907296290491560440772390713810515859307960866" + \
              "70172427121883998797908792274921901699720888093776" + \
              "65727333001053367881220235421809751254540594752243" + \
              "52584907711670556013604839586446706324415722155397" + \
              "53697817977846174064955149290862569321978468622482" + \
              "83972241375657056057490261407972968652414535100474" + \
              "82166370484403199890008895243450658541227588666881" + \
              "16427171479924442928230863465674813919123162824586" + \
              "17866458359124566529476545682848912883142607690042" + \
              "24219022671055626321111109370544217506941658960408" + \
              "07198403850962455444362981230987879927244284909188" + \
              "84580156166097919133875499200524063689912560717606" + \
              "05886116467109405077541002256983155200055935729725" + \
              "71636269561882670428252483600823257530420752963450"

    cur_max = 0
    for i in range(0, len(num_str) - num_digits + 1):
        temp_num = num_str[i: i + num_digits]
        if "0" not in temp_num:
            new_num = numpy.prod([int(i) for i in temp_num])
            if new_num > cur_max:
                cur_max = new_num
    return cur_max


def problem_009(sum_of=1000):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which,

    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for
    which a + b + c = 1000.

    Find the product abc.
    """
    checked = 0
    for i in range(1, int(sum_of / 3)):
        for j in range(i + 1, 1 + int((sum_of - i) / 2)):
            for k in range(j + 1, 1 + int(sum_of - i - j)):
                checked += 1
                if i + j + k == sum_of:
                    if i * i + j * j == k * k:
                        return i * j * k


def problem_010(prime_below=2000000):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    return sum(_get_all_primes(prime_below)) - 1

def problem_011():
    return 1

def problem_012():
    return 1

def problem_013():
    """
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    74324986199524741059474233309513058123726617309629
    91942213363574161572522430563301811072406154908250
    23067588207539346171171980310421047513778063246676
    89261670696623633820136378418383684178734361726757
    28112879812849979408065481931592621691275889832738
    44274228917432520321923589422876796487670272189318
    47451445736001306439091167216856844588711603153276
    70386486105843025439939619828917593665686757934951
    62176457141856560629502157223196586755079324193331
    64906352462741904929101432445813822663347944758178
    92575867718337217661963751590579239728245598838407
    58203565325359399008402633568948830189458628227828
    80181199384826282014278194139940567587151170094390
    35398664372827112653829987240784473053190104293586
    86515506006295864861532075273371959191420517255829
    71693888707715466499115593487603532921714970056938
    54370070576826684624621495650076471787294438377604
    53282654108756828443191190634694037855217779295145
    36123272525000296071075082563815656710885258350721
    45876576172410976447339110607218265236877223636045
    17423706905851860660448207621209813287860733969412
    81142660418086830619328460811191061556940512689692
    51934325451728388641918047049293215058642563049483
    62467221648435076201727918039944693004732956340691
    15732444386908125794514089057706229429197107928209
    55037687525678773091862540744969844508330393682126
    18336384825330154686196124348767681297534375946515
    80386287592878490201521685554828717201219257766954
    78182833757993103614740356856449095527097864797581
    16726320100436897842553539920931837441497806860984
    48403098129077791799088218795327364475675590848030
    87086987551392711854517078544161852424320693150332
    59959406895756536782107074926966537676326235447210
    69793950679652694742597709739166693763042633987085
    41052684708299085211399427365734116182760315001271
    65378607361501080857009149939512557028198746004375
    35829035317434717326932123578154982629742552737307
    94953759765105305946966067683156574377167401875275
    88902802571733229619176668713819931811048770190271
    25267680276078003013678680992525463401061632866526
    36270218540497705585629946580636237993140746255962
    24074486908231174977792365466257246923322810917141
    91430288197103288597806669760892938638285025333403
    34413065578016127815921815005561868836468420090470
    23053081172816430487623791969842487255036638784583
    11487696932154902810424020138335124462181441773470
    63783299490636259666498587618221225225512486764533
    67720186971698544312419572409913959008952310058822
    95548255300263520781532296796249481641953868218774
    76085327132285723110424803456124867697064507995236
    37774242535411291684276865538926205024910326572967
    23701913275725675285653248258265463092207058596522
    29798860272258331913126375147341994889534765745501
    18495701454879288984856827726077713721403798879715
    38298203783031473527721580348144513491373226651381
    34829543829199918180278916522431027392251122869539
    40957953066405232632538044100059654939159879593635
    29746152185502371307642255121183693803580388584903
    41698116222072977186158236678424689157993532961922
    62467957194401269043877107275048102390895523597457
    23189706772547915061505504953922979530901129967519
    86188088225875314529584099251203829009407770775672
    11306739708304724483816533873502340845647058077308
    82959174767140363198008187129011875491310547126581
    97623331044818386269515456334926366572897563400500
    42846280183517070527831839425882145521227251250327
    55121603546981200581762165212827652751691296897789
    32238195734329339946437501907836945765883352399886
    75506164965184775180738168837861091527357929701337
    62177842752192623401942399639168044983993173312731
    32924185707147349566916674687634660915035914677504
    99518671430235219628894890102423325116913619626622
    73267460800591547471830798392868535206946944540724
    76841822524674417161514036427982273348055556214818
    97142617910342598647204516893989422179826088076852
    87783646182799346313767754307809363333018982642090
    10848802521674670883215120185883543223812876952786
    71329612474782464538636993009049310363619763878039
    62184073572399794223406235393808339651327408011116
    66627891981488087797941876876144230030984490851411
    60661826293682836764744779239180335110989069790714
    85786944089552990653640447425576083659976645795096
    66024396409905389607120198219976047599490197230297
    64913982680032973156037120041377903785566085089252
    16730939319872750275468906903707539413042652315011
    94809377245048795150954100921645863754710598436791
    78639167021187492431995700641917969777599028300699
    15368713711936614952811305876380278410754449733078
    40789923115535562561142322423255033685442488917353
    44889911501440648020369068063960672322193204149535
    41503128880339536053299340368006977710650566631954
    81234880673210146739058568557934581403627822703280
    82616570773948327592232845941706525094512325230608
    22918802058777319719839450180888072429661980811197
    77158542502016545090413245809786882778948721859617
    72107838435069186155435662884062257473692284509516
    20849603980134001723930671666823555245252804609722
    53503534226472524250874054075591789781264330331690
    """

    num_arr = [
        "37107287533902102798797998220837590246510135740250",
        "46376937677490009712648124896970078050417018260538",
        "74324986199524741059474233309513058123726617309629",
        "91942213363574161572522430563301811072406154908250",
        "23067588207539346171171980310421047513778063246676",
        "89261670696623633820136378418383684178734361726757",
        "28112879812849979408065481931592621691275889832738",
        "44274228917432520321923589422876796487670272189318",
        "47451445736001306439091167216856844588711603153276",
        "70386486105843025439939619828917593665686757934951",
        "62176457141856560629502157223196586755079324193331",
        "64906352462741904929101432445813822663347944758178",
        "92575867718337217661963751590579239728245598838407",
        "58203565325359399008402633568948830189458628227828",
        "80181199384826282014278194139940567587151170094390",
        "35398664372827112653829987240784473053190104293586",
        "86515506006295864861532075273371959191420517255829",
        "71693888707715466499115593487603532921714970056938",
        "54370070576826684624621495650076471787294438377604",
        "53282654108756828443191190634694037855217779295145",
        "36123272525000296071075082563815656710885258350721",
        "45876576172410976447339110607218265236877223636045",
        "17423706905851860660448207621209813287860733969412",
        "81142660418086830619328460811191061556940512689692",
        "51934325451728388641918047049293215058642563049483",
        "62467221648435076201727918039944693004732956340691",
        "15732444386908125794514089057706229429197107928209",
        "55037687525678773091862540744969844508330393682126",
        "18336384825330154686196124348767681297534375946515",
        "80386287592878490201521685554828717201219257766954",
        "78182833757993103614740356856449095527097864797581",
        "16726320100436897842553539920931837441497806860984",
        "48403098129077791799088218795327364475675590848030",
        "87086987551392711854517078544161852424320693150332",
        "59959406895756536782107074926966537676326235447210",
        "69793950679652694742597709739166693763042633987085",
        "41052684708299085211399427365734116182760315001271",
        "65378607361501080857009149939512557028198746004375",
        "35829035317434717326932123578154982629742552737307",
        "94953759765105305946966067683156574377167401875275",
        "88902802571733229619176668713819931811048770190271",
        "25267680276078003013678680992525463401061632866526",
        "36270218540497705585629946580636237993140746255962",
        "24074486908231174977792365466257246923322810917141",
        "91430288197103288597806669760892938638285025333403",
        "34413065578016127815921815005561868836468420090470",
        "23053081172816430487623791969842487255036638784583",
        "11487696932154902810424020138335124462181441773470",
        "63783299490636259666498587618221225225512486764533",
        "67720186971698544312419572409913959008952310058822",
        "95548255300263520781532296796249481641953868218774",
        "76085327132285723110424803456124867697064507995236",
        "37774242535411291684276865538926205024910326572967",
        "23701913275725675285653248258265463092207058596522",
        "29798860272258331913126375147341994889534765745501",
        "18495701454879288984856827726077713721403798879715",
        "38298203783031473527721580348144513491373226651381",
        "34829543829199918180278916522431027392251122869539",
        "40957953066405232632538044100059654939159879593635",
        "29746152185502371307642255121183693803580388584903",
        "41698116222072977186158236678424689157993532961922",
        "62467957194401269043877107275048102390895523597457",
        "23189706772547915061505504953922979530901129967519",
        "86188088225875314529584099251203829009407770775672",
        "11306739708304724483816533873502340845647058077308",
        "82959174767140363198008187129011875491310547126581",
        "97623331044818386269515456334926366572897563400500",
        "42846280183517070527831839425882145521227251250327",
        "55121603546981200581762165212827652751691296897789",
        "32238195734329339946437501907836945765883352399886",
        "75506164965184775180738168837861091527357929701337",
        "62177842752192623401942399639168044983993173312731",
        "32924185707147349566916674687634660915035914677504",
        "99518671430235219628894890102423325116913619626622",
        "73267460800591547471830798392868535206946944540724",
        "76841822524674417161514036427982273348055556214818",
        "97142617910342598647204516893989422179826088076852",
        "87783646182799346313767754307809363333018982642090",
        "10848802521674670883215120185883543223812876952786",
        "71329612474782464538636993009049310363619763878039",
        "62184073572399794223406235393808339651327408011116",
        "66627891981488087797941876876144230030984490851411",
        "60661826293682836764744779239180335110989069790714",
        "85786944089552990653640447425576083659976645795096",
        "66024396409905389607120198219976047599490197230297",
        "64913982680032973156037120041377903785566085089252",
        "16730939319872750275468906903707539413042652315011",
        "94809377245048795150954100921645863754710598436791",
        "78639167021187492431995700641917969777599028300699",
        "15368713711936614952811305876380278410754449733078",
        "40789923115535562561142322423255033685442488917353",
        "44889911501440648020369068063960672322193204149535",
        "41503128880339536053299340368006977710650566631954",
        "81234880673210146739058568557934581403627822703280",
        "82616570773948327592232845941706525094512325230608",
        "22918802058777319719839450180888072429661980811197",
        "77158542502016545090413245809786882778948721859617",
        "72107838435069186155435662884062257473692284509516",
        "20849603980134001723930671666823555245252804609722",
        "53503534226472524250874054075591789781264330331690"]

    cur_total = ""
    carry_over = 0
    for i in range(len(num_arr[0]) - 1, -1, -1):
        this_sum = carry_over
        for num in num_arr:
            this_sum += int(num[i])
        cur_total = str(this_sum)[-1] + cur_total
        carry_over = int(this_sum / 10)
    cur_total = str(carry_over) + cur_total
    return int(cur_total[0:10])

def problem_014(less_than=1000000):
    """
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    len_arr = []
    already_found = {}
    max_num = 0
    max_index = 0
    for i in range(2, less_than):
        cur_num = i
        cur_chain_len = 0
        while cur_num != 1:
            cur_chain_len += 1
            if cur_num % 2 == 0:
                cur_num = cur_num / 2
            else:
                cur_num = cur_num * 3 + 1
            try:
                cur_chain_len += already_found[str(cur_num)] - 1
                cur_num = 1
            except:
                pass
        cur_chain_len += 1
        if cur_chain_len > max_num:
            max_num = cur_chain_len
            max_index = i
        already_found[str(i)] = cur_chain_len
    return max_index


def _get_all_primes(prime_below):
    primes = list(range(0, prime_below))
    p = 2
    inc = 1
    while True:
        for index in range(p ** 2, len(primes), inc * p):
            primes[index] = 0
        for i in range(p+1, int(prime_below ** (0.5))):
            if primes[i] != 0:
                inc = 2
                p = primes[i]
                break
        else:
            return primes


def _is_prime(num):
    factors = _get_factors(num)
    return len(factors) == 1


def _is_prime_quick(num):
    num_str = str(num)
    if len(num_str) > 1:
        if num_str[-1] in '024568':
            return False
    for i in _drange(2, (num / 2) + 1):
        if num % i == 0:
            return False
    return True


def _get_factors(num):
    factors = [(1, num)]
    for i in _drange(2, (num / 2) + 1):
        div = num / i
        if num % i == 0:
            if i == factors[-1][1]:
                break
            factors.append((i, div))
            if i == div:
                break
    return factors


def _drange(start, stop, step=1):
    r = start
    while r < stop:
        yield r
        r += step


def _build_fib(max_num):
    fib = [1, 2]
    while fib[-1] < max_num:
        fib.append(fib[-1] + fib[-2])
    return fib[0:-1]


def _divisible_by(num, div):
    a = num / float(div)
    return a == int(a)


if __name__ == "__main__":
    me = _sys.modules[__name__]
    if len(_sys.argv) > 1:
        item = getattr(me, _sys.argv[1])
        print "%s: %d" % (_sys.argv[1], item())
        _sys.exit(0)
    times = _LapWatch()
    for i in dir(me):

        if i[0] != "_":
            item = getattr(me, i)
            item_v2 = None
            try:
                item_v2 = getattr(me, i + "_v2")
            except:
                pass
            if callable(item):
                if callable(item_v2):
                    pass
                else:
                    print "{:14}: {:13} in {} sec".format(i, item(), times.lap(i))
                    times.lap(i)
    print "\n{:14}: {} sec".format("Total Time", times.elapsed)
