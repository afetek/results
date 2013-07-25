# Get Script Variables: timestamp: 5456746
# generated script variable --> self.TEST_RUN = "r3": timestamp: 5456761
# generated script variable --> self.fan1_fault = "False": timestamp: 5456781
# generated script variable --> self.fan2_fault = "True": timestamp: 5456801
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 5456821
# Test Setup --> r3 Debug Level: 3: timestamp: 5456827
# Start Test --> : timestamp: 5457160
# Powerup Test Script: timestamp: 5457161
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5457161
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5457161
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5457161
# self.model.powerECU.Value == 1.0: timestamp: 5457161

def test1_test_test():
    """
    script1 run r3 test 1: Exception in Validation: Model instance has no attribute 'fan2_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"



def test2_test_test():
    """
    script1 run r3 test 2: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5457232: timestamp: 5457232
# No Fans Available EICAS message: timestamp: 5457232

def test3_test_test():
    """
    script1 run r3 test 3: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 5457232
