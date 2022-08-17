Lime Button
-----------

.. figure:: ../images/lime/button-sa.png
   :width: 27
   :height: 27

   Button with Double Border
   
   Standard image made using the common class.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10button.py

   .. literalinclude:: ../examples/10button.py


.. |bn| image:: ../images/lime/button-n.png
   :width: 25
   :height: 25

.. |bp| image:: ../images/lime/button-p.png
   :width: 25
   :height: 25

.. |ba| image:: ../images/lime/button-a.png
   :width: 25
   :height: 25

.. |bd| image:: ../images/lime/button-d.png
   :width: 25
   :height: 25

.. table:: Lime Button (alternative)

   ================= ================= ================= =================
   Normal            Pressed           Active             Disabled
   |bn|              |bp|              |ba|               |bd|
   ================= ================= ================= =================

There are quite a few button variations to pick from, to start with use the 
standard widget from the common code. 

If we now look at the alternative button the border has a gradient that changes 
from near white at the upper part. Inside the widget a second gradient runs
from top to the bottom border. This is based on ideas from the keramik button.

The border was initially quite dark and surrounded a fairly light gradient,
created by an import from ``tools``. A second image was created with just a 
slightly darker gradient. The two images were coalesced using PIL ImageChops
lighter. The goal was to replace the border with a gradient, but
retain the internal gradient. Afterwards resize then create the extra states. 
Set the border dimensions such that when the button is expanded vertically 
only a narrow band is utilised, horizontally make allowance for the corners.

In order to enable the pressed state it had to be placed just after the 
normal state, with the active state next. The appearance had horizontal 
stripes due to the gradient, which was cured by an aggressive use of the 
border dimensions just as we had done in the pirate theme. The text 
foreground was changed to dark red to give contrast to the background.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10buttonalternative.py

   .. literalinclude:: ../examples/10buttonalternative.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_button.py

   .. literalinclude:: ../examples/10lime_button.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_button_alt.py

   .. literalinclude:: ../examples/10lime_button_alt.py

Menubutton
^^^^^^^^^^

The choice seems to be between a menubutton with a down arrow, as in the
combobox, a rectangle as used by some or two arrows as in elegance. Once 
again the blue theme has no special image.