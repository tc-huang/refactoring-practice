# Reference: https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs
import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert inc_dec.decrement(3) == 2
