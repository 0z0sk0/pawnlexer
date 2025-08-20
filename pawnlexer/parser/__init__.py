import sys
import inspect

from .program import *
from .tags import *
from .expressions import *
from .node import *
from .variable import *
from .functions import *


parse_rules = {}

start = 'program'

current_package = __package__
modules = []
for name, obj in list(sys.modules.items()):
    if name.startswith(current_package + '.') and inspect.ismodule(obj):
        if name == __name__ or not name.startswith(current_package + '.'):
            continue
        modules.append(obj)

for module in modules:
    module_dict = vars(module)
    for name, obj in module_dict.items():
        if name.startswith('p_') and callable(obj):
            parse_rules[name] = obj

__all__ = ['parse_rules', 'start']