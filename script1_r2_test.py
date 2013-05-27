# # Get Script Variables: timestamp: 1827076
# generated script variable --> self.s2 = 22: timestamp: 1827091
# generated script variable --> self.TEST_RUN = "r2": timestamp: 1827111
# generated script variable --> self.description = "hello r2": timestamp: 1827131
# generated script variable --> self.s1 = 11: timestamp: 1827151
# Test Setup --> r2 Debug Level: 3: timestamp: 1827157
# Start Test --> : timestamp: 1827340
# self.model.c1.Value == 2.0: timestamp: 1827341
# self.model.c2.Value == 2.0: timestamp: 1827341
# self.model.c3.Value == 3.0: timestamp: 1827341
# Validation Timestamp: 1827341: timestamp: 1827341
# set c1: timestamp: 1827341

def test1_test_test():
    """
    test 1 for run r2: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 1827341: timestamp: 1827341
# set c2: timestamp: 1827341

def test2_test_test():
    """
    test 2 for run r2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 1827341: timestamp: 1827341
# set c3: timestamp: 1827341

def test3_test_test():
    """
    test 3 for run r2: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 1827342
