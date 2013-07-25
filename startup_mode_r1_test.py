# Get Script Variables: timestamp: 5452671
# generated script variable --> self.TEST_RUN = "r1": timestamp: 5452686
# generated script variable --> self.fan1_fault = "False": timestamp: 5452706
# generated script variable --> self.fan2_fault = "False": timestamp: 5452726
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 5452746
# Test Setup --> r1 Debug Level: 3: timestamp: 5452752
# Start Test --> : timestamp: 5453077
# Powerup Test Script: timestamp: 5453078
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5453078
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5453078
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5453078
# self.model.powerECU.Value == 1.0: timestamp: 5453078

def test1_test_test():
    """
    script1 run r1 test 1: Exception in Validation: Model instance has no attribute 'fan2_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"



def test2_test_test():
    """
    script1 run r1 test 2: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5453132: timestamp: 5453132
# No Fans Available EICAS message: timestamp: 5453132

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 5453132
