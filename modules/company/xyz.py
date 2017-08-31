print('[xyz.py]  name=',__name__)
def xyz():
    import sys
    print("[xyz.py] call",sys._getframe().f_code.co_name)

if __name__=='__main__':

    print('[xyz.py]',xyz.__name__)
    xyz()