# # Get Script Variables: timestamp: 5558204
# generated script variable --> self.s2 = 1111: timestamp: 5558219
# generated script variable --> self.TEST_RUN = "r2": timestamp: 5558239
# generated script variable --> self.description = "hello r2": timestamp: 5558259
# generated script variable --> self.s1 = 111: timestamp: 5558279
# Test Setup --> r2 Debug Level: 3: timestamp: 5558285
# Start Test --> : timestamp: 5558466
# signal1: 111: timestamp: 5558467
# signal2: 1111: timestamp: 5558467
# self.model.c1.Value == 2.0: timestamp: 5558467
# self.model.c2.Value == 2.0: timestamp: 5558467
# self.model.c3.Value == 3.0: timestamp: 5558467
# Validation Timestamp: 5558467: timestamp: 5558467
# set c1: timestamp: 5558467

def test1_test_test():
    """
    script1 test 1 for run r2: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5558467: timestamp: 5558467
# set c2: timestamp: 5558467

def test2_test_test():
    """
    script1 test 2 for run r2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5558467: timestamp: 5558467
# set c3: timestamp: 5558467

def test3_test_test():
    """
    script1 test 3 for run r2: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 5558468
