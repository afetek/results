# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4424201
# Get Test Data Variables: timestamp: 4424202
# test data variable --> self.fan1_fault = True: timestamp: 4424217
# test data variable --> self.fan2_fault = True: timestamp: 4424237
# test data variable --> self.TEST_RUN = "r4": timestamp: 4424257
# test data variable --> self.powerup = False: timestamp: 4424277
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 4424297
# Test Setup --> r4 Debug Level: 3: timestamp: 4424303
# Start Test --> : timestamp: 4424535
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 4424536
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 4424536
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4424536
# 
# Validation Timestamp: 4425536: timestamp: 4425536
# fan 1 should not power on: timestamp: 4425536

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4425536: timestamp: 4425536
# fan 2 should not power on: timestamp: 4425536

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# 
# Validation Timestamp: 4425536: timestamp: 4425536
# no fans available: timestamp: 4425536

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# Test Done --> r4: timestamp: 4425536
