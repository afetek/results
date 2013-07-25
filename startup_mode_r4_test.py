# Get Script Variables: timestamp: 5458799
# generated script variable --> self.TEST_RUN = "r4": timestamp: 5458814
# generated script variable --> self.fan1_fault = "True": timestamp: 5458834
# generated script variable --> self.fan2_fault = "True": timestamp: 5458854
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 5458874
# Test Setup --> r4 Debug Level: 3: timestamp: 5458880
# Start Test --> : timestamp: 5459205
# Powerup Test Script: timestamp: 5459206
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5459206
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5459206
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5459206
# self.model.powerECU.Value == 1.0: timestamp: 5459206

def test1_test_test():
    """
    script1 run r4 test 1: Exception in Validation: Model instance has no attribute 'fan2_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"



def test2_test_test():
    """
    script1 run r4 test 2: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5459271: timestamp: 5459271
# No Fans Available EICAS message: timestamp: 5459271

def test3_test_test():
    """
    script1 run r4 test 3: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 5459271
