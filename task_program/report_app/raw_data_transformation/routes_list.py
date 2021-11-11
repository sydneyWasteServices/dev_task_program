from enum import Enum


class By_Revenue_type(Enum):
    TOTAL = 'TOTAL'
    TOTAL_EXCL_SUBCON = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2', 'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI',
                         'RLJ', 'RLK', 'SWG', 'APR', 'FLP', 'HYG', 'RED', 'RL5', 'RL6', 'RL8', 'RLP', 'RLR', 'SWP', 'HOOKCB', 'CBK', 'RLC', 'RLG', 'DOY']
                         
    GENERAL_WASTE = ['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2',
                     'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG']

    CARDBOARD = ['APR', 'FLP', 'HYG', 'RED', 'RL5',
                 'RL6', 'RL8', 'RLP', 'RLR', 'SWP', 'HOOKCB']

    COMINGLE = ['CBK', 'RLC', 'RLG', 'DOY']

    SUBCONTRACTED = ['SUB', 'JJT', 'ALLMED', 'BIN', 'CKG', 'CLN', 'GRACE', 'JJR', 'OWE', 'REM', 'REP',
                     'REQ', 'RRNW', 'RRR', 'SHR', 'SPD', 'SUE', 'URM', 'VEO', 'VEOACT', 'VTG', 'AUSSKIP', 'GRIMA']

    UOS = ['UOSCB', 'UOSCO', 'UOSGW', 'CMDCB',
           'CMDGW', 'CUMCB', 'CUMGW', 'NEPGW', 'NEPCB']


    AGG_GENERAL_WASTE =['HOOK1', 'BR1', 'BR2', 'BR3', 'FL2', 'FLG', 'RL1', 'RL2',
                     'RL4', 'RL7', 'RL9', 'RLD', 'RLE', 'RLH', 'RLI', 'RLJ', 'RLK', 'SWG', 'UOSGW', 'CMDGW', 'CUMGW', 'NEPGW']
# Subcontractor FLP  , RLR merged with RED
    AGG_CARDBOARD = ['APR', 'HYG', 'RED', 'RL5',
                 'RL6', 'RL8', 'RLP', 'RLR', 'SWP', 'HOOKCB','UOSCB','CMDCB','CUMCB','NEPCB']

    AGG_COMINGLE = ['CBK', 'RLC', 'RLG', 'DOY', 'UOSCO']