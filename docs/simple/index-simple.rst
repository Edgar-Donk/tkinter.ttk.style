.. _02SimpleStyleChanges:

=======================
02 Simple Style Changes
=======================

.. sidebar:: Query

   Each enquiry relies on the information gained from the previous enquiry. 
   Once the queries are set up with an interactive session using 
   Style() you may be able to short circuit one or more steps.

.. topic:: Finding out the Element

   Using named elements we can change the colours, width, font and relief of 
   our widget. Instead of using property options on each widget, we use the 
   Style module together with relevant component and element names. The first 
   task is to determine the relevant component and element names of our widget.

The sequence of the queries to find out the elements and their properties 
is as follows::

   --> 1 Widget name
   --> 2 class name (widget.winfo_class)
   --> 3 component name (Style.layout)
   --> 4 element name (Style.element_options) 
   --> 5 element value (Style.lookup)

.. toctree::
    :maxdepth: 3

    button-style
    orientated-widget
    widget-with-aux
    style-configure