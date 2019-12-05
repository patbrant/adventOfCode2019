from enum import IntEnum

class Opcode(IntEnum):
    ADDITION = 1
    MULTIPLICATION = 2
    SAVE_AT_ADDRESS = 3
    GET_FROM_ADDRESS = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99