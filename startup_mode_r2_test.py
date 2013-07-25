# Get Script Variables: timestamp: 45920637
# Convert value for fan1_fault (enum) to a (enum): timestamp: 45920647
# generated script variable --> self.fan1_fault = True: timestamp: 45920652
# Convert value for fan2_fault to a (none): timestamp: 45920667
# generated script variable --> self.fan2_fault = "False": timestamp: 45920672
# Convert value for TEST_RUN to a (none): timestamp: 45920687
# generated script variable --> self.TEST_RUN = "r2": timestamp: 45920692
# Convert value for description to a (none): timestamp: 45920707
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 45920712
# Test Setup --> r2 Debug Level: 3: timestamp: 45920718
# Start Test --> : timestamp: 45920995
# Powerup Test Script: timestamp: 45920996
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 45920996
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 45920996
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 45920996
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 45920996
# Validation Timestamp: 45921996: timestamp: 45921996
# fan 2 should power on: timestamp: 45921996

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 45921996: timestamp: 45921996
# fan 1 should not power on: timestamp: 45921996

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 45921996: timestamp: 45921996
# Fan 2 is available EICAS message: timestamp: 45921996

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 45921996
