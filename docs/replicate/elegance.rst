Elegance Button
===============

.. |elo| image:: ../images/elegance_button-default.gif
   :width: 60
   :height: 34

.. |elc| image:: ../figures/09eleg_button.png
   :width: 60
   :height: 34

.. table:: Elegance Button

   =============== ===============  
   Original          Created   
   |elo|            |elc|         
   =============== ===============

The elegance button's gradient looks quite challenging. The frame looks 
simple, but it actually changes colour. One approach would be to create a single 
gradient and darken the lower half, or we could make two gradients. Any 
antialiasing effects are not showing strongly.

The button appears to have a 2D gradient, in that the rows and columns 
change. Checking with 09find_line_color.py, the rows change on average from
(230,231,230) to (200,200,200) upto the mid point, whilst the upper half 
column changed from (227,227,227) to (207,207,207) and back to (226,226,226).
In the lower half the rows were pretty static, changing from (184,184,184) to
(180,180,179), whilst the columns changed from (199,199,198) to (168,168,168)
and back to (196,196,196). 

The gradient can be based on 08radial_gradient.py where points are coloured
according to the distance of the point from the centre. An alternative 2D
gradient can be created by using the ellipse.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09elegance_button.py

   .. literalinclude:: ../examples/09elegance_button.py
