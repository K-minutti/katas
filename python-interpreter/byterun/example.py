class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def STORE_NAME(self,  name):
        self.environment[name] = self.stack.pop()

    def LOAD_NAME(self, name):
        self.stack.append(self.environment[name])

    def LOAD_VALUE(self, val):
        self.stack.append(val)

    def ADD_TWO_VALUES(self):
        a = self.stack.pop()
        b = self.stack.pop()
        res = a + b
        self.stack.append(res)
    
    def PRINT_ANSWER(self):
        ans = self.stack.pop()
        print(ans)

    def parse_arg(self, instruction, arg, code_to_run):
        """ Understand what the argument to each instruction means."""
        nums = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']
        if instruction in nums:
            return code_to_run['numbers'][arg]
        elif instruction in names:
            return code_to_run['names'][arg]

    def run_code(self, container):
        instructions = container.get('instructions')
        for step in instructions:
            instruction, arg = step
            arguement = self.parse_arg(instruction, arg, container)
            bytecode_method = getattr(self, instruction)
            if arguement is None:
                bytecode_method()
            else:
                bytecode_method(arguement)
            # if instruction == 'LOAD_VALUE':
            #     self.LOAD_VALUE(arguement)
            # elif instruction == 'ADD_TWO_VALUES':
            #     self.ADD_TWO_VALUES()
            # elif instruction == 'PRINT_ANSWER':
            #     self.PRINT_ANSWER()
            # elif instruction == 'LOAD_NAME':
            #     self.LOAD_NAME(arguement)
            # elif instruction == 'STORE_NAME':
            #     self.STORE_NAME(arguement)

if __name__ == "__main__":
    code_to_run =  {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [11, 7] }

    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"] }
    interp = Interpreter()
    interp.run_code(code_to_run)