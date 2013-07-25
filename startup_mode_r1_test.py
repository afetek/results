# Get Script Variables: timestamp: 51600290
# generated script variable --> self.fan1_fault = False: timestamp: 51600305
# generated script variable --> self.fan2_fault = False: timestamp: 51600325
# generated script variable --> self.TEST_RUN = "r1": timestamp: 51600345
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 51600365
# Test Setup --> r1 Debug Level: 3: timestamp: 51600371
# Start Test --> : timestamp: 51600701
# Powerup Test Script: timestamp: 51600702
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 51600702
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 51600702
# 
# Validation Timestamp: 51600744: timestamp: 51600744
# fan 1 should power on: timestamp: 51600744

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 51601702: timestamp: 51601702
# fan 2 should not power on: timestamp: 51601702

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 51601702: timestamp: 51601702
# Both fans are Available EICAS message: timestamp: 51601702

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 51601702
