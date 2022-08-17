Create a Standalone Theme
=========================

Using information gained from existing themes, we'll try to use common images
as done in the ttktheme Blue, and borrowing heavily from the Ubuntu theme for
style. The standalone theme in python can be easily tested, although if you 
are competent in TCL I'm sure it's just as easy to test with that language.

After the first attempt or so it was found that the widget sizes had to be 
changed, so common images were not always possible. This 
theme will use images for most of the varying widgets and their states. Many 
widgets in ttktheme simply reused the standard theme, sometimes altering the
colour of an element or two. 

Common Imported Code
--------------------

.. sidebar:: Naming Common Code

   Each of these two scripts roundrect and tools and have no preceeding chapter 
   number so that they can be imported.

Using one starting image it should be possible to create most, if not all, of 
the other images for a single widget. Use a class from roundrect
that can create a rounded rectangle with a plain or gradient filled inner 
part. The border can be single or double. Each of these four options 
can be made with an open side as used in tabs for the notebook. Supply the 
size, enlargement factor, gap (radius), fill and gradient colours whether it 
should be treated as a tab.

.. table:: Options for roundrect.py

   =============== ======== =============
   Class           Border   Internal Fill
   =============== ======== =============
   Base_Rect         single plain
   Bi_Base_Rect      double plain
   Gr_Base_Rect      single gradient
   GR_Bi_Base_Rect   double gradient
   =============== ======== =============

Each option provides a completed image.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* roundrect.py

   .. literalinclude:: ../examples/roundrect.py

Where a non-standard widget is created use tools.py, which can be supplemented
as necessary. The toolbox only uses functions, so it is possible to 
work with an image that is already opened in the calling program, make the 
change then return back to the original image. When creating a border with
its own gradient there are actions that need to be made before the image is
resized, so the complete widget would not be suitable. Examples are given in
the alternative button, scale trough and progressbar.

Only gr_2d_rect creates an almost complete widget, used to make a simple
border with 2d gradient based on rectangles, otherwise the other functions
are called individually.  

.. container:: toggle

   .. container:: header

       *Show/Hide Code* tools.py

   .. literalinclude:: ../examples/tools.py

Each widget has its own generation and separate test script. The latter are 
similar to the 07pirate scripts. 
