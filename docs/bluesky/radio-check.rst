Radio and Check Buttons
-----------------------

.. |radio| image:: ../figures/07piratz_radio.jpg
   :width: 86px
   :height: 66px

.. |checkb| image:: ../figures/07piratz_check.jpg
   :width: 82px
   :height: 59px

Radiobutton |radio| Checkbutton |checkb|

.. sidebar:: States

   There are compound states used in the checkbox, there must be at least 
   two states whenever there is a selected state for pressed, active and
   disabled.

Both radio- and check buttons are created in a similar fashion, in that 
multiple images were created for the various states. All images need to be 
the same size and if they are about the same distance between the lines of
widgets that 
would not be such a bad idea.

Whenever a radio or check button is disabled or enabled its selection must
be maintained.  

Radio Buttons
^^^^^^^^^^^^^^

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 07pirate_radio.py

   .. literalinclude:: ../examples/07pirate_radio.py
      :start-after: style = Style()

Check Buttons
^^^^^^^^^^^^^^

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 07pirate_check.py

   .. literalinclude:: ../examples/07pirate_check.py
      :start-after: style = Style()
