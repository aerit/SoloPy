# Copyright: (c) 2021, 2022, 2023 SOLO motor controllers project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Title: SoloPy
# Author: SOLOMotorControllers
# Date: 2023
# Code version: 3.1.0
# Availability: https://github.com/Solo-FL/SoloPy/tree/main/SoloPy
# This Library is made by SOLOMotorControllers.COM
# please visit:  https://www.SOLOMotorControllers.com/

# In this example we want:
# STEP 1: to print the command mode of SOLO and the error status of the reading operation
# STEP 2: if we read the command mode without error we want to change the command mode of SOLO.

import SoloPy as solo

import time

# instanciate a SOLO object:
# check with SOLO motion terminal that you are able to connect to your device and make sure the port name in the code is the correct one 
mySolo = solo.SoloMotorControllerUart("/dev/ttyACM0", 0, solo.UART_BAUD_RATE.RATE_937500)

# loop actions
while True:
    time.sleep(1)

    # STEP 1
    # commandMode : is the Command Mode reading from SOLO device 
    # error : after the execution of the fuction will have the error status of the execution
    commandMode, error = mySolo.get_command_mode()

    # we print the info:
    print("COMMAND MODE READ: " + str(commandMode) + " ERROR: " + str(error))

    # STEP 2
    # if we have no error we want to change the command mode of SOLO
    # we can compare error with SOLOMotorControllersError enum or int value. Equal code: 
    #    error == SOLOMotorControllers::SOLOMotorControllersError::noErrorDetected
    #    error == 0
    if error == solo.ERROR.NO_ERROR_DETECTED:
        # we check the commandMode readed value.
        # we can compare commandMode with CommandMode enum or int value. Equal code:
        #    commandMode == solo.COMMAND_MODE.ANALOGUE
        #    commandMode == 0

        if commandMode == solo.COMMAND_MODE.ANALOGUE:
            # setIsSuccesfull : set return if the set was succesfull
            # SOLOMotorControllers::CommandMode::digital : is the command mode i want to set to SOLO.
            # error : after the execution of the fuction will have the error status of the execution
            setIsSuccesfull, error = mySolo.set_command_mode(solo.COMMAND_MODE.DIGITAL)

            # we can call the function without check the return:
            # mySolo.set_command_mode(solo.COMMAND_MODE.DIGITAL)

            # we print the info:
            print("COMMAND MODE SET: " + str(commandMode) + " ERROR: " + str(error))
        else:
            # in this situation we want to set analogue as command mode in SOLO
            # we choose the alternative code with less herror and status controlling:
            setIsSuccesfull, error = mySolo.set_command_mode(solo.COMMAND_MODE.ANALOGUE)

            # we can call the function without check the return:
            # mySolo.set_command_mode(solo.COMMAND_MODE.ANALOGUE)

            # we print the info:
            print("COMMAND MODE SET: " + str(commandMode) + " ERROR: " + str(error))
