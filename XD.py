# launcher.py
import platform

arch = platform.architecture()[0]

if arch == '32bit':
    import DREP1 as DREP
else:
    import DREP as DREP