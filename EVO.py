class EVO:
    def __init__(self, commands, through=None, escape=None, inverse=False, double=0) -> None:
        self.commands = commands
        self.through = through
        self.escape = escape
        self.inverse = inverse
        self.double = double

        # self.history = {}


    def alg(self, number, end, last=0):
        # n_truth = truth
        # n_truth += 1 if self.through and number in self.through else 0
        # Этот код отвечал за "обязательные" числа
        if number == end:
            return 1
        if not self.inverse and number > end or self.inverse and number < end:  # Число уже ушло за нужное
            if not self.double or\
                    self.double and last == self.double or\
                    last != self.double and eval(str(number) + self.commands[self.double - 1]) != end:  # Последняя возможность получить нужное число
                return 0
        if type(self.escape) is set and len(set(str(number)) & self.escape) or\
                type(self.escape) is tuple and number in self.escape:  # Запрещённая цифра в числе или число среди запрещённых
            return 0
        # if number == end:
        #     return int(type(self.through) is tuple and n_truth == len(self.through) or\
        #             type(self.through) is set and n_truth > 0 or\
        #                 self.through is None)
        # Прошёл ли код через все "обязательные" числа
        variants = 0
        for command in self.commands:
            if not (self.double and last == self.double == self.commands.index(command) + 1) and\
                    not (self.inverse and " / " in command and eval(str(number) + command.replace("/", "%"))):
                n_number = int(eval(str(number) + command))
                alged = self.alg(n_number, end, self.commands.index(command) + 1)
                variants += alged
                # if alged != 0:
                #     self.history[number].append((n_number, alged))
                # Добавление в историю
        return variants
    
    
    def evo(self, start, end):
        if self.through:
            all = (start, ) + self.through + (end, )
            result = 1
            for i in range(len(all) - 1):
                result *= self.alg(all[i], all[i + 1])

            return result
        return self.alg(start, end)
    
        
    # def get_history(self):
    #     dct = {}
    #     for key in sorted(self.history.keys()):
    #         if self.history[key]:
    #             dct[key] = self.history[key]
    #     return str(dct)