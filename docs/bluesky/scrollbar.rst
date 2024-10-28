Piratz Scrollbar
----------------

.. image:: ../figures/07piratz_scrollbar_grip.jpg
   :width: 168px
   :height: 215px
   :align: center

Looking at the scrollbars next, they have components which will change with 
orientation, so together with changes of state there are quite a few images used. 
07pirate_scrollbar.py is the original script. I like the images from ubuntu 
so we can change their colours to aquamarine and subsititute the coconut tree 
from pirate_label for the arrows (steppers). The thumb image is a coconut, so 
for the first attempt there was no grip. 

The trough has been copied from elegance, with a colour change, this shows 
how the trough can be created from an image. Ubuntu used the trough from the 
parent theme and changed its colour with a configure command - obviously both 
approaches are equally valid, but the image can give more flexibility. 

Since there are changes to the arrangement compared to the parent theme we will 
need a layout, which will need to be copied and changed as appropriate for 
the other orientation. It is important that the thumb component has the element 
"expand" set to True or 1, otherwise the thumb cannot be moved using the mouse 
- this in turn means that the thumb will no longer remain circular but becomes 
oval. The original script is available.

.. image:: ../figures/07piratz_scrollbar.jpg
   :width: 162px
   :height: 216px
   :align: center

Just as it was necessary to set the border limits in pirate_label so thumb needs 
to have its border set (try experimenting with a border of 1). An oval coconut 
is not really what we want, we can keep it circular if we change the layout 
slightly - borrowed from the plastik theme - utilise a thumb and grip, the 
grip is our coconut and the thumb is a beach, as in the first script the thumb 
expands and has differing states, but the grip only changes between vertical 
and horizontal orientations. If you want you can uncomment out the third arrow 
in the layout in this script. 

The flexibility of the tkinter theme is shown to its full limits - quite 
impressive.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 07pirate_scrollbar_grip.py

   .. literalinclude:: ../examples/07pirate_scrollbar_grip.py
      :start-after: style = Style()
