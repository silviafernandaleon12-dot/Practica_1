import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Diferenciador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.prev = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        for i in range(len(x)):
            y[i] = x[i] - self.prev
            self.prev = float(x[i])

        return len(y)
