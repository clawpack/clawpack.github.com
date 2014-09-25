import os

from clawpack.clawutil.runclaw import runclaw

runclaw('xamr',outdir='_output',nohup=True, nice=10)

