"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from scipy import special as sp

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param
        

        

    
    def work(self, input_items, output_items):
        def qfunc(x):
            return 0.5-0.5*sp.erf(x/np.sqrt(2))
        
        def invqfunc(x):
        
            inp = np.arange(0, 1000)/1000
            min=1
        
            for i in range(0,len(inp)):
            
                if abs(qfunc(inp[i])-x)< min:
                    min = abs(qfunc(inp[i])-x)
                    y = inp[i]
                    
                    
            return y
        """example: multiply with constant"""
        
        output_items[0][:] = invqfunc(0.1)
        return len(output_items[0])
