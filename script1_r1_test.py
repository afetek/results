# Get Script Variables: timestamp: 3815802
# generated script variable --> self.s2 = 11: timestamp: 3815817
# generated script variable --> self.TEST_RUN = "r1": timestamp: 3815837
# generated script variable --> self.description = "hello r1": timestamp: 3815857
# generated script variable --> self.s1 = 1: timestamp: 3815877
# Test Setup --> r1 Debug Level: 3: timestamp: 3815883
# Start Test --> : timestamp: 3816226
# signal1: 1: timestamp: 3816227
# signal2: 11: timestamp: 3816227
# self.model.c1.Value == 2.0: timestamp: 3831094
# self.model.c2.Value == 2.0: timestamp: 3831094
# self.model.c3.Value == 3.0: timestamp: 3831094
# Validation Timestamp: 3831094: timestamp: 3831094
# set c1: timestamp: 3831094

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 3831094: timestamp: 3831094
# set c2: timestamp: 3831094

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 3831094: timestamp: 3831094
# set c3: timestamp: 3831094

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 3842085
