#!/usr/bin/env python
# coding=utf-8

import sys
import os
import logging
import json

logging.basicConfig(level = logging.WARNING,format = '[%(filename)s:%(funcName)s:%(lineno)s]%(message)s')
logger = logging.getLogger("iSearch")


class Configer:
    def __init__(self, configPath):
        with open(configPath) as json_data_file:
            self.__config = json.load(json_data_file)

    def __del__(self):
        self.__config.close()

    def __set_check_func(self):
        self.__checkFunc = {
            "version":versionCheck,
            "titleColor":ColorCheck,
            "textColor":ColorCheck,
        }

    def get_config_option(self, key):
        return self.__config["key"]

    def set_config_option(self, key, value):
        if self.__checkFunc[key](key, value):
            self.__config[key] = value

    def versionCheck(self, key, value):
        if("1.0" == value or "1.1" == value):
            return 1
        else:
            logger.error("version error")
            sys.exit(1)

    def ColorCheck(self,key, value):
        if value in ColorArr:
            return 1
        else:
            logger.error(key + " can't be setted " + value)
            sys.exit(1)




