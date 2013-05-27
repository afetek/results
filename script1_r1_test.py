# # Get Script Variables: timestamp: 6772927
# generated script variable --> self.s2 = 2: timestamp: 6772942
# generated script variable --> self.TEST_RUN = "r1": timestamp: 6772962
# generated script variable --> self.description = "hello r1": timestamp: 6772982
# generated script variable --> self.s1 = 1: timestamp: 6773002
# Test Setup --> r1 Debug Level: 3: timestamp: 6773008
# Start Test --> : timestamp: 6773183
# signal1: 1: timestamp: 6773184
# signal2: 2: timestamp: 6773184
# self.model.c1.Value == 2.0: timestamp: 6773184
# self.model.c2.Value == 2.0: timestamp: 6773184
# self.model.c3.Value == 3.0: timestamp: 6773184
# Validation Timestamp: 6773184: timestamp: 6773184
# set c1: timestamp: 6773184

def test1_test_test():
    """
    test 1 for run r1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 6773184: timestamp: 6773184
# set c2: timestamp: 6773184

def test2_test_test():
    """
    test 2 for run r1: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 6773184: timestamp: 6773184
# set c3: timestamp: 6773184

def test3_test_test():
    """
    test 3 for run r1: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 6773185
