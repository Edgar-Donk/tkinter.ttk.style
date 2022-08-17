Clearlooks Button
=================

.. |clo| image:: ../images/cl_button-n.gif
   :width: 28
   :height: 28

.. |clc| image:: ../figures/09clbut.png
   :width: 28
   :height: 28

.. table:: Clearlooks Button

   =============== ===============  
   Original          Created   
   |clo|            |clc|         
   =============== ===============

.. sidebar:: Check Gradients

   Use 09find_line_colour.py to see whether gradients exist in the rows and 
   columns in the gradient area. Load the image and adjust the gradient area.

The clearlooks button looks straightforward until we notice  the pixel distribution in the
gradient area. First check whether there is a simple vertical gradient, 
then see whether there is a horizontal gradient. The checks show that the 
colour gradually changes vertically (rows), whereas horizontally it is steady.

Since the corner pixels and the gradient do not interfere, we can create a
round corner frame, reduce in size then insert the gradent and highlights. 
The frame is a simple one with a gap of 4. The frame colour (148,125,123) has
a shadow (231,219,214) along its lower and righthand sides. Let's choose
(148,125,123) as a first estimate. We can choose the corner pixel colour 
#EFEBE7 as our background. The result looked good, but the frame (155,133,131)
needed darkening, start with (141,117,115) instead. 

.. topic:: Calculating the Frame Colour

   Use the colour component differences between starting and resulting frame
   then subtract these differences from from the target frame colour.
   
   =========== ============== ==============
   Target      (148,125,123)
   Start       (148,125,123)  (141,117,115)
   Result      (155,133,131)  (148,125,123)
   Differences (  7,  8,  8)
   =========== ============== ==============

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09cl_but.py

   .. literalinclude:: ../examples/09cl_but.py
