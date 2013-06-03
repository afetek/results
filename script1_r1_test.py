# Get Script Variables: timestamp: 4555941
# generated script variable --> self.s2 = 11: timestamp: 4555956
# generated script variable --> self.TEST_RUN = "r1": timestamp: 4555976
# generated script variable --> self.description = "hello r1": timestamp: 4555996
# generated script variable --> self.s1 = 1: timestamp: 4556016
# Test Setup --> r1 Debug Level: 3: timestamp: 4556022
# Start Test --> : timestamp: 4556373
# signal1: 1: timestamp: 4556374
# signal2: 11: timestamp: 4556374
# self.model.c1.Value == 2.0: timestamp: 4568589
# self.model.c2.Value == 2.0: timestamp: 4568589
# self.model.c3.Value == 3.0: timestamp: 4568589
# Validation Timestamp: 4568589: timestamp: 4568589
# set c1: timestamp: 4568589

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 4568589: timestamp: 4568589
# set c2: timestamp: 4568589

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 4568589: timestamp: 4568589
# set c3: timestamp: 4568589

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 4571621
