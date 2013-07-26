# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 9295185
# Start Test: : timestamp: 9295414
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 9295415
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 9295415
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 9295415
# 
# Validation Timestamp: 9295459: timestamp: 9295459
# fan 1 should power on: timestamp: 9295459

def r5_tc1_test():
    """
    r5_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9296415: timestamp: 9296415
# fan 2 should not power on: timestamp: 9296415

def r5_tc2_test():
    """
    r5_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 9296415
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 9296415
# 
# Validation Timestamp: 9296458: timestamp: 9296458
# both fans are available: timestamp: 9296458

def r5_tc3_test():
    """
    r5_tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9296458: timestamp: 9296458
# low fan speed: timestamp: 9296458

def r5_tc4_test():
    """
    r5_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 9296458
