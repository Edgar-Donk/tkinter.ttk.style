Piratz Combobox
---------------

.. image:: ../figures/07piratz_combobox.jpg
   :width: 167px
   :height: 142px
   :align: center

.. sidebar:: Combobox

   Be careful about which theme to use, when testing we cannot use clam for 
   some reason, remember this was used to position the down arrow for our 
   green and orange themes. When loaded into the final piratz theme it works 
   with clam.

Take combobox next, it is best not to alter this too much - since we 
need to incorporate a drop down list - so let's use the images from ubuntu. 
Remember ubuntu uses png, which is easier to manipulate than gif within PIL. 
We can see that ubuntu uses theme create without layout. 

.. topic:: Changing Colours of a Widget

   All the ubuntu images have a brown-beige look which we can change to 
   aquamarine based colours using 07list_colours.py and 07shift_colours.py, 
   this then matches our label widget. If we list the colours sorted by the 
   sum of the colour components, we can detect the different shades, then 
   we apply the darkest shade of brown-beige to the shift colours as our main 
   source colour. The shift script sorts out the shades of brown-beige and 
   substitutes shades of aquamarine. It is best to skip over arrows by creating 
   a mask by commenting out parts of the substitution process. Afterwards the 
   arrows are removed by painting over using the appropriate image background 
   colour with an image editor. The arrow is then replaced by an anchor. 
   
   There are various options available to change the colours, the system chosen is not the most rigorous, but seems to produce 
   surprisingly good results. To create a finished colour 3 colours are required, 
   the source pixel, a notional main source colour (called pivot in the program) 
   to which each pixel is compared and a target colour from which the required 
   colour is produced by adjusting the target colour. If a widget appears to use 
   a different hue we can substitute a new pivot and target colours - a commented 
   example is included. The 3 colour channels are linearly adjusted based on 
   the two constant points, if the source was white then the sum of the channels 
   would be 765 and the individual channels of the final colour would be 255, 
   the other point we know is that if the source is the same as our pivot colour, 
   then the channel values of the final colour would be the same as our target 
   colour.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 07pirate_combobox.py

   .. literalinclude:: ../examples/07pirate_combobox.py
      :start-after: style = Style()
