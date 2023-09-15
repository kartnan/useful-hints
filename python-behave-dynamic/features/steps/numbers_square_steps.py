# from behave import *
#
# def parse_input_pairs(input_pairs_str):
#     pair_strings = input_pairs_str.split(';')
#     input_pairs = [tuple(map(int, pair.split(','))) for pair in pair_strings]
#     return input_pairs
#
# @given("the input pairs are {input_pairs}")
# def set_input_pairs(context, input_pairs):
#     input_pairs_str = context.config.userdata.get("input_pairs")
#     context.input_pairs = parse_input_pairs(input_pairs_str)
#
# @when("I add the input pairs")
# def add_input_pairs(context):
#     sum_of_pair = context.input_pairs[0] + context.input_pairs[1]
#     print("The sum of the pair", str(context.input_pairs), "is", str(sum_of_pair))
#
# @then("the sum of the input pairs is {expected_sum}")
# def verify_sum_of_input_pairs(context, expected_sum):
#     print("The sum of the input pairs is:", context.input_pairs)

from behave import step

@step(u'the {number:d} squared is {result:d}')
def step_impl(context, number, result):
    assert number*number == result