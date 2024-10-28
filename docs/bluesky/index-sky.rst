
.. _07blue_sky:

====================
07 Blue Sky Thinking
====================

Rather than adapt one of the existing ttk or ttktheme themes, 
as demonstrated previously - we are going to be a bit more unconventional.

With hardly any drawing we can create
widgets that show off different facets. 

* Frame 
   soft introduction into using an image and standard Style.element_create
   and Style.layout
* Piratz Sizegrip 
   widget with single state using Style.theme_create then ``"element create"`` 
   (two separate words)
* Piratz Label 
   multiple states, showing how to ensure the image expands correctly and 
   setting the text position.
* Piratz LabelFrame 
   showing that the frame element still responds correctly when text is inserted.
* Piratz Scrollbar 
   first use a layout then add a completely new element.
* Piratz Separator 
   Using layout to create vertical and horizontal elements that did not yet exist.
* Piratz Button 
   Creative states, also added layout to change position of dashed line when
   using focus
* Piratz Progressbar and Scale 
   a little animation

Piratz
======

In my quest for blue sky thinking I'm using piratz as a theme, that was 
fun to dream up the widgets and their associated images then see how to display 
them. The second example 07pirate_label.py can be used as a template for our 
subsequent pirate examples.

.. toctree::
   :maxdepth: 3

   frame
   sizegrip
   label
   labelframe
   entry
   combobox
   scrollbar
   separator
   radio-check
   note-tree
   button
   progress-scale
   theme