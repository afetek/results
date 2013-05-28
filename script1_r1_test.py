# # Get Script Variables: timestamp: 5854126
# generated script variable --> self.s2 = 11: timestamp: 5854141
# generated script variable --> self.TEST_RUN = "r1": timestamp: 5854161
# generated script variable --> self.description = "hello r1": timestamp: 5854181
# generated script variable --> self.s1 = 1: timestamp: 5854201
# Test Setup --> r1 Debug Level: 3: timestamp: 5854207
# Start Test --> : timestamp: 5854383
# signal1: 1: timestamp: 5854384
# signal2: 11: timestamp: 5854384
# self.model.c1.Value == 2.0: timestamp: 5854384
# self.model.c2.Value == 2.0: timestamp: 5854384
# self.model.c3.Value == 3.0: timestamp: 5854384
# Validation Timestamp: 5854384: timestamp: 5854384
# set c1: timestamp: 5854384

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5854384: timestamp: 5854384
# set c2: timestamp: 5854384

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5854384: timestamp: 5854384
# set c3: timestamp: 5854384

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 5854385
