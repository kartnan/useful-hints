from behave import step

@step(u'the {number:d} squared is {result:d}')
def step_impl(context, number, result):
    assert number*number == result