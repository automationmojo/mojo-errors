import unittest

from mojo.errors.xtraceback import (
    enhance_exception,
    format_exception
)

class TestError(Exception):
    """
        This is a test error used for testing the exceptionator.
    """

def failing_function(message = "This is a test error"):
    raise TestError(message)
    return


def fail_function_with_inner_function(message = "This is a test error"):
    
    def inner_function(blah):
        raise TestError(blah)
        return
    
    inner_function(message)
    
    return


class TestClass:

    def failing_function(message = "This is a test error"):
        raise TestError(message)
        return

    def fail_function_with_inner_function(message = "This is a test error"):
    
        def inner_function(blah):
            raise TestError(blah)
            return
        
        inner_function(message)
        
        return


class TestEnhancer(unittest.TestCase):

    def test_enhance_exception_simple(self):

        try:
            failing_function()
        except TestError as terr:
            enhance_exception(terr, "This is some extra content.", "BLAH")

            tblines = format_exception(terr)

            for line in tblines:
                print(line)

        return
    
    def test_enhance_exception_with_inner_function(self):

        try:
            fail_function_with_inner_function()
        except TestError as terr:
            enhance_exception(terr, "This is some extra content.", "BLAH")

            tblines = format_exception(terr)

            for line in tblines:
                print(line)

        return

    def test_enhance_exception_from_class_simple(self):

        try:
            tc = TestClass()
            tc.failing_function()
        except TestError as terr:
            enhance_exception(terr, "This is some extra content.", "BLAH")

            tblines = format_exception(terr)

            for line in tblines:
                print(line)

        return
    
    def test_enhance_exception_from_class_with_inner_function(self):

        try:
            tc = TestClass()
            tc.fail_function_with_inner_function()
        except TestError as terr:
            enhance_exception(terr, "This is some extra content.", "BLAH")

            tblines = format_exception(terr)

            for line in tblines:
                print(line)

        return


if __name__ == '__main__':
    unittest.main()
