Lime Progressbar
----------------

.. |vp| image:: ../images/lime/iprog.png
   :width: 34
   :height: 34

.. |hp| image:: ../images/lime/rprog.png
   :width: 34
   :height: 34

.. table:: Lime Progressbar 

   ================= ================= 
    Horizontal       Vertical       
    rectangles       radial
   |hp|              |vp|              
   ================= ================= 

Let's see if we can reuse two of the thumb images for the trough, then all 
we require are internal parts to form the horizontal and vertical progress 
sliders. The horizontal slider used rectangles and the vertical one used 
points for radial gradients, so a comparison can be made.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10progressbar.py

   .. literalinclude:: ../examples/10progressbar.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10prog_alt.py

   .. literalinclude:: ../examples/10prog_alt.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_prog.py

   .. literalinclude:: ../examples/10lime_prog.py
