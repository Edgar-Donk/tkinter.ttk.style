Lime Checkbox
-------------

.. |cnu| image:: ../images/lime/check-nu.png
   :width: 19
   :height: 18

.. |cnc| image:: ../images/lime//check-nc.png
   :width: 19
   :height: 18

.. |chu| image:: ../images/lime//check-hu.png
   :width: 19
   :height: 18

.. |chc| image:: ../images/lime//check-hc.png
   :width: 19
   :height: 18

.. |cdu| image:: ../images/lime//check-du.png
   :width: 19
   :height: 18

.. |cdc| image:: ../images/lime//check-dc.png
   :width: 19
   :height: 18

.. table:: Lime Checkbox

   ========= ========= ========= ========= ========= =========
   Normal    Normal    Active    Active    Disabled  Disabled
   unchecked checked   unchecked checked   unchecked checked
   |cnu|     |cnc|      |chu|    |chc|      |cdu|     |cdc|
   ========= ========= ========= ========= ========= =========

Looking at the blue widgets the checkbox is similar to the scrollbar thumb.
The check buttons have images showing highlighted(h) and normal(n) combined 
with checked(c) and unchecked(u) tags, corresponding to active and selected 
states. In the selected state there are compound states with active and 
disabled.

The gradient will be as our thumb, but the surrounding frame is lighter. At
normal size the difference in the upper and left sides with the lower and 
right sides is not really discernable. The check mark is a simple cross with 
double lines drawn at 45 degrees.

When testing we can re-use 07pirate_check.py as 10lime_check.py. Be careful
when setting up the states. The active states come immediately after the 
normal state and active selected precedes plain active.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10check.py

   .. literalinclude:: ../examples/10check.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_check.py

   .. literalinclude:: ../examples/10lime_check.py
