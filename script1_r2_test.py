# Get Script Variables: timestamp: 74492
# generated script variable --> self.s2 = 1111: timestamp: 74507
# generated script variable --> self.TEST_RUN = "r2": timestamp: 74527
# generated script variable --> self.description = "hello r2": timestamp: 74547
# generated script variable --> self.s1 = 111: timestamp: 74567
# Test Setup --> r2 Debug Level: 3: timestamp: 74573
# Start Test --> : timestamp: 74950
# signal1: 111: timestamp: 74951
# signal2: 1111: timestamp: 74951
# self.model.c1.Value == 2.0: timestamp: 74951
# self.model.c2.Value == 2.0: timestamp: 74951
# self.model.c3.Value == 3.0: timestamp: 74951
# Validation Timestamp: 74951: timestamp: 74951
# set c1: timestamp: 74951

def test1_test_test():
    """
    script1 run r2 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 74951: timestamp: 74951
# set c2: timestamp: 74951

def test2_test_test():
    """
    script1 run r2 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 74951: timestamp: 74951
# set c3: timestamp: 74951

def test3_test_test():
    """
    script1 run r2 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 74952
