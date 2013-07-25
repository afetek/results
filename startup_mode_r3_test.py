# Get Script Variables: timestamp: 43842884
# Conversion for fan1_fault (enum) is (enum): timestamp: 43842894
# generated script variable --> self.fan1_fault = False: timestamp: 43842899
# Conversion for fan2_fault is (none): timestamp: 43842914
# generated script variable --> self.fan2_fault = "True": timestamp: 43842919
# Conversion for TEST_RUN is (none): timestamp: 43842934
# generated script variable --> self.TEST_RUN = "r3": timestamp: 43842939
# Conversion for description is (none): timestamp: 43842954
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 43842959
# Test Setup --> r3 Debug Level: 3: timestamp: 43842965
# Start Test --> : timestamp: 43843204
# Powerup Test Script: timestamp: 43843205
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 43843205
# Assignment: self.model.fan2FaultRead.Value = 1.0: timestamp: 43843205
# Assignment: self.model.powerECU.Value = 1.0: timestamp: 43843205
# Validation Timestamp: 43843251: timestamp: 43843251
# fan 1 should power on: timestamp: 43843251

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 43844205: timestamp: 43844205
# fan 2 should not power on: timestamp: 43844205

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 43844205: timestamp: 43844205
# Both fans are Available EICAS message: timestamp: 43844205

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is >= 1 and <= 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 43844205
