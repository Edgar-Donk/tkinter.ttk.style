Lime Scrollbar
--------------

.. figure:: ../figures/10scrollbar.png
   :width: 278
   :height: 26
   :align: center

   Horizontal Scrollbar

The scrollbar consists of four parts, and each can have more than one state,
so quite a few images.

Scrollbar Thumb
^^^^^^^^^^^^^^^^

.. |hn| image:: ../images/lime/slider-hn.png
   :width: 25
   :height: 21

.. |htp| image:: ../images/lime/slider-hp.png
   :width: 25
   :height: 21

.. |ha| image:: ../images/lime/slider-ha.png
   :width: 25
   :height: 21

.. |hd| image:: ../images/lime/slider-hd.png
   :width: 25
   :height: 21

.. table:: Lime Horizontal Scrollbar Thumb / Slider

   ================= ================= ================= =================
   Normal            Pressed           Active             Disabled
   |hn|              |htp|              |ha|               |hd|
   ================= ================= ================= =================

As seen in the Blue theme the scrollbar thumb/slider can be used as a common
image for several other widgets. This aids us in ensuring that the various
widgets have a recognisable theme look.

Even though the blue theme seems to have one of the more interesting thumbs, 
we may still be able to use some of the properties of the Ubuntu comboarrow, 
where the rounded corners look distinctly better. Also before applying a 
gradient let's see if we can add shadows and highlights with the light 
falling from the upper left to lower right.

.. topic:: Initial Method of Working

   #. Make the scrollbar thumb/slider file to create an image.
   #. Use the thumb image and add the arrow.
   #. Using the right arrow image make the left arrow.
   #. Copy the pirate scrollbar file 07pirate_scrollbar.py and use as 
      10lime_scrollbar.py. Comment out all the files and states not yet
      present, such as the vertical scrollbars and troughs.
   #. Be particularly critical of the shape and colouring. Now is the time
      to adjust and prove that the template looks good.
   #. Start creating the vertical scrollbar and then the other states.

* Select File Size
   To assist centering make the file with an odd number of pixels . It is 
   useful to see the results of the gradient and corners being created, so save 
   the large image, which can be overwritten later. 

* Construct the Border(s)
   There was no need to explicitly draw the outside rectangle, our outer borders 
   have been created by the background colour the central area being made into a 
   gradient. 

* Internal Fill/Gradient
   Initially when making the gradient use its start and end colours 
   as the internal corner fill. The paler corner fill colours may need a slight 
   adjustment since the eye is more sensitive to the contrast. Later on a 
   function was created that made this adjustment within a standard widget.

* Highlights and Shadows
   Now for the highlights and shadows, our gradient should give the impression 
   that the centre is raised therefore create a highlight on the upper and left 
   sides. The hightlights did not work too well, even when made before
   resizing.

* Resize
   Resize - normally with a Lanczos resampling filter.

* Complete the Corners
   Make the corners transparent. 

Now that is finished, we'd better see that it works before using it. If 
we need to reduce it in size then we'll have to rethink the corner sizes.

.. sidebar:: Construction Class

   There should be quite a few similar looking widgets, so start making a
   construction class. The principles are best explained through 
   `Sammy the Shark tutorial <https://cuny.manifoldapp.org/read/59ff9b35-d1a7-4a79-9bde-4e8bf12c5108/section/2b30f08f-b316-4087-879a-81785709dcb6>`_

The final construct had four states, starting from the normal theme turn it
upside down and we have the pressed state, lighten it and we have the active
state finally turn it into greyscale and we have the disabled state. The 
vertical thumb was made by turning the horizontal thumb 90° to create the
vertical normal state, then repeating the above actions to create the other 
three vertical states.

Scrollbar Trough and Arrows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |ahn| image:: ../images/lime/arrowright-n.png
   :width: 25
   :height: 21

.. |ahp| image:: ../images/lime/arrowright-p.png
   :width: 25
   :height: 21

.. |aha| image:: ../images/lime/arrowright-a.png
   :width: 25
   :height: 21

.. |ahd| image:: ../images/lime/arrowright-d.png
   :width: 25
   :height: 21

.. table:: Lime Right Arrow

   ================= ================= ================= =================
   Normal            Pressed           Active             Disabled
   |ahn|              |ahp|              |aha|               |ahd|
   ================= ================= ================= =================

The blue trough has no separate image, therefore it is being generated from 
the parent theme. Let's see if the result is acceptable. 

Arrows share the same background image which is the thumb image.

.. topic:: Arrow Transposition and Rotate

   When making the transposition, remember that it is FLIP_LEFT_RIGHT, not
   ROTATE_180, to keep the arrow and gradient running in the same direction.
   
   As the image is rectangular use the transpose method, save the image then 
   reopen it if needing to work with it further - ``rotate()`` should only 
   be used on square images. 

Let's see if the alternative arrow can be used. Since the background is 
green be careful about the contrast with the 3 green arrow colours.

.. sidebar:: Widget Sizes

   Some GUI produce pictures with widgets about the same size as the widget
   whereas others and starting the code from the OS will show widgets twice
   their pixel size.

The first result is not too bad, the arrow and thumb have a good shape, the
corners look nicely round but the thumb is about 50 as opposed to 30 pixels.
The background gradient is a bit too sickly and was changed. The vertical
size in a down arrow needs to match the combobox size, and as the arrow is
longer than broad the border width could be reduced, the arrows were 
shoehorned into the background image. 

Because the expected light source comes from the upper left corner the 
horizontal gradient had to be reversed, leaving the arrow colours as is. 
Ensure that the thumb gradient orientation allows it to expand without odd 
looking results - the arrows do not have a size change.

Once these three parts of the scrollbar have been finalised transpose each 
image to make the vertical scrollbars. 

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10scrollbarthumb.py

   .. literalinclude:: ../examples/10scrollbarthumb.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10scrollbararrow.py

   .. literalinclude:: ../examples/10scrollbararrow.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_scrollbar.py

   .. literalinclude:: ../examples/10lime_scrollbar.py
