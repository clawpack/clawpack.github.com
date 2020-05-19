

def test():
    import sys
    if sys.version_info[0] >= 3:
        if sys.version_info[1] >= 4:
            from importlib import reload
        else:
            from imp import reload
    reload(sys)



Traceback (most recent call last):
  File "test1.py", line 12, in <module>
    test()
  File "test1.py", line 10, in test
    reload(sys)
