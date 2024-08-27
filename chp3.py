# Part 1

# Sum of Squares
def sum_squares(int_list):
    sum_of_squares = 0
    for item in int_list:
        sum_of_squares += item ** 2
    return sum_of_squares

print(sum_squares([]))

# Factorial, Sumorial
def factorial(pos_int):
    product_of_nums = 1
    for num in range(1, pos_int + 1):
        product_of_nums *= num
    return product_of_nums    

print(factorial(6))

def sumtorial(pos_int):
    sum_of_nums = 0
    for num in range(1, pos_int + 1):
        sum_of_nums += num
    return sum_of_nums

print(sumtorial(6))

# Sum of Odds
def sum_n_odds(n):
    summed_n_odds = 0
    for odd_num in range(1, n * 2 + 1, 2):
        summed_n_odds += odd_num
    return summed_n_odds

print(sum_n_odds(7))
    
def sum_odds_to_n(n):
    summed_odds_to_n = 0
    for odd_num in range(1, n + 1, 2):
        summed_odds_to_n += odd_num
    return summed_odds_to_n
print(sum_odds_to_n(7))

# Fibonacci Sequence
def fib(n):
    a = 1
    b = 1
    for item in range(n - 1):
        c = b
        b = a + b
        a = c
    return a

print(fib(10))

# Tribonacci Sequence
def trib(n):
    a = 0
    b = 0
    c = 1
    for item in range(n - 1):
        d = c
        e = b
        c = a + b + c
        a = e
        b = d
        
    return a

print(trib(24))

# The Harmonic Series
def harmonic_series(n):
    sum = 0
    for num in range(1, n + 1):
        sum += 1 / num
    return sum

print(harmonic_series(12))

# Alternate Signs
def alt_signs(n):
    value = 0
    for i in range(n + 1):
        value += -1 * (((-1) ** i) * i)
    return value
    
print(alt_signs(12))

# Pi Approximated
def pi_approx(n):
    Pi_est = 0
    real_i = -1
    for i in range(n):
        real_i += 2
        neg_or_pos = ((-1) ** i)
        Pi_est += 1 / (neg_or_pos * real_i)
    Pi_est *= 4
    return Pi_est

print(pi_approx(100))

# Geometric Series
def geometric_series(i, n, r):
    sum_series = 0
    for _ in range(n):
        sum_series += i
        i *= r
    return sum_series
    
print(geometric_series(1, 101, -1))

# Iterated Iteration
def iter_iter(n):
    sum_series = 0
    summed_odds = 0
    for current_num in range(1, n * 2, 2):
        summed_odds += current_num
        sum_series += current_num / (summed_odds)
    return sum_series

print(iter_iter(18))

# Hyperoperations (Stretch)
def addition(a, n):
    sum = a
    for _ in range(n):
        sum += 1
    return sum

def multiplication(a, n):
    product = a
    for _ in range(n - 1):
         product = addition(product, a)
    return product

def exponentiation(a, n):
    exponent_result = a
    for _ in range(n - 1):
        exponent_result = multiplication(exponent_result, a)
    return exponent_result
    
def tetration(a, n):
    tetrate = a
    for _ in range(n - 1):
         tetrate = exponentiation(a, tetrate)
    return tetrate

#print(tetration(3, 3))

# Part 2 (euclid)





########################################################






# Name: Iteration Unit Test
# Time: 9.7.2023 @ 9:02 am

# Helper Functions
import operator as op
import traceback
from datetime import datetime

eq_comp = op.__eq__
is_comp = op.is_

def perm_eq(p1, p2):
    if not isinstance(p1, str) or not isinstance(p2, str):
        return False
    def to_dct(perm):
        split_perm = perm[1:len(perm)-1].split(')(')
        dct = {}
        for chunk in split_perm:
            n = len(chunk)
            for i in range(n):
                if i < n - 1:
                    dct[chunk[i]] = chunk[i+1]
                else:
                    dct[chunk[i]] = chunk[0]
        return dct
    return(to_dct(p1) == to_dct(p2))

def elems_comp(a_list, b_list):
    # Return true if every element of a is an element of b and vice versa, False otherwise
    if not isinstance(a_list, list) or not isinstance(b_list, list):
        return False
    for elem in a_list:
        if elem not in b_list:
            return False
    for elem in b_list:
        if elem not in b_list:
            return False
    return True

def order_comp(a_list, b_list):
    for i in range(len(a_list)):
        try:
            if a_list[i] != b_list[i]:
                return False
        except:
            return False
    return True

def eq_not_is(an_obj, another_obj):
    return (an_obj == another_obj) and not(an_obj is another_obj)

def approx_eq(expected, actual):
    if expected is None and actual is None:
        return True
    if isinstance(expected, (int, float, complex)):
        if not isinstance(actual, (int, float, complex)):
            return False
        return abs(expected - actual) < 0.000001
    return False

def build_arg_str(args, is_poly):
    arg_str = ""
    if is_poly:
        for arg in args:
            if callable(arg):
                arg_str = arg_str + arg.__name__ + " "
            else:
                if isinstance(arg, str):
                    arg_str = arg_str + "'" + arg + "'" + " "
                else:
                    arg_str = arg_str + str(arg) + " "
    else:
        if callable(args):
            arg_str = args.__name__
        else:
            if isinstance(args, str):
                arg_str = "'" + args + "'"
            else:
                arg_str = str(args)
    return arg_str.strip()

class Unit():

    def __init__(self, func, name, cases, is_polyadic, is_mutator, test_type, extra_credit = False):
        # If the function is polyadic, we need to * the input so that it unpacks.
        # If the function is a mutator, we don't ask for its return value.
        # Instead we compare the input after the function is called to the correct mutated value.
        # Six test types are required:
        # 1. Verify equality of value: eq_comp
        # 2. Verify identity: is_comp
        # 3. Verify equality of value and non-identity: eq_not_is
        # 4. Verify that two lists have the same elements, order irrelevant: elems_comp
        # 5. Verify that two lists have same elements in same order: order_comp
        # 6. Verify that two floats are close enough: approx_eq
        self.func = func
        self.name = name
        self.cases = cases
        self.is_polyadic = is_polyadic
        self.is_mutator = is_mutator
        self.test_type = test_type
        self.score = 0
        self.extra_credit = extra_credit

    def add_test(self, new_test):
        self.cases.append(new_test)

class UnitTest():

    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.score = 0
        self.num_tests = 0

    def run_test(self):
        test_file = open("report.txt", "w")
        test_file.write(self.name + "\n")
        now = datetime.now()
        dt_string = now.strftime("Date: %m/%d/%Y, Time: %H:%M:%S")
        test_file.write(dt_string + "\n")
        total_score = 0
        pts_lost_dict = {}
        for unit in self.units:
            pts_lost_dict[unit.name] = 0
            if unit.extra_credit:
                header_str = "\nFunction: \"" + unit.name + "\"" + "(extra credit)\n"
            else:
                header_str = "\nFunction: \"" + unit.name + "\"\n"
            test_file.write(header_str)
            for case in unit.cases:
                if not unit.extra_credit:
                    self.num_tests += 1
                arg = case[0]
                expected_value = case[1]
                arg_str = build_arg_str(arg, unit.is_polyadic)
                test_file.write("Argument(s): " + arg_str + "  ")
                # Now flush the contents of the write buffer so that if a function hangs,
                # the report will show precisely where it happened.
                test_file.flush()
                try:
                    if unit.is_polyadic:
                        actual_value = unit.func(*arg)
                    else:
                        actual_value = unit.func(arg) 
                except Exception as err:
                    # Do not print error if function hasn't been implemented (no arguments defined but passing args error).
                    # This avoids giving students a wall of errors when starting project.
                    if "takes 0 positional arguments but" not in str(err):
                        # Print error to console
                        traceback.print_exc()
                    test_file.write("Crash! No points!\n")
                    pts_lost_dict[unit.name] += 1
                else:
                    if not unit.is_mutator:
                        if unit.test_type(expected_value, actual_value):
                            test_file.write("  Return value correct! +1\n")
                            unit.score += 1
                        else:
                            test_file.write("  Incorrect return value! No point!\n")
                            pts_lost_dict[unit.name] += 1
                    else:
                        if unit.is_polyadic:
                            mutated_value = arg[0]
                        else:
                            mutated_value = arg
                        if unit.test_type(expected_value, mutated_value):
                            test_file.write("  Mutated value correct! +1\n")
                            unit.score += 1
                        else:
                            test_file.write("  Incorrect mutated value! No point!\n")
                            pts_lost_dict[unit.name] += 1

            total_score += unit.score

        self.score = total_score
        test_file.write("\nSummary:")
        if self.score < self.num_tests:
            for name in pts_lost_dict:
                pts_lost = pts_lost_dict[name]
                if pts_lost > 0:
                    test_file.write("\nFunction \"" + name + "\", points lost " + str(pts_lost) + ".")
        else:
            test_file.write(" Perfection!")
        summary = "Final Score: " + str(self.score) + "/" + str(self.num_tests)
        grade = round((self.score / self.num_tests) * 100, 1)
        summary += "\nGrade: " + str(grade) + "%"
        test_file.write("\n\n" + summary)
        print(summary)

# Test Cases (tc)
# Format: a list of tuples where each tuple
# gives an argument (or tuple of arguments)
# and the expected return for that argument.
sum_squares_tc = [([], 0), ([3], 9), ([3, 33, 333], 111987)]
factorial_tc = [(0, 1), (1, 1), (2, 2), (12, 479001600)]
sumtorial_tc = [(0, 0), (1, 1), (2, 3), (12, 78)]
sum_n_odds_tc = [(0, 0), (1, 1), (2, 4), (144, 20736)]
sum_odds_to_n_tc = [(0, 0), (1, 1), (3, 4), (12**4 + 1, 107516161)]
fib_tc = [(3, 2), (30, 832040), (300, 222232244629420445529739893461909967206666939096499764990979600)]
trib_tc = [(1, 0), (8, 13), (16, 1705)]
harmonic_series_tc = [(1, 1.0), (10, 2.9289682539682538), (100, 5.187377517639621), (1000, 7.485470860550343)]
alt_signs_tc = [(0, 0), (1, 1), (12, -6), (145, 73)]
pi_approx_tc = [(1, 4.0), (100, 3.1315929035585537), (10000, 3.1414926535900345), (1000000, 3.1415916535897743)]
geometric_series_tc = [((0, 0, 0), 0), ((1, 1, 1), 1), ((-1, 12, -1), 0), ((12, 144, 1/3), 18), ((12, 288, -1/3), 9)]
iter_iter_tc = [(1, 1.0), (10, 4.308168776769968), (100, 8.739771135094355)]
addition_tc = [((123, 456), 579)]
multiplication_tc = [((123, 456), 56088)]
exponentiation_tc = [((12, 7), 35831808)]
tetration_tc = [((2, 4), 65536)]

# Create Units
# This block will cause a crash if you haven't created all of the required functions.
# Format: Unit(func, name, cases, is_polyadic, is_mutator, test_type)
# Test types: eq_comp, is_comp, eq_not_is, elems_comp
sum_squares_unit = Unit(sum_squares, "sum of squares", sum_squares_tc, False, False, eq_comp)
factorial_unit = Unit(factorial, "factorial", factorial_tc, False, False, eq_comp)
sumtorial_unit = Unit(sumtorial, "sumtorial", sumtorial_tc, False, False, eq_comp)
sum_n_odds_unit = Unit(sum_n_odds, "sum n odds", sum_n_odds_tc, False, False, eq_comp)
sum_odds_to_n_unit = Unit(sum_odds_to_n, "sum odds to n", sum_odds_to_n_tc, False, False, eq_comp)
fib_unit = Unit(fib, "fibonacci sequence", fib_tc, False, False, eq_comp)
trib_unit = Unit(trib, "tribonacci sequence", trib_tc, False, False, eq_comp)
harmonic_series_unit = Unit(harmonic_series, "harmonic series", harmonic_series_tc, False, False, approx_eq)
alt_signs_unit = Unit(alt_signs, "alternate signs", alt_signs_tc, False, False, approx_eq)
pi_approx_unit = Unit(pi_approx, "pi approximated", pi_approx_tc, False, False, approx_eq)
geometric_series_unit = Unit(geometric_series, "geometric series", geometric_series_tc, True, False, approx_eq)
iter_iter_unit = Unit(iter_iter, "iterated iteration", iter_iter_tc, False, False, eq_comp)
addition_unit = Unit(addition, "addition", addition_tc, True, False, eq_comp)
multiplication_unit = Unit(multiplication, "multiplication", multiplication_tc, True, False, eq_comp)
exponentiation_unit = Unit(exponentiation, "exponentiation", exponentiation_tc, True, False, eq_comp)
tetration_unit = Unit(tetration, "tetration", tetration_tc, True, False, eq_comp)

# Unit Test List
units = [sum_squares_unit, factorial_unit, sumtorial_unit, sum_n_odds_unit, sum_odds_to_n_unit, fib_unit, trib_unit,
         harmonic_series_unit, alt_signs_unit, pi_approx_unit, geometric_series_unit, iter_iter_unit,
         addition_unit, multiplication_unit, exponentiation_unit, tetration_unit]

# Create Unit Test
unit_test = UnitTest("Iteration Unit Test", units)

# Test!
unit_test.run_test()