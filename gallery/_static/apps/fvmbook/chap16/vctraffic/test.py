

def test():
    import sys
    if (sys.version_info[0] >= 3) and (sys.version_info[1] >= 4):
        from importlib import reload
    else:
        from imp import reload
    reload(sys)

test()
