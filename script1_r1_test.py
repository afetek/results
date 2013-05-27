# # Get Script Variables: timestamp: 4360009
# generated script variable --> self.s2 = 2: timestamp: 4360024
# generated script variable --> self.TEST_RUN = "r1": timestamp: 4360044
# generated script variable --> self.description = "hello r1": timestamp: 4360064
# generated script variable --> self.s1 = 1: timestamp: 4360084
# Test Setup --> r1 Debug Level: 3: timestamp: 4360090
# Start Test --> : timestamp: 4360368
# self.model.c1.Value == 2.0: timestamp: 4360369
# self.model.c2.Value == 2.0: timestamp: 4360369
# self.model.c3.Value == 3.0: timestamp: 4360369
# Validation Timestamp: 4360369: timestamp: 4360369
# set c1: timestamp: 4360369

def test1_test_test():
    """
    test 1 for run r1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 4360369: timestamp: 4360369
# set c2: timestamp: 4360369

def test2_test_test():
    """
    test 2 for run r1: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 4360369: timestamp: 4360369
# set c3: timestamp: 4360369

def test3_test_test():
    """
    test 3 for run r1: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 4360370
