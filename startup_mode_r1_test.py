# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Description: Fans OK at startup
# #######################################################
# : timestamp: 9283003
# Start Test: : timestamp: 9283234
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 9283235
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 9283235
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 9283235
# 
# Validation Timestamp: 9283279: timestamp: 9283279
# fan 1 should power on: timestamp: 9283279

def r1_tc1_test():
    """
    r1_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9284235: timestamp: 9284235
# fan 2 should not power on: timestamp: 9284235

def r1_tc2_test():
    """
    r1_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 9284235
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 9284235
# 
# Validation Timestamp: 9284279: timestamp: 9284279
# both fans are available: timestamp: 9284279

def r1_tc3_test():
    """
    r1_tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9284279: timestamp: 9284279
# low fan speed: timestamp: 9284279

def r1_tc4_test():
    """
    r1_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 9284279
