# Get Script Variables: timestamp: 10293978
# generated script variable --> self.s2 = 1111: timestamp: 10293993
# generated script variable --> self.TEST_RUN = "r2": timestamp: 10294013
# generated script variable --> self.description = "hello r2": timestamp: 10294033
# generated script variable --> self.s1 = 111: timestamp: 10294053
# Test Setup --> r2 Debug Level: 3: timestamp: 10294059
# Start Test --> : timestamp: 10294455
# signal1: 111: timestamp: 10294456
# signal2: 1111: timestamp: 10294456
# self.model.c1.Value == 2.0: timestamp: 10294456
# self.model.c2.Value == 2.0: timestamp: 10294456
# self.model.c3.Value == 3.0: timestamp: 10294456
# Validation Timestamp: 10294456: timestamp: 10294456
# set c1: timestamp: 10294456

def test1_test_test():
    """
    script1 run r2 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 10294456: timestamp: 10294456
# set c2: timestamp: 10294456

def test2_test_test():
    """
    script1 run r2 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 10294456: timestamp: 10294456
# set c3: timestamp: 10294456

def test3_test_test():
    """
    script1 run r2 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 10294457
