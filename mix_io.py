from xit_words import XitWord
class MixIODevice():
    def __init__(self, host, block_size=1, num_blocks = 100):
        self.busy = False
        self.ready = False
        self.host = host
        self.block_size=block_size
        self.num_blocks = num_blocks
        self.memory = [XitWord(0, word_length=5, base=self.host.base) for i in range(0, self.block_size*self.num_blocks)]
        self.current_location = 0

    def read_to_host(self, transfer_location):
        for offset in range(0, self.block_size):
            self.host[transfer_location + offset].read(self.memory[self.current_location + offset])
        self.current_location += self.block_size

    def write_from_host(self, transfer_location):
        for offset in range(0, self.block_size):
            self.memory[self.current_location + offset].read(self.host[transfer_location + offset])
        self.current_location += self.block_size

    def instruct(self, instruction):
        return None