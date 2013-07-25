# Get Script Variables: timestamp: 5454706
# generated script variable --> self.TEST_RUN = "r2": timestamp: 5454721
# generated script variable --> self.fan1_fault = "True": timestamp: 5454741
# generated script variable --> self.fan2_fault = "False": timestamp: 5454761
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 5454781
# Test Setup --> r2 Debug Level: 3: timestamp: 5454787
# Start Test --> : timestamp: 5455114
# Powerup Test Script: timestamp: 5455115
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5455115
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5455115
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5455115
# self.model.powerECU.Value == 1.0: timestamp: 5455115

def test1_test_test():
    """
    script1 run r2 test 1: Exception in Validation: Model instance has no attribute 'fan2_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"



def test2_test_test():
    """
    script1 run r2 test 2: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5455172: timestamp: 5455172
# No Fans Available EICAS message: timestamp: 5455172

def test3_test_test():
    """
    script1 run r2 test 3: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 5455172
