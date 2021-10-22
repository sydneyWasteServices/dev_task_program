from enum import Enum

# Rev types are constant

class Rev_types(Enum):
    TOTAL = 'total'
    GENERAL_WASTE = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG']
    CARDBOARD = ['APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP']
    COMINGLED = ['CBK', 'RLC', 'RLG', 'DOY']
    SUBCONTRACTED = ['SUB', 'JJT', 'ALLMED', 'BIN', 'CKG', 'CLN', 'GRACE', 'JJR', 'OWE', 'REM', 'REP', 'REQ', 'RRNW', 'RRR', 'SHR', 'SPD', 'SUE', 'URM', 'VEO', 'VEOACT', 'VTG', 'AUSSKIP','GRIMA']
    UOS = ['NEPCB', 'UOSCB', 'UOSCO', 'UOSGW', 'CMDCB', 'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW']


# JJR Grima GRACE