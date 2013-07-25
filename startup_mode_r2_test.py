# Get Script Variables: timestamp: 44486075
# Conversion for fan1_fault (enum) is (enum): timestamp: 44486085
# generated script variable --> self.fan1_fault = True: timestamp: 44486090
# Conversion for fan2_fault is (none): timestamp: 44486105
# generated script variable --> self.fan2_fault = "False": timestamp: 44486110
# Conversion for TEST_RUN is (none): timestamp: 44486125
# generated script variable --> self.TEST_RUN = "r2": timestamp: 44486130
# Conversion for description is (none): timestamp: 44486145
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 44486150
# Test Setup --> r2 Debug Level: 3: timestamp: 44486156
# Start Test --> : timestamp: 44486397
# Powerup Test Script: timestamp: 44486398
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 44486398
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 44486398
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 44486398
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 44486398
# Validation Timestamp: 44487398: timestamp: 44487398
# fan 2 should power on: timestamp: 44487398

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 44487398: timestamp: 44487398
# fan 1 should not power on: timestamp: 44487398

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 44487398: timestamp: 44487398
# Fan 2 is available EICAS message: timestamp: 44487398

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 44487398
