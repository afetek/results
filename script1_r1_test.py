# Get Script Variables: timestamp: 152535
# generated script variable --> self.s2 = 11: timestamp: 152550
# generated script variable --> self.TEST_RUN = "r1": timestamp: 152570
# generated script variable --> self.description = "hello r1": timestamp: 152590
# generated script variable --> self.s1 = 1: timestamp: 152610
# Test Setup --> r1 Debug Level: 3: timestamp: 152616
# Start Test --> : timestamp: 152958
# signal1: 1: timestamp: 152959
# signal2: 11: timestamp: 152959
# self.model.c1.Value == 2.0: timestamp: 152959
# self.model.c2.Value == 2.0: timestamp: 152959
# self.model.c3.Value == 3.0: timestamp: 152959
# Validation Timestamp: 152959: timestamp: 152959
# set c1: timestamp: 152959

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 152959: timestamp: 152959
# set c2: timestamp: 152959

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 152959: timestamp: 152959
# set c3: timestamp: 152959

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 152960
