# Import all model template files
from .gfs import *
from .hrrr import *
from .navgem import *
from .nbm import *
from .nexrad import *
from .rap import *
from .rrfs import *

try:
    # An experimental special case for locally stored files.
    from .local import *
except:
    pass
try:
    # Brian's personal local special case.
    from .local_B import *
except:
    pass
