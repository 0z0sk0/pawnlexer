import sys
import inspect

from .directives import *
from .functions import *
from .node import *
from .operators import *
from .bit_operators import *
from .types import *


lex_rules = {}
all_tokens = []

start = 'program'

current_package = __package__
modules = []
for name, obj in list(sys.modules.items()):
    if name.startswith(current_package + '.') and inspect.ismodule(obj):
        if name == __name__ or not name.startswith(current_package + '.'):
            continue
        modules.append(obj)

for module in modules:
    if hasattr(module, 'tokens'):
        module_tokens = module.tokens
        if isinstance(module_tokens, str):
            all_tokens.append(module_tokens)
        else:
            all_tokens.extend(list(module_tokens))

    module_dict = vars(module)
    for name, obj in module_dict.items():
        if name.startswith('t_') and callable(obj):
            lex_rules[name] = obj

# Remove duplicate tokens
seen = set()
tokens = tuple(t for t in all_tokens if not (t in seen or seen.add(t)))

__all__ = ['lex_rules', 'tokens', 'start']