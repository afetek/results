# # Get Script Variables: timestamp: 10003306
# generated script variable --> self.s2 = 22: timestamp: 10003321
# generated script variable --> self.TEST_RUN = "r2": timestamp: 10003341
# generated script variable --> self.description = "hello r2": timestamp: 10003361
# generated script variable --> self.s1 = 11: timestamp: 10003381
# Test Setup --> r2 Debug Level: 3: timestamp: 10003387
# Start Test --> : timestamp: 10003765
# self.model.c1.Value == 1.0: timestamp: 10003766
# self.model.c2.Value == 2.0: timestamp: 10003766
# self.model.c3.Value == 3.0: timestamp: 10003766
# Validation Timestamp: 10003766: timestamp: 10003766
# set c2: timestamp: 10003766

def test1_r2_test_test():
    """
    Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_r2_test"


# Validation Timestamp: 10003766: timestamp: 10003766
# set c3: timestamp: 10003766

def test2_r2_test_test():
    """
    Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test2_r2_test"


# Validation Timestamp: 10004766: timestamp: 10004766
# set c1: timestamp: 10004766

def test3_r2_test_test():
    """
    Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 2.0
    """

    test_passed = False
    assert test_passed, "Failed test3_r2_test"


# Test Done --> r2: timestamp: 10004766

def test4_r2_test_test():
    """
    Confirm event EVENT_1 is ACTIVE
    """

    test_passed = False
    assert test_passed, "Failed test4_r2_test"


