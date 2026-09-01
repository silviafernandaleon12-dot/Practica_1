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
        self.last_sample = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y0 = output_items[0]
        
        N = len(x)
        if N > 0:
            x_prev = np.empty_like(x)
            x_prev[0] = self.last_sample
            if N > 1:
                x_prev[1:] = x[:-1]
            
            y0[:] = x - x_prev
            self.last_sample = x[-1]
            
        return len(x)
