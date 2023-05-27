import dis
import types
import inspect


class VirtualMachineError(Exception):
    pass

class VirtualMachine:
    """Stores the call stack, the exception state, and return
    values while they are based between frames.
    """
    def __init__(self) -> None:
        self.frames = [] # call stack
        self.frame = None # current frame
        self.return_value = None
        self.last_exception = None
    
    def run_code(self,code, global_names=None, local_names=None):
        """Entry point to execute code using the virtual machine.
        Args:
            code (_type_): _description_
            global_names (_type_, optional): _description_. Defaults to None.
            local_names (_type_, optional): _description_. Defaults to None.
        """
        frame = self.make_frame(code, global_names=global_names, local_names=local_names)
        self.run_frame(frame)

    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        """Allows us manipulate frames

        Args:
            code (_type_): _description_
            callargs (dict, optional): _description_. Defaults to {}.
            global_names (_type_, optional): _description_. Defaults to None.
            local_names (_type_, optional): _description_. Defaults to None.
        """
        if global_names is not None and local_names is not None:
            local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = {}
        else:
            global_names = local_names = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
                '__package__': None,
            }
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame
    
    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None


    ###
    # Data stack manipulation methods
    def top(self):
        return self.frame.stack[-1]
    
    def pop(self):
        return self.frame.stack.pop()

    def push(self, *vals):
        self.frame.stack.extend(vals)

    def popn(self, n):
        """A list of n values is returned, the deepest value first"""
        if n:
            ret = self.frame.stack[-n:]
            self.frame.stack[-n:] = []
            return ret
        else:
            return []

    def parse_byte_and_args(self):
        f = self.frame
        opoffset = f.last_instruction
        byte_code = f.code_obj.co_code[opoffset]
        f.last_instruction +=1
        byte_name = dis.opname[byte_code]
        if byte_code >= dis.HAVE_ARGUMENT:
            # index into bytecode
            arg = f.code_obj.co_code[f.last_instruction:f.last_instruction+2]
            f.last_instruction +=2 # advance instruction pointer
            arg_val = arg[0] + (arg[1] * 256)
            if byte_code in dis.hasconst: # look up a constant
                arg = f.code_obj.co_consts[arg_val]
            elif byte_code in dis.hasname: # look up a name
                arg = f.code_obj.co_names[arg_val]
            elif byte_code in dis.haslocal: # look up a local name
                arg = f.code_obj.co_varnames[arg_val]
            elif byte_code in dis.hasjrel: # calculate a relative jump
                arg = f.last_instruction + arg_val
            else:
                arg = arg_val
            argument = [arg]
        else:
            argument = []
        return byte_name, argument

    def dispatch(self, byte_name, argument):
        pass

    def run_frame(self, frame):
        pass


class Frame:
    """Collection of attributes with no methods.
    Attrs: the code object created by the compiler, the local, global and builtin namespaecs
    a ref to the previous frame, a data stack, a block stack, and the last instruction executed
    """
    def __init__(self, code_obj, global_names, local_names, prev_frame);
        self.code_obj = code_obj
        self.global_names = global_names
        self.local_names = local_names
        self.prev_frame = prev_frame
        self.stack = []
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtins__']
            if hasattr(self.builtin_names, '__dict__'):
                self.builtin_names = self.builtin_names.__dict__
        self.last_instruction = 0
        self.block_stack = []

class Function:
    """Call a function ie invoking the __call__ method creates
    a new Frame object and runs it. Create a reaslistic func obj, defining the things the interpreter expects.
    """
    __slots__ = [
        'func_code', 'func_name', 'func_defaults', 'func_globals', 'func_locals', 'func_dict', 'func_closure',
        '__name__', '__dict__', '__doc__',
        '_vm', '_func',
    ]
    def __init__(self, name, code, globs, defaults, closure, vm):
        self._vm = vm
        self.func_code = code
        self.func_name = self.__name__ = name or code.co_name
        self.func_defaults = tuple(defaults)
        self.func_globals = globs
        self.func_locals = self._vm.frame.f_locals
        self.__dict__ = {}
        self.func_closure = closure
        self.__doc__ = code.co_consts[0] if code.co_consts else None

        # Sometimes, we need a real python func, this is for that.
        kw = {
            'argdefs': self.func_defaults,
        }
        if closure:
            kw['closure'] = tuple(make_cell(0) for _ in closure)
        self._func = types.FunctionType(code, globs, **kw)

    def __call__(self, *args, **kwargs):
        """When calling a Function, make a new frame and run it."""
        callargs = inspect.getcallargs(self._func, *args, **kwargs)
        # User callargs to provide a mapping of arguments: values to pass into the new
        # frame
        frame = self._vm.make_frame(
            self.func_code, callargs, self.func_globals, {}
        )
        return self._vm.run_frame(frame)

def make_cell(value):
    """Create a real python closure and grab a cell.

    Args:
        value (_type_): _description_
    """
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]



class Block:
    pass