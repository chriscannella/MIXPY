class MixIODevice():
    def __init__(self, host):
        self.busy = False
        self.ready = False
        self.host = host
        
    def instruct(self, instruction):
        return None