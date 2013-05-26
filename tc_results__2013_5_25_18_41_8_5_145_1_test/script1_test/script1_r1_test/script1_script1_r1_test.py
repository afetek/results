# # Get Script Variables: timestamp: 10000212
# generated script variable --> self.s2 = 2: timestamp: 10000227
# generated script variable --> self.TEST_RUN = "r1": timestamp: 10000247
# generated script variable --> self.description = "hello r1": timestamp: 10000267
# generated script variable --> self.s1 = 1: timestamp: 10000287
# Test Setup --> r1 Debug Level: 3: timestamp: 10000293
# Start Test --> : timestamp: 10000673
# self.model.c1.Value == 1.0: timestamp: 10000674
# self.model.c2.Value == 2.0: timestamp: 10000674
# self.model.c3.Value == 3.0: timestamp: 10000674
# Validation Timestamp: 10000674: timestamp: 10000674
# set c2: timestamp: 10000674

def test1_r1_test_test():
    """
    Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_r1_test"


# Validation Timestamp: 10000674: timestamp: 10000674
# set c3: timestamp: 10000674

def test2_r1_test_test():
    """
    Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test2_r1_test"


# Validation Timestamp: 10001674: timestamp: 10001674
# set c1: timestamp: 10001674

def test3_r1_test_test():
    """
    Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 2.0
    """

    test_passed = False
    assert test_passed, "Failed test3_r1_test"


# Test Done --> r1: timestamp: 10001674

def test4_r1_test_test():
    """
    Confirm event EVENT_1 is ACTIVE
    """

    test_passed = False
    assert test_passed, "Failed test4_r1_test"


