.. _03style_with_state:

===========================
Linking Style with State
===========================

States
======

Style.map()
-----------

Every widget exists with a state that for some widgets can be directly 
changed by the user's actions, such as moving the mouse over the widget, or 
by selecting or pressing the widget. Whenever the state changes the widget 
changes in colour, relief and/or size thus providing the user feedback. Other 
states which are not being changed dynamically are changed by the program. 
States are a fundamental part of styles and themes.

.. seealso:: Buttons changing with state, remember :ref:`01two_buttons<Script 01two_buttons.py>` 
   at the end of the Basics chapter. 

03states.csv
^^^^^^^^^^^^

.. csv-table:: 03states.csv
   :file: tables/03states.csv
   :header-rows: 1
   :widths: 15, 150

All states also have an opposite condition in which the 
name is prefixed by an exclamation mark, so the opposite of ``disabled`` is 
``!disabled`` and not one of the other states, such as active.

Some widgets, such as Frame would hardly ever need a state other than the 
normal state, others such as Button are only really useful if they use several
different states. When programming with states be aware that a widget with 
no named state is in the "normal" state even though normal cannot be directly 
referenced, it is implicitly the state we have previously used when making simple changes 
to the widget with Style.configure. When we survey states some are never used, 
or as the captain of the Pinafore might say - hardly ever used.

.. |normal| image:: figures/normal.jpg
   :width: 89px
   :height: 33px

.. |active| image:: figures/active.jpg
   :width: 90px
   :height: 33px

.. |disabled| image:: figures/disabled.jpg
   :width: 89px
   :height: 34px

.. |focus| image:: figures/focus.jpg
   :width: 88px
   :height: 32px

.. |pressed| image:: figures/pressed.jpg
   :width: 88px
   :height: 34px

.. sidebar:: States for Default Button

   Other states such as alternate, background, invalid, readonly and selected
   look just the same as the normal state.

======== ============== 
 normal  |normal|
 active  |active|
disabled |disabled|
focus    |focus|
pressed  |pressed|
======== ============== 

We can determine what states are currently being used in a theme. Just as in 
the simple style change we need to know the class name and the element we 
are interested in.

.. topic:: Relief 

   Use your interactive session to check the Button components, we'll
   find relief lurking under Button.border - it's where we determine whether
   the widget will be displayed as flat, raised, sunken, groove or ridge.
   If we already knew that ``relief`` was the correct element name we can use it 
   directly.

.. figure:: figures/03relief.jpg
   :width: 420px
   :height: 41px

   Relief Styles

So if we wished to find the situation for the relief element on a button we 
use Style.map() in the following manner::

   from tkinter.ttk import Style, Button
   >>>St = Style()
   >>>St.theme_use('default')
   >>>St.map('TButton', 'relief')
   [('!disabled', 'pressed', 'sunken')]

In this case the theme uses a compound state, in that the pressed state only 
applies when the button is not disabled, and the relief element becomes 'sunken'. 
These mapped states vary with both widget and theme. Within a theme we can 
have a common mapping::

	>>>St.theme_use('default')
	>>>St.map('TButton', 'background')
	[]

Weird it's showing nothing - but we know that the background, as used in text,
changed in our button examples, so how to find out what is going on.

.. sidebar:: "Background" is mapped with ``.`` 

   Ahha - now we can see that all widgets with a "background" element will 
   react in a similar way, so if you haven't done it see what happens when 
   you pass the cursor over our scrollbar example :ref:`02scrollbar`.

Let's see if we have a common mapping working here::

   >>>St.theme_use('default')
   # '.' is the shorthand for common mapping
   >>>St.map('.', 'background') 
   # here we have two separate states being mapped 
   [('disabled', '#d9d9d9'), ('active', '#ececec')]

If we test for relief, which we looked at on button, with a common 
mapping we get an empty result::

	>>>St.map('.', 'relief')
	[]

Since the common and button mapping may have more than one state what happens 
if we query it without any elements::

   >>>St.map('.')
   {'background': [('disabled', '#d9d9d9'), ('active', '#ececec')],
   ^            ^
   'foreground': [('disabled', '#a3a3a3')]}
               ^                          ^
   >>>St.map('TButton')
   # added element name 
   {'relief': [('!disabled', 'pressed', 'sunken')]} 
   ^        ^                                     ^

.. Note:: The element name has been added with the extra curly brackets and 
   full colon. When we have 2 or more elements the parts are enclosed in 
   curly brackets.

Some of the behaviours and properties of ttk widgets are now a little more 
understandable when we use the common mapping system. If we are working with 
a widget such as label with no dynamic states, it makes no sense to send 
warning messages if a widget does not have that particular element or state. 
The other minor problem is that only widgets with the exact element name will 
react in a similar manner, so button has 'background', whereas entry has 
'fieldbackground' and must be programmed separately.

One way to change the properties of a widget is to expand upon our simple 
method, so the normal state is set by configure(), we can then set the other 
states using map(). This means that any single element could have several 
properties corresponding to more than one states. Related states should be 
listed with tuples. We can see this in the example above for common, we have 
an element called background with a list of two tuples, the first tuple is for 
the disabled state ('disabled', '#d9d9d9') and the second tuple 
('active', '#ececec') applies to the active state.

.. _03mapbutton:

Script Map Button
^^^^^^^^^^^^^^^^^^

.. figure:: figures/03map_button.jpg
   :width: 154px
   :height: 92px

In the example 03map_button.py 

.. literalinclude:: examples/03map_button.py
   :lines: 12-19

we have configure which sets up the general widget appearance then uses map 
to set the active state by changing the background colour. Both configure and 
map utilise the same reference found in Button's `style` property option. 

We randomly select from 6 colours, to set the active colour 
we first find the RGB colour using winfo_rgb(color) - color is the variable 
- then we change each of the RGB components and finally convert back to the 
hash value. Simple colour manipulations are straightforward in the RGB scheme. 
A further frill is that we use a white foreground for a dark background and 
a black foreground for a yellow background.

Script Combobox in a Theme
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: figures/03map_combo.jpg
   :width: 171px
   :height: 41px

.. topic:: Remember 

   If you are running under windows or mac and the "theme_use" command is 
   commented out the combobox will be white, not green, even with 
   ``style.theme_settings("default"``.

When using Style.configure and Style.map you would normally run as 
separate clauses within the program, however if we use theme_settings the 
commands configure and map can be run together into a single clause. 

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 03combobox.py

   .. literalinclude:: examples/03combobox.py

.. note:: See how configure and map are used in theme_settings - with quotes 
   and followed by a full colon. 

Since we are running the program as a theme, combobox will react to our 
settings without the need for Combobox to have a property style setting. 

Punctuation in Map
^^^^^^^^^^^^^^^^^^

Now is a good time as ever to review the punctuation, in particular all the 
brackets being used. Theme_settings is a function so it has opening and closing 
round brackets, all those curly brackets look suspiciously like nested 
dictionaries, especially when we note the full colons following "Combobox", 
"configure" and "map" (our erstwhile functions), "background", "fieldbackground" 
and "foreground" are the relevant elements. The states and their relevant 
values (in these cases colours) are contained as pairs in tuples - round 
brackets. When we have two or more states used on a single element then we 
have a list of tuples - square brackets. But you probably already knew that. 

.. seealso:: 

   Just look at :ref:`03map_button.py<03mapbutton>` again and compare how the 
   programming differs when using style.configure or style.map as standalone 
   functions. 

When using a standalone theme, coming up soon, the method of theme_settings 
is the same as that used in theme_create. Theme_settings changes the style of 
the parent theme for a widget or two, all the other widgets still appear as 
normal - so theme_use still refers to the parent theme, whilst theme_create 
supplants the parent theme and we would instead refer to the newly created 
theme name in theme_use.

Keeping to the style system we can easily have two or more widgets with 
differing properties - this is useful when comparing appearances and state 
changes during the testing phase and help in choosing the most appropriate 
settings.

Mapping is primarily concerned with dynamic widgets and their states, but we 
know that there are states that need to be selected from the program, in 
this case use the following construct for ttk, (see 03states_themes.py,
coming soon)::

	checkbox.state(['selected'])  # ticks the checkbox
	checkbox.state(['!selected']) # clear the checkbox

whereas in tkinter we would use the following construct::

	listbox['state']='normal' 
	listbox['state']='disabled'

.. warning::

   The order of mapping states for the element is important. If the active 
   tuple is placed before the pressed tuple then when the button or scrollbar 
   is pressed the colour remains as the active colour without changing for 
   other states. As ever - test first.

It is useful to be able to see the individual widgets when changing their 
states. 03states_themes.py gives you the abilty to do just that, 

States and Themes
-----------------

.. figure:: figures/03themes_states.jpg
   :width: 215px
   :height: 300px

Script 03states_themes.py
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. topic::   Anticipating ttkthemes

   The additional themes from ttkthemescan can be enabled, the standard 
   themes will still be available whether ttkthemescan are enabled or not.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 03states_themes.py

   .. literalinclude:: examples/03states_themes.py
      :emphasize-lines: 17-25

there is no problem changing themes, however when changing states we need to 
cancel the previous state by applying the opposite state (you remember the 
state prefixed with an exclamion mark), we also have to ensure that we are 
dealing with a string rather than a tuple, further we must ensure that the 
tuple is not empty. In our example we are changing the state of a button, you 
can modify this or add another widget as required. 

As we have already seen states are not only used singly, they may be used in 
combination, particularly in dynamic situations. The common themes do not 
always use the same states for any particular widget, if we are building 
custom widgets keep this in mind, as ever test using different themes. Check 
out the table 03mapped_states.csv to see the states that the themes use with 
which widget.

.. csv-table:: 03mapped_states.csv
   :file: tables/03mapped_states.csv
   :delim: ;
   :header-rows: 1
   :widths: 20, 20, 55,45,25,25

Colour your own
---------------

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

   .. literalinclude:: examples/03checkbox_themes.py

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

In 03combobox_text_themes.py we have a dictionary of element_options containing 
a list of elements with their options, colour, size and font, these are then 
listed in style configure and can then be added to the Text widget so that we 
display each element with its colour option as a hash value and a rectangle 
of colour. 

Almost all the elements react as expected except for the font for combobox, 
which is unusual in that it will not react with configure and the style 
property, nor will it change with the font property - as the Entry widget does. 
A special class is therefore required to allow us to change the font of the 
specified combobox, which is written to allow other properties to be included. 
A simpler method is to use option_add but it seems to affect all the other 
comboboxes. 

Combobox is derived from the entry and listbox widgets and this 
might explain this anomoly in some way.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 03combobox_text_themes.py

   .. literalinclude:: examples/03combobox_text_themes.py

When using font we can refer to each instance of the font directly - such as 
'Helvetica 12 Bold' - or we can use the generic names used by Tk 03tkfonts.md,

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