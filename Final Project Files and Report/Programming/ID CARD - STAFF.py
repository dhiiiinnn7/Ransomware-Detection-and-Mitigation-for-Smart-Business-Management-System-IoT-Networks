from time import *
from physical import *

CARD_ID = 1001  # var CARD_ID


def setup():
    global CARD_ID
    CARD_ID = restoreProperty('CardID', CARD_ID)
    setDeviceProperty(getName(), 'CardID', CARD_ID)


def restoreProperty(propertyName, defaultValue):
    value = getDeviceProperty(getName(), propertyName)
    if not (value is "" or value is None):
        if type(defaultValue) is int:
            value = int(value)

        setDeviceProperty(getName(), propertyName, value)
        return value
    return defaultValue


if __name__ == "__main__":
    setup()
    while True:
        sleep(3600)

