Blue Theme - Scrollbar, Button 
==============================

Blue Scrollbar
--------------

.. |sb| image:: ../images/sb-thumb.gif
   :width: 28
   :height: 28

.. |bsb| image:: ../figures/09bluesb.png
   :width: 28
   :height: 28

.. table:: Blue Scrollbar Thumb

   ================= =================
   Original          Created
   |sb|              |bsb|
   ================= =================

Within the blue theme there are several widgets with a gradient. Some images
appear to be alike, so the scrollbar thumb and scrollbar left and right 
arrows have similar rectangular frames. Since the arrows are drawn across 
with an even number of pixels the arrow point is 2 pixels across. The slanted 
lines are made at 45 degrees without any antialiasing. It's surprising what 
you can get away with.

The blue scrollbar thumb can be used as a template. It consists of a simple 
frame, with all four corners made transparent, and a simple vertical gradient. 
There is no antialiasing. Let's go ahead and make this.

When counting the number of times that a line is drawn to make the gradient,
allow for the borders, if the first line has a y-value of 1 and the last 
line of 12 we actually have 12 steps (count inclusively). Since 
``range(steps)`` starts from 0 and ends at the maximum value less 1, it 
requires no adjustment. 

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09bluesb.py

   .. literalinclude:: ../examples/09bluesb.py

Blue Button
------------

.. |blue| image:: ../images/bluebutton-n.gif
   :width: 32
   :height: 32

.. |bl| image:: ../figures/09bluebutton2.png
   :width: 32
   :height: 32

.. table:: Blue Button

   =============== ===============  
   Original          Created   
   |blue|            |bl|         
   =============== ===============

The button frame looks more interesting than the scrollbar thumb. Use the 
medium blue colour as the background, draw a rectangle using the dark blue.
Run a simple gradient then create the corners using points.

Since there is no size change with filter there is no stray colours as in the
original, on the other hand the colour stays true.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09bluebut2.py

   .. literalinclude:: ../examples/09bluebut2.py
