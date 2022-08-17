Frame
=====

The first example is probably best run as a standalone style for frame. The 
idea is copied from a website `canvas image <https://datatofish.com/how-to-create-a-gui-in-python/>`_
that demonstrated how to use the tkinter canvas to contain the background 
image and some other widgets together with a matplotlib interface. This works 
but the geometry management is limited to the canvas system. If we use frame 
as our parent widget all the normal geometry managers - grid, pack and place 
- can be used. The only minor problem is that it works best with a full view 
of the background image. Use the example 07frame_background_image.py 

Frame with Background
---------------------

.. image:: ../figures/07frame_background.jpg
   :width: 592px
   :height: 359px
   :align: center

.. sidebar:: Frame

   Look in the upper left hand corner for label and entry

to see what I mean, use a jpg image of your choice as backdrop, typically a 
panoramic view. Since these may be downloaded from many digital cameras and 
are usually half the size of a png or gif of equivalent size.

.. container:: toggle

   .. container:: header 


       *Show/Hide Code* 07frame_background_image.py

   .. literalinclude:: ../examples/07frame_background_image.py
