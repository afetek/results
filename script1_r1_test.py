# Get Script Variables: timestamp: 10291917
# generated script variable --> self.s2 = 11: timestamp: 10291932
# generated script variable --> self.TEST_RUN = "r1": timestamp: 10291952
# generated script variable --> self.description = "hello r1": timestamp: 10291972
# generated script variable --> self.s1 = 1: timestamp: 10291992
# Test Setup --> r1 Debug Level: 3: timestamp: 10291998
# Start Test --> : timestamp: 10292407
# signal1: 1: timestamp: 10292408
# signal2: 11: timestamp: 10292408
# self.model.c1.Value == 2.0: timestamp: 10292408
# self.model.c2.Value == 2.0: timestamp: 10292408
# self.model.c3.Value == 3.0: timestamp: 10292408
# Validation Timestamp: 10292408: timestamp: 10292408
# set c1: timestamp: 10292408

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 10292408: timestamp: 10292408
# set c2: timestamp: 10292408

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 10292408: timestamp: 10292408
# set c3: timestamp: 10292408

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 10292409
