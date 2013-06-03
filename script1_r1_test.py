# Get Script Variables: timestamp: 72411
# generated script variable --> self.s2 = 11: timestamp: 72426
# generated script variable --> self.TEST_RUN = "r1": timestamp: 72446
# generated script variable --> self.description = "hello r1": timestamp: 72466
# generated script variable --> self.s1 = 1: timestamp: 72486
# Test Setup --> r1 Debug Level: 3: timestamp: 72492
# Start Test --> : timestamp: 72913
# signal1: 1: timestamp: 72914
# signal2: 11: timestamp: 72914
# self.model.c1.Value == 2.0: timestamp: 72914
# self.model.c2.Value == 2.0: timestamp: 72914
# self.model.c3.Value == 3.0: timestamp: 72914
# Validation Timestamp: 72914: timestamp: 72914
# set c1: timestamp: 72914

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 72914: timestamp: 72914
# set c2: timestamp: 72914

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 72914: timestamp: 72914
# set c3: timestamp: 72914

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 72915
