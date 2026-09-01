import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  # Hereda de sync_block
    """Bloque personalizado de Python para Comunicaciones II"""

    def __init__(self, factor=1.0):  # Parametro configurable desde GRC
        """Inicializacion del bloque"""
        gr.sync_block.__init__(
            self,
            name='Mi_Bloque_Python',   # Nombre que aparecera en el bloque
            in_sig=[np.float32],       # Tipo de senal de entrada (Float 32)
            out_sig=[np.float32]      # Tipo de senal de salida (Float 32)
        )
        self.factor = factor

    def work(self, input_items, output_items):
        """Procesamiento de muestras"""
        in0 = input_items[0]
        out = output_items[0]
        
        # Operacion sobre las muestras de entrada
        out[:] = in0 * self.factor
        
        return len(output_items[0])
