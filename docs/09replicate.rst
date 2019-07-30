.. _09replicating:

=======================
Replicating the Widgets
=======================

We are now in a position to replicate the widget images, as we have enough 
tools to draw most of the variations encountered.

We may be forced to create parts of the widget before or
after it has been reduced to the final size, dependant on the widget geometry 
and methods used in antialiasing.

.. topic:: Drawing at the Widget Size

   If we were to draw at the actual widget size we only need lines one pixel 
   wide and place pixels. However such an exercise would not help much in 
   creating widgets. In particular the corner construction, gradients and the 
   antialiasing would remain untested.

Ubuntu Combobox
===============

.. |comboa| image:: figures/08comboarrow_large.png
   :width: 80
   :height: 120

.. |combo| image:: figures/08combo_large.png
   :width: 120
   :height: 120

.. table:: combo-n.png and comboarrow-n.png

   ============================== ==============================
   |combo|                        |comboa|
   ============================== ==============================

Let's start with our old faithful - it shouldn't hold any surprises, just 
kidding.

Load comboarrow-n.png and combo-n.png into our image editor. This gives us
the sizes, layout and main colours without too much trouble. We are going to
create two files based on 08rounded_rectangle.py and 08rounded_rectangle_both.py.

If we tackle combo-n.png first, left and right sides seem to be mirror images,
just that the righthand side seems to have two columns cropped. The next 
question is whether the surrounding border consists of one, two or three 
frames. If three then we would see a shadow on the fourth row. We probably 
have a dark and a light frame, the shadow and highlight at the third column
and row we can add by hand. Next check that the central area is all one 
colour - since this is the text area this is not surprising. There are 
two areas of transparency at the uncropped corners.

The widget is 26 wide x 24 high (allowing for cropping, the outer and inner 
frames are #EDEBE7, #B6ABA0 whilst the central area is white. (The first
attempt used 2 pieslices, only joining the inner border). It looks alright
so let's reduce the image size ``img = img.resize((w,h),Image.LANCZOS)``. 
Looking at the result the corner definitely needs modification, the transparent 
area is way too large, and the outer antialias pixels have an alpha content 
that the original did not have. 

.. |a| image:: figures/09comboa.png
   :width: 147
   :height: 147

.. |combob| image:: figures/combo_corner.png
   :width: 114
   :height: 114

.. table:: Comparing Corners

   ================ ================
   Original          1st Attempt
   |combob|           |a|
   ================ ================

The outer frame needs to be joined by an arc this will reduce the background 
coloured corner area. Change the corner background to white seems a safe bet. 
We are going to modify the corner to have 3 pieslices. 

.. |b| image:: figures/09combob.png
   :width: 128
   :height: 128

.. |c| image:: figures/09comboc.png
   :width: 128
   :height: 128

.. |d| image:: figures/09combod.png
   :width: 128
   :height: 128

.. |e| image:: figures/09comboe.png
   :width: 128
   :height: 128
.. table:: Comparing Corners (more attempts)

   ================ ================ ================ ================
   2nd attempt       3rd attempt      just frame       4th attempt
   |b|               |c|               |d|               |e|
   ================ ================ ================ ================

Look at the 2nd attempt - it's better but something is still not right, the 
original has a straight diagonal ours kinks outwards, this was hidden by the 
alpha problem. Reduce the gap from 5 to 4 and run again. ( I saved the 
output to a new image). 

Look at the colour. When the filter is applied we know that colour is 
changed, the frame becomes lighter and the adjacent pixels become darker, 
the question is can we estimate by how much. 

Checking combo-n.png again we see that there are two adjacent rows of 
lighter colour beside the upper and lefthand part of the frame. Let's try
adding both these colours to the frame colour, then draw the darkened frame
using a white background. Outer colour (237,235,231), inner colour (242,240,
239) and frame colour (182,171,160) would give a start colour (151,136,120).

Using just the frame with no outer frame left too many white pixels in the 
corner, but all is not lost since we now have a frame colour that is too dark.
This simplifies finding the frame start colour. 

All we need do now is make the corner near white pixels transparent, whiten 
the righthand and bottom inner sides and crop the righthand side. As you can 
see these actions have been left until after the image is resized.

.. figure:: figures/09combolarge.png
   :width: 120
   :height: 120

   Constructed Combo 

Now for comboarrow-n.png, it has a main frame along the sides, the corners 
have a diagonal that bulges outward. There are highlights along the upper
and lefthand sides, the other two sides are shaded. The main area has a single
background colour, which helps in assessing what the starting frame colour was.
Lastly we have a downward pointing arrow, which we have already made, even
the antialias pixels.

Based on the script 08rounded_rectangle.py we should be able to create the 
frame, then set the arrow, place the transparent corner elements and draw 
the highlights. Using a simple border the gap size should be 5. The inner 
area is (246,244,242), the righthand shadow is (238,235,231) and the frame
is (215,208,200). We can therefore guess that the frame starting colour 
should be (207,199,189). 

The resulting rectangle looks good, but the final frame colour is not quite
right, which is not too surprising as we were using a different frame colour
to that found in combo, let's use that one. The result is slightly out, but 
within reason. Add the arrow, make the near white corner pixels transparent 
and add the highlights.

.. figure:: figures/09carrowlarge.png
   :width: 128
   :height: 192

   Constructed Comboarrow 

Afterwards compare the two widgets.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09compare_combobox.py

   .. literalinclude:: examples/09compare_combobox.py

They compare well, if anything the comboarrow has a slightly darker frame,
the arrow appears off centre so if we were to create from scratch, rather 
than copy it, it would be better to change the image width to 25, say, and 
run again.

Blue Theme - Scrollbar, Button 
==============================

Blue Scrollbar
--------------

.. |sb| image:: images/sb-thumb.gif
   :width: 28
   :height: 28

.. |bsb| image:: figures/09bluesb.png
   :width: 28
   :height: 28

.. table:: Blue Scrollbar Thumb

   ================= =================
   Original          Created
   |sb|              |bsb|
   ================= =================

Within the blue theme there are several widgets with a gradient. Some images
appear to be alike, so the scrollbar thumb and scrollbar left and right 
arrows have similar rectangular frames. Since the arrows are drawn across 
with an even number of pixels the arrow point is 2 pixels across. The slanted 
lines are made at 45 degrees without any antialiasing. It's surprising what 
you can get away with.

The blue scrollbar thumb can be used as a template. It consists of a simple 
frame, with all four corners made transparent, and a simple vertical gradient. 
There is no antialiasing. Let's go ahead and make this.

When counting the number of times that a line is drawn to make the gradient,
allow for the borders, if the first line has a y-value of 1 and the last 
line of 12 we actually have 12 steps (count inclusively). Since 
``range(steps)`` starts from 0 and ends at the maximum value less 1, it 
requires no adjustment. 

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09bluesb.py

   .. literalinclude:: examples/09bluesb.py

Blue Button
------------

.. |blue| image:: images/bluebutton-n.gif
   :width: 32
   :height: 32

.. |bl| image:: figures/09bluebutton2.png
   :width: 32
   :height: 32

.. table:: Blue Button

   =============== ===============  
   Original          Created   
   |blue|            |bl|         
   =============== ===============

The button frame looks more interesting than the scrollbar thumb. Use the 
medium blue colour as the background, draw a rectangle using the dark blue.
Run a simple gradient then create the corners using points.

Since there is no size change with filter there is no stray colours as in the
original, on the other hand the colour stays true.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09bluebut2.py

   .. literalinclude:: examples/09bluebut2.py

Clearlooks Button
=================

.. |clo| image:: images/cl_button-n.gif
   :width: 28
   :height: 28

.. |clc| image:: figures/09clbut.png
   :width: 28
   :height: 28

.. table:: Clearlooks Button

   =============== ===============  
   Original          Created   
   |clo|            |clc|         
   =============== ===============

.. sidebar:: Check Gradients

   Use 09find_line_colour.py to see whether gradients exist in the rows and 
   columns in the gradient area. Load the image and adjust the gradient area.

The clearlooks button looks straightforward until we notice  the pixel distribution in the
gradient area. First check whether there is a simple vertical gradient, 
then see whether there is a horizontal gradient. The checks show that the 
colour gradually changes vertically (rows), whereas horizontally it is steady.

Since the corner pixels and the gradient do not interfere, we can create a
round corner frame, reduce in size then insert the gradent and highlights. 
The frame is a simple one with a gap of 4. The frame colour (148,125,123) has
a shadow (231,219,214) along its lower and righthand sides. Let's choose
(148,125,123) as a first estimate. We can choose the corner pixel colour 
#EFEBE7 as our background. The result looked good, but the frame (155,133,131)
needed darkening, start with (141,117,115) instead. 

.. topic:: Calculating the Frame Colour

   Use the colour component differences between starting and resulting frame
   then subtract these differences from from the target frame colour.
   
   =========== ============== ==============
   Target      (148,125,123)
   Start       (148,125,123)  (141,117,115)
   Result      (155,133,131)  (148,125,123)
   Differences (  7,  8,  8)
   =========== ============== ==============

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09cl_but.py

   .. literalinclude:: examples/09cl_but.py

Elegance Button
===============

.. |elo| image:: images/elegance_button-default.gif
   :width: 60
   :height: 34

.. |elc| image:: figures/09eleg_button.png
   :width: 60
   :height: 34

.. table:: Elegance Button

   =============== ===============  
   Original          Created   
   |elo|            |elc|         
   =============== ===============

The elegance button's gradient looks quite challenging. The frame looks 
simple, but it actually changes colour. One approach would be to create a single 
gradient and darken the lower half, or we could make two gradients. Any 
antialiasing effects are not showing strongly.

The button appears to have a 2D gradient, in that the rows and columns 
change. Checking with 09find_line_color.py, the rows change on average from
(230,231,230) to (200,200,200) upto the mid point, whilst the upper half 
column changed from (227,227,227) to (207,207,207) and back to (226,226,226).
In the lower half the rows were pretty static, changing from (184,184,184) to
(180,180,179), whilst the columns changed from (199,199,198) to (168,168,168)
and back to (196,196,196). 

The gradient can be based on 08radial_gradient.py where points are coloured
according to the distance of the point from the centre. An alternative 2D
gradient can be created by using the ellipse.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 09elegance_button.py

   .. literalinclude:: examples/09elegance_button.py




