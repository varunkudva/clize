# clize - automatically generate command-line interfaces from callables
# Copyright (C) 2013 by Yann Kaiser <kaiser.yann@gmail.com>
# See COPYING for details.

"""procedurally generate command-line interfaces from callables"""

from clize.parser import Parameter
from clize.runner import Clize, SubcommandDispatcher, run
from clize.legacy import clize
from clize.errors import (
    UserError, ArgumentError, MissingRequiredArguments, TooManyArguments,
    UnknownOption, MissingValue, BadArgumentFormat, SetUserErrorContext,
    SetArgumentErrorContext)



