==============
Style Commands
==============

To manipulate the appearance of a widget - changing its style - we use the 
class Style() and one or more of its commands. Using common style
changes on several widgets we can produce a theme.

The table 01style_commands.csv has a summary of all the Style() commands, 

Table 01style_commands.csv
--------------------------

.. raw:: html

   <details>
   <summary><a>Show/Hide <b> Table </b> 01style_commands.csv </a></summary>

.. csv-table::
   :file: /tables/01style_commands.csv
   :header-rows: 1
   :widths: 55, 80

.. raw:: html

   </details>

|

.. Note:: 

   the variables quoted here are local variables, so style may be a reference 
   to a widget class or cross-reference

.. topic:: Viewing Tables

   Most tables have been created as csv tables and can be independantly 
   viewed using a spreadsheet or loading into the ttk Treeview script 
   01view_csv.py (found in the examples directory), select the csv file
   from the dropdown list.

Buttons in tkinter and ttk
--------------------------

.. warning:: Image Quality

    Some IDEs will not show the images created in tkinter / ttk at the same
    resolution or quality if you are using an ultra high definition monitor.
    Standard monitors should be the same no matter which IDE is used. If 
    there is a difference run the Python script from the command line, Idle
    or use PyScripter.


Using buttons compare the two different types of widgets, use the script 
01two_buttons.py - found in the examples directory. You should see 4 buttons, 
the upper two buttons are standard tkinter, whilst the lower two are ttk 
buttons. 

.. |d2| image:: /figures/01two_buttons.jpg
   :width: 175px
   :height: 234px

.. |v2| image:: /figures/01two_buttons_vista.jpg
   :width: 175px
   :height: 238px

.. |c2| image:: /figures/01two_buttons_combined.jpg
   :width: 753px
   :height: 315px

..
    .. |t2| image:: /figures/01two_buttons_thonny.jpg
    :width: 299px
    :height: 188px

    .. |p2| image:: /figures/01two_buttons_pyscripter.jpg
    :width: 388px
    :height: 195px

.. table:: Comparing Client Interaction on Buttons

   ==================== ====================
   Default ttk Buttons   Windows ttk Buttons
   ==================== ====================
    |d2|                  |v2|
   ==================== ====================

..
    .. table:: Comparing UHD output on 2 different IDEs

    =================================== =========================
    PyScripter or Idle                  Thonny or many other IDEs
    =================================== =========================
    |p2|                                |t2|
    =================================== =========================

|c2|

.. sidebar:: User Interaction

   In order to fully appreciate the effects being discussed make sure to run
   the relevant script. Widgets are not wholly static so images alone cannot 
   give the full flavour.

All four buttons are grey but the tkinter buttons are paler. Move the cursor 
over all four buttons. The two ttk buttons lighten but the tkinter buttons 
do not react. Click on all four buttons, all four appear to be depressed, 
but the two ttk buttons will have a broken line showing which one of the two 
buttons was last activated. 

.. raw:: html

   <details>
   <summary><a>Show/Hide <b> Video </b> two_buttons </a></summary>

.. raw:: html

   <video width="320" height="240" controls>
      <source src="../_static/twobuttons.mp4" type="video/mp4">
   Your browser does not support the video tag.

.. raw:: html

   </details>

|

Buttons, in common with several other widgets, have what we call states, 
for example when a cursor passes over the widget its state changes to active, 
so we have just seen how the ttk button's state together with the theme used
affects its appearance.

Script 01two_buttons.py
^^^^^^^^^^^^^^^^^^^^^^^^

To view or hide the code just click on the arrow.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 01two_buttons.py

   .. literalinclude:: /examples/01two_buttons.py
      :linenos:
      :emphasize-lines: 13

If we had left out the line::

   13 s.theme_use('default')

and we were running either a Windows or Mac system then we would have seen 
blue ttk buttons because both operating systems have their own OS specific 
themes. 

By using a theme many ttk widgets react by default without any special input. 
This is in contrast to the original tkinter widgets which have to be 
individually programmed.