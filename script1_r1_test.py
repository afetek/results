# Get Script Variables: timestamp: 1945146
# generated script variable --> self.s2 = 11: timestamp: 1945161
# generated script variable --> self.TEST_RUN = "r1": timestamp: 1945181
# generated script variable --> self.description = "hello r1": timestamp: 1945201
# generated script variable --> self.s1 = 1: timestamp: 1945221
# Test Setup --> r1 Debug Level: 3: timestamp: 1945227
# Start Test --> : timestamp: 1945372
# signal1: 1: timestamp: 1945373
# signal2: 11: timestamp: 1945373
# Waitng ...: timestamp: 1945373
# ... Ok: timestamp: 1948621
# self.model.c1.Value == 2.0: timestamp: 1948621
# self.model.c1.Value == 2.0: timestamp: 1948621
# self.model.c3.Value == 3.0: timestamp: 1948621
# Validation Timestamp: 1948621: timestamp: 1948621
# set c1: timestamp: 1948621

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 1948621: timestamp: 1948621
# set c2: timestamp: 1948621

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 1948621: timestamp: 1948621
# set c3: timestamp: 1948621

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 1950198
