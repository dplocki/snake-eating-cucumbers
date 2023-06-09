from radish import given, when, then


@given("calculator")
def _(step):
    pass


@when("add number {a:g} to number {b:g}")
def _(step, a, b):
    step.context.result = step.context.calculator.add(a, b)


@when("sub number {a:g} from number {b:g}")
def _(step, a, b):
    step.context.result = step.context.calculator.sub(b, a)


@when("multiple number {a:g} and number {b:g}")
def _(step, a, b):
    step.context.result = step.context.calculator.mul(a, b)


@then("result should be equal {result:g}")
def _(step, result):
    assert step.context.result == result
