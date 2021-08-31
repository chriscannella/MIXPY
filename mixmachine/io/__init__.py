from xitwords import XitWord
class MixIODevice():
    def __init__(self, host, block_size=1, num_blocks = 100):
        self.busy = False
        self.host = host
        self.block_size=block_size
        self.num_blocks = num_blocks
        self.memory = [XitWord(0, word_length=5, base=self.host.base) for i in range(0, self.block_size*self.num_blocks)]
        self.current_location = 0
        self.transfer_location = 0
        self.current_offset = 0
        self.current_task = None

    def read_to_host(self):
        if self.current_offset < self.block_size:
            if self.transfer_location + self.current_offset < 4000 and self.current_location + self.current_offset < len(self.memory):
                self.host[self.transfer_location + self.current_offset].read(self.memory[self.current_location + self.current_offset])
            self.current_offset += 1
        else:
            self.current_offset = 0
            self.current_location += self.block_size
            self.current_task = None
            self.busy = False

    def write_from_host(self):
        if self.current_offset < self.block_size:
            if self.transfer_location + self.current_offset < 4000 and self.current_location + self.current_offset < len(self.memory):
                self.memory[self.current_location + self.current_offset].read(self.host[self.transfer_location + self.current_offset])
            self.current_offset += 1
        else:
            self.current_offset = 0
            self.current_location += self.block_size
            self.current_task = None
            self.busy = False

    def instruct(self, instruction):
        return None

    def operate(self):
        if self.busy and self.current_task is not None:
            self.current_task()