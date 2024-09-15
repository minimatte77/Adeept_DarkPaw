#!/usr/bin/env/python
# File name   : test.py
# Production  : EWP
# Website     : www.ewp.it
# Author      : Matteo
# Date        : 2024/02/04

import time
import os

import SpiderG
import switch

FLB_init_pwm = SpiderG.FLB_init_pwm
FLM_init_pwm = SpiderG.FLM_init_pwm
FLE_init_pwm = SpiderG.FLE_init_pwm

FRB_init_pwm = SpiderG.FRB_init_pwm
FRM_init_pwm = SpiderG.FRM_init_pwm
FRE_init_pwm = SpiderG.FRE_init_pwm

HLB_init_pwm = SpiderG.HLB_init_pwm
HLM_init_pwm = SpiderG.HLM_init_pwm
HLE_init_pwm = SpiderG.HLE_init_pwm

HRB_init_pwm = SpiderG.HRB_init_pwm
HRM_init_pwm = SpiderG.HRM_init_pwm
HRE_init_pwm = SpiderG.HRE_init_pwm


def servoPosInit():
    print('move_init')
    SpiderG.move_init()
    time.sleep(2)
    print('move_leg1')
    SpiderG.move_leg1()


#servoPosInit()


if __name__ == '__main__':
    switch.switchSetup()
    switch.set_all_switch_off()
    SpiderG.servoStop()

    while  1:
        try:                  #Start server,waiting for client
            servoPosInit()
            break
        except Exception as e:
            print(e)
'''
    try:
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        print(e)
        # move.destroy()
'''