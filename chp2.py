#Quotient and Remainder
def quotient (m, n):
  return m // n
def remainder (m, n):
  return m % n

#Circle Area
def circle_area(radius):
  PI = 3.14159
  return PI * radius ** 2

#Fahrenheit to Celsius
def f_to_c(temp_in_f):
  return (temp_in_f - 32) * 5/9

#Celcius to Fahrenheit
def c_to_f(temp_in_c):
  return (temp_in_c * 9/5) + 32

#Weighted Average
def hg_grade (q_1, q_2, f_e):
  return q_1 * 0.4 + q_2 * 0.4 + f_e * 0.2

#What do I need on the Final?
def grade_needed(grade_wanted, q_1_grade, q_2_grade):
  return -2 * (q_1_grade + q_2_grade) + 5 * grade_wanted

#Equation of a Line
def linear_eq(slope, y_intercept, x_coord):
  return slope * x_coord + y_intercept

#Cube Root
def cube_rt(a_num):
  return a_num ** (1/3)

#nth Root
def nth_rt(m, n):
  return m ** (1/n)

#Distance
def distance(x_1, y_1, x_2, y_2):
  return nth_rt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2, 2)

#Absolute Value
def abs_val(a_num):
  return nth_rt(a_num ** 2, 2)

#Digit Chop
def digit_chop(m, n):
  return m // (10 ** (n - 1)) % 10

#24 Hour Clock
def alarm_clock(current_24hr, hrs_until_alarm):
  return (current_24hr + hrs_until_alarm) % 24

#Change
def make_change(number_cents):
  qs = number_cents // 25
  ds = (number_cents - qs * 25) // 10
  ns = (number_cents - qs * 25 - ds * 10) // 5
  ps = (number_cents - qs * 25 - ds * 10 - ns * 5) // 1
  return qs, ds, ns, ps

#Distance from Point to Line (Stretch)
def pt_to_line(x_cs, y_cs, slope, y_intercept):
  A = slope
  B = -1
  C = y_intercept
  d = (abs(A * x_cs + B * y_cs + C)) / (nth_rt((A ** 2 + B ** 2), 2))
  return d



###########################################



# Name: Way of the Func Unit Test
# Time: 8.30.2023 @ 2:16 pm

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
quotient_tc = [((21, 5), 4),
               ((21, 10), 2),
               ((21, 21), 1),
               ((21, 22), 0)]
remainder_tc = [((21, 5), 1),
               ((21, 6), 3),
               ((21, 21), 0),
               ((21, 22), 21)]
circle_area_tc = [(0, 0.0),
                  (1, 3.14159),
                  (3.14159, 31.006198110721677)]
f_to_c_tc = [(-100, -73.33333333333334),
          (333, 167.22222222222223)]
c_to_f_tc = [(-300, -508.0),
             (555, 1031.0)]
hg_grade_tc = [((77, 72, 99), 79.4),
               ((92, 96, 81), 91.40000000000002)]
grade_needed_tc = [((90, 72, 92), 121.99999999999996),
                   ((80, 72, 92), 71.99999999999996)]
linear_eq_tc = [((-3.2, -15, 4), -27.8),
                ((0, 8.5, 99), 8.5)]
cube_rt_tc = [(0, 0.0),
            (1, 1.0),
            (1024, 10.079368399158984)]
nth_rt_tc = [((1, 1), 1.0),
             ((144, 5), 2.701920077041227)]
distance_tc = [((0, 0, 0, 0), 0.0),
               ((1, 2, 3, 4), 2.8284271247461903),
               ((-4, 5, -6, -7), 12.165525060596439)]
abs_val_tc = [(0, 0.0),
              (-15, 15.0),
              (17.9, 17.9)]
digit_chop_tc = [((0, 1), 0),
                 ((12345, 4), 2)]
alarm_clock_tc = [((0, 0), 0),
                  ((0, 28), 4),
                  ((28, 128), 12)]
make_change_tc = [(0, (0, 0, 0, 0)),
                  (14, (0, 1, 0, 4)),
                  (66, (2, 1, 1, 1)),
                  (99, (3, 2, 0, 4))]
pt_to_line_tc = [((0, -6, 0, 15), 21),
                 ((6, -2, 2, -3), 4.9193495505)]


# Create Units
# This block will cause a crash if you haven't created all of the required functions.
# Format: Unit(self, func, name, cases, is_polyadic, is_mutator, test_type)
quotient_unit = Unit(quotient, "quotient", quotient_tc, True, False, eq_comp)
remainder_unit = Unit(remainder, "remainder", remainder_tc, True, False, eq_comp)
circle_area_unit = Unit(circle_area, "circle area", circle_area_tc, False, False, approx_eq)
f_to_c_unit = Unit(f_to_c, "Fahrneheit to Celcius", f_to_c_tc, False, False, approx_eq)
c_to_f_unit = Unit(c_to_f, "Celcius to Fahrenheit", c_to_f_tc, False, False, approx_eq)
hg_grade_unit = Unit(hg_grade, "honors geo grade", hg_grade_tc, True, False, approx_eq)
grade_needed_unit = Unit(grade_needed, "grade needed on final", grade_needed_tc, True, False, approx_eq)
linear_eq_unit = Unit(linear_eq, "linear equation", linear_eq_tc, True, False, eq_comp)
cube_rt_unit = Unit(cube_rt,"square root", cube_rt_tc, False, False, approx_eq)
nth_rt_unit = Unit(nth_rt,"nth root", nth_rt_tc, True, False, approx_eq)
distance_unit = Unit(distance, "distance", distance_tc, True, False, approx_eq)
abs_val_unit = Unit(abs_val, "absolute value", abs_val_tc, False, False, approx_eq)
digit_chop_unit = Unit(digit_chop, "digit chop", digit_chop_tc, True, False, eq_comp)
alarm_clock_unit = Unit(alarm_clock, "alarm clock", alarm_clock_tc, True, False, eq_comp)
make_change_unit = Unit(make_change, "make change", make_change_tc, False, False, eq_comp)
pt_to_line_unit = Unit(pt_to_line, "distance from point to line", pt_to_line_tc, True, False, approx_eq)

# Unit Test List
units = [quotient_unit, remainder_unit, circle_area_unit, f_to_c_unit, c_to_f_unit,
         hg_grade_unit, grade_needed_unit, linear_eq_unit, cube_rt_unit, nth_rt_unit, distance_unit,
         abs_val_unit, digit_chop_unit, alarm_clock_unit, make_change_unit, pt_to_line_unit]

# Create Unit Test
unit_test = UnitTest("The Way of the Function Unit Test", units)

# Test!
unit_test.run_test()