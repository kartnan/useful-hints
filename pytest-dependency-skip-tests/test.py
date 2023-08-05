import pytest

pytestmark = pytest.mark.depend_on_failures


# @pytest.mark.parametrize("value", [1, 2])
@pytest.mark.dependency()
@pytest.mark.xfail(reason='simulate failing test')
def test_foo():
    # print(value)
    # assert False
    assert True

# @pytest.mark.parametrize("value", [3, 4])
@pytest.mark.dependency(depends=['test_foo'])
def test_bar():
    # print(value)
    assert True
