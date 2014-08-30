
.. _fvmbook_chap20_rotate:

Advection equation for solid body rotation
------------------------------------------

Edge velocities are stored in aux array (see setaux.f) with
velocity specified by differencing the streamfunction defined in 
psi.f.  The velocities are :math:`u = \psi_y, v = -\psi_x`.
    
Example [book/chap20/rotate] to accompany the book 
`Finite Volume Methods for Hyperbolic Problems
<http://www.clawpack.org/book.html>`_
by R. J. LeVeque.

Converted to Clawpack 5.0 form in 2013.
        

