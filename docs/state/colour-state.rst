===============
Colour your own
===============

How will a widget look when the style or theme is changed. Tkinter is rather 
forgiving so we can have a list with too many changeable elements and see 
just how they will react. Using this property we can see how and which 
elements affect our widget. This then simplifies our task when testing 
widgets, in that the Style.configure variables stay the same and only the 
widget is changed, and we still see the effect on the widget. 

Look at the script for Checkbox Themes, 

Checkbox themes
^^^^^^^^^^^^^^^^

.. image:: /figures/03checkbox_themes.jpg
   :width: 281px
   :height: 261px
   :align: center

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 03checkbox_themes.py

   .. literalinclude:: /examples/03checkbox_themes.py

As you can see not only do we have an excess of element names, but we can 
also display the layout of the widget and change the theme. Remember 
a widget is affected both by changing the theme and its element colours. 
A second widget is run in parallel where its configuration is not changed
but it changes with the theme.

A further improvement can be made by using tkinter's Text so that the name 
and its colour representation can be made in one line. 

combobox themes
^^^^^^^^^^^^^^^^

.. image:: /figures/03combobox_themes.jpg
   :width: 787px
   :height: 493px
   :align: center

.. tip:: The image was created using the **default** theme, if in Windows or 
   Mac do not forget to change the theme.

In 03combobox_text_themes.py we have a dictionary of element_options containing 
a list of elements with their options, colour, size and font, these are then 
listed in style configure and can then be added to the Text widget so that we 
display each element with its colour option as a hash value and a rectangle 
of colour. 

Almost all the elements react as expected, as Combobox is derived from entry 
and listbox widgets font would normally be changed by the font attribute 
rather than through style. 03combobox_text_themes.py has a special method
that allows style to change font - whether it is required or not depends on 
the application.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 03combobox_text_themes.py

   .. literalinclude:: /examples/03combobox_text_themes.py

When using font we can refer to each instance of the font directly - such as 
'Helvetica 12 Bold' - or we can use the generic names used by Tk,

.. table:: tkfonts

   =================== ================================================================
   Tk Standard         Font Description
   =================== ================================================================
   TkDefaultFont       The default for all GUI items not otherwise specified.
   TkTextFont          Used for entry widgets, list boxes, etc.
   TkFixedFont         A standard fixed-width font.
   TkMenuFont          The font used for menu items.
   TkHeadingFont       The font typically used for column headings in lists and tables.
   TkCaptionFont       A font for window and dialog caption bars.
   TkSmallCaptionFont  A smaller caption font for subwindows or tool dialogs
   TkIconFont          A font for icon captions.
   TkTooltipFont       A font for tooltips
   =================== ================================================================
 
which has the advantage that they are compatible to all operating systems, 
and no special precautions should be necessary. If you do use custom fonts 
obviously check on their availability on other os - maybe easier said than done.