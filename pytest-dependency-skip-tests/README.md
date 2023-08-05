I had a situation where I had to run a test case using pytest.

If the test case fails, I wanted to trigger another test case which does some investigation on why the original test failed.

This was a special case because usually tests are skipped if a previous test had failed.

Luckily I found this thread on stackoverflow https://stackoverflow.com/questions/53545315/can-pytest-run-a-test-iff-another-fails

I installed pytest_dependency using pip and used the code from the above link.

For some reason, it failed. I then added scope="module" and then the tests passed.

On entering pytest -v test5.py,

1. test_foo will run. If it passes, test_bar will be skipped.
2. If test_foo fails, test_bar will run.

I tried using parameterization, xdist etc but then both the tests started to execute no matter what.

Credits to the original author https://stackoverflow.com/users/2650249/hoefling