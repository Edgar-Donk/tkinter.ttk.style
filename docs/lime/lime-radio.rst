Lime Radiobuttons
-----------------

.. |rn| image:: ../images/lime/radio-n.png
   :width: 25
   :height: 25

.. |rs| image:: ../images/lime/radio-s.png
   :width: 25
   :height: 25

.. |rd| image:: ../images/lime/radio-d.png
   :width: 25
   :height: 25

.. |rds| image:: ../images/lime/radio-ds.png
   :width: 25
   :height: 25

.. table:: Lime Radiobox

   ================= ================= ================= =================
   Normal            Selected           Disabled         Disabled Selected
   |rn|              |rs|              |rd|               |rds|
   ================= ================= ================= =================

Both radiobuttons have to be created, since whether we use a circular or
diamond shape we have nothing yet in our lime images. The best looking ones
were from aquativo, which meant decoding to view them, the unselected button 
is grey with a highlight in the lower half, the selected button is colourful 
with a dark centre.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10radio.py

   .. literalinclude:: ../examples/10radio.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_radio.py

   .. literalinclude:: ../examples/10lime_radio.py
