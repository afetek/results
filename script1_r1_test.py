# Get Script Variables: timestamp: 2092649
# generated script variable --> self.s2 = 11: timestamp: 2092664
# generated script variable --> self.TEST_RUN = "r1": timestamp: 2092684
# generated script variable --> self.description = "hello r1": timestamp: 2092704
# generated script variable --> self.s1 = 1: timestamp: 2092724
# Test Setup --> r1 Debug Level: 3: timestamp: 2092730
# Start Test --> : timestamp: 2093085
# signal1: 1: timestamp: 2093086
# signal2: 11: timestamp: 2093086
# self.model.c1.Value == 2.0: timestamp: 2093086
# self.model.c2.Value == 2.0: timestamp: 2093086
# self.model.c3.Value == 3.0: timestamp: 2093086
# Validation Timestamp: 2093086: timestamp: 2093086
# set c1: timestamp: 2093086

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 2093086: timestamp: 2093086
# set c2: timestamp: 2093086

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 2093086: timestamp: 2093086
# set c3: timestamp: 2093086

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 2093087
