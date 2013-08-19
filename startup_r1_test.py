# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Description: Fans OK at startup
# #######################################################
# : timestamp: 7826400
# Start Test: : timestamp: 7826592
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7826593
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7826593
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7826593
# 
# Validation Timestamp: 7826628: timestamp: 7826628
# fan 1 should power on: timestamp: 7826628

def r1_tc1_test():
    """
    STARTUP r1 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7827593: timestamp: 7827593
# fan 2 should not power on: timestamp: 7827593

def r1_tc2_test():
    """
    STARTUP r1 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7827593
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7827593
# 
# Validation Timestamp: 7827620: timestamp: 7827620
# both fans are available: timestamp: 7827620

def r1_tc3_test():
    """
    STARTUP r1 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7827620: timestamp: 7827620
# low fan speed: timestamp: 7827620

def r1_tc4_test():
    """
    STARTUP r1 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 7827620
