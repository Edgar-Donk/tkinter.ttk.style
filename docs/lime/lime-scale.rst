Lime Scale
----------

.. |vs| image:: ../figures/10largevscale.png
   :width: 62
   :height: 70

.. |hs| image:: ../figures/10largehscale.png
   :width: 69
   :height: 70

.. table:: Lime Scale 

   ================= ================= 
   Vertical           Horizontal       
   standard           alternative
   |vs|              |hs|              
   ================= ================= 

The vertical scale has been fashioned from the standard code.

The horizontal scale has an alternative trough. The keramik scale trough has 
been used as a template, and the slider has been copied from the blue theme. 
When building the trough ensure that the upper border is overdrawn by the 
gradient. The upper corners were lightened to fit in with the gradient. 

When building the trough, using element_create, ensure that the border reflects the
method of trough expansion. We want the trough to expand horizontally, so a
vertical gradient is required, the trough should be slightly lower than the
upper part of the slider, so a ``'sticky': 'ews'`` is important. Don't forget to make
the border fit the trough image, so that we expand from the centre of the
image ``'height': 10`` - ``'border': [6,0,6,0]``. 

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10scale.py

   .. literalinclude:: ../examples/10scale.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10scale_trough.py

   .. literalinclude:: ../examples/10scale_trough.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10scale_trough_alt.py

   .. literalinclude:: ../examples/10scale_trough_alt.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_scale.py

   .. literalinclude:: ../examples/10lime_scale.py
