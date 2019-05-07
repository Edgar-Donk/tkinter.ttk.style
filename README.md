### tkinter.ttk.style

# Tkinter in Python - you've got to have style!

As you are no doubt aware tkinter introduced a theme (or tile) based module. Searching the web I was struck by how little the
new capabilities were demonstrated, questions and answers concentrated mostly on how to colour widgets and suchlike.

In order to use the scripts developed here, a modern version of Python and Tkinter (>= v 8.5) will be necessary, it is advisable to use
version 8.6 or greater and use png files. I find it helpful to download the pdf version of “Tkinter 8.5 reference: a GUI for Python” 
http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf, then run it on a pdf reader. At some stage we will be encoding and
decoding small images using the base64 module. To see what has already been achieved it will be helpful to view and install the
external module ttkthemes (pip install ttkthemes) found at https://github.com/RedFantom/ttkthemes. Since we will be checking images, a
graphics editor will also be useful.

## What to expect

A quick tour, with working examples, through the tkinter.ttk Style module, so that you should be able to test a widget and check 
its styling changes on your own ideas and scripts.  

An even more lightning tour through the themes from tkinter.ttk and ttkthemes.

Create a few specials to show what can be achieved then create a standalone version, after that you are only limited by your
imagination, where an appreciation of PIL (Pillow) will be useful.

## 01. Basics

If you are using Python 2.7 or later or any of the Python 3 versions then the tkinter version will be 8.5 or later, and if we 
import the ttk module in an active Python session then there will be no warning message.

1 import tkinter.ttk # applicable to Python 3 - all scripts will assume Python 3 is being used 

2 import Tkinter.ttk # applicable to Python 2

To help distinguish which examples refer to any particular paragraph, the file names will be prefixed by the chapter number.

All the widgets previously found in tkinter remain, ttk has 17 widgets and 1 Style module. 2 of the widgets in ttk, Combobox and 
Treeview are new. The widgets Canvas, Listbox, Message, OptionMenu, Spinbox and Text only exist in tkinter. All other widgets are
duplicated, with the proviso that their property options do not correspond, so if we take the Button widget, in tkinter there are 24
more property options than in ttk which has a single <style> option replacing those former options, the remaining 10 property options
are common to both Button widgets. When we talk about style we are generally only applying it to a single widget, whereas if we create
a similar looking style in several ttk widgets we could save it as a theme. The example 01Label_config.py shows the differences in
property configurations found in the older tkinter and newer ttk Label.
  
Ttk has already created 4 standard themes common to all operating systems. Windows and the MacOS have their own customised
themes, therefore wherever possible my examples will use one of the 4 common themes alt, clam, classic or default. In any 
interaction with a ttk widget we will be using the Style() module imported from ttk. The table 01style_commands.md has a summary of all
the Style() commands, we will be going through these commands one by one.
  
We can think of a widget in terms of a collection of components, which in turn are made up of elements. Widgets have one or more
components that can be referenced directly using the Style module, assisted by the widget "style" property option. Just to clarify -
every ttk widget has a "style" property which is used when we wish to modify a widget's appearance (colour, size, relief and font). If
we take a look at the button widget we have a rectangular shape divided into 4 components, starting from the outside - border, focus,
spacing and label. Look at
```
```
![button:components](/images/01button_components.png) 


this is a typical example of how a button may be constructed. We shall see that when a widget is modified or called by various themes
the component and element names may change. While we are thinking of components look at the vertical scrollbar 

![scrollbar:components](/images/01scrollbar_components.png) ,

we have an up and down arrow as well as a thumb component all contained in a trough. We have a method within the Style module whereby
we can easily find out the component names and their relative positions, so there is no real reason to worry or fret about trying to
remember everything in detail.

Let us compare two diferent types of button widgets, using the script 01two_buttons.py - found in the examples directory. Running this
script you will see 3 buttons, the top button is the standard tkinter, the lower two are both ttk buttons. All three buttons are grey
but the tkinter button is paler. Move the cursor over all three buttons. The two ttk buttons lighten but the tkinter button does not
react. Click on all three buttons, all three appear to be depressed, but the two ttk buttons show which one of the two buttons was
last activated. Buttons, in common with several other widgets, have what we call states, so for example when a cursor passes over the
widget its state changes to active, so we have just seen how the ttk button's state affects its appearance. The actual appearance is
set up by the individual style or theme.

If we had left out the line

s.theme_use('default')

and we were running either a Windows or Mac system then we would have seen blue ttk buttons because both operating systems have their
own system themes. 

By using a theme all ttk widgets react by default without any special input. This is in contrast to the original tkinter widgets which
have to be individually programmed.

## 02 Simple Style Changes

Using named elements we can change the colours, width, font and relief of our widget. Instead of using property options on each
widget, we use the Style module together with relevant component and element names. The first task is to determine the relevant
component and element names of our widget.

The sequence of the queries to find out the elements and their properties is as follows:-
````
--> 1 Widget name
--> 2 class name (widget.winfo_class)
--> 3 component name (Style.layout)
--> 4 element name (Style.element_options) 
--> 5 element value (Style.lookup)
````
Each enquiry relies on the information gained from the previous enquiry. Once the queries are set up with an interactive session
running with Style() you may be able to short circuit one or more steps.

Use the button widget as our first example and run the following queries interactively in Python. 
Find the class name:-
```
import ttk
>>> s = ttk.Style() # Style is used here to call the classic theme
>>> s.theme_use('classic')
>>> b = ttk.Button(None, text='Yo') # step 1 using the widget name of Button
>>> bClass = b.winfo_class() # step 2 find the class name using the Button handle b
>>> bClass  
'TButton'
```
The class name is 'TButton'. Now let's find the component name(s):-
```
>>> layout = s.layout('TButton')  
>>> layout # step 3 find the Button component names as used by the classic theme
[('Button.highlight', {'children': [('Button.border', {'border':
'1', 'children': [('Button.padding', {'children': [('Button.label',
{'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})],
'sticky': 'nswe'})]
```
It creates quite an output, but don't be put off. We have found 4 component names - highlight, border, padding and label (they were all
preceded by the widget name 'Button.'). Be careful to use the correct component name with right theme. That's just completed the third
step. As a help in determining the component names for every widget check out the table 02Components.md. See how the names change not
only with the widgets, but may change with the theme. 

Now onto the element names:-
```
d = s.element_options('Button.highlight') # step 4 find the element names
>>> d
('-highlightcolor', '-highlightthickness')
>>>s.lookup('Button.highlight', 'highlightthickness')
1 # step 5 the highlight is 1 pixel thick
>>> s.lookup('Button.highlight', 'highlightcolor')
'#d9d9d9' # step 5 highlight has a default or normal colour #d9d9d9 which is grey
```
Button is a fairly straightforward widget, but some such as Progressbar, Scale and Scrollbar have an orientation, whereas 
LabelFrame, Notebook and Treeview have a main and auxiliary class name. Lastly PanedWindow has both orientation and an auxiliary
part. 

When we have a widget with an orientation, such as Scale, let's see what changes:-
```
>>>b = ttk.Scale(None)
>>>b.winfo_class()
'TScale'    # class name
>>> layout = s.layout('Vertical.TScale') # It won't work if you use just TScale
>>>layout
[('Vertical.Scale.trough',
  {'children': [('Vertical.Scale.slider', {'side': 'top', 'sticky': ''})],
   'sticky': 'nswe'})] # we found 2 components, trough and slider
```   
Now try the Horizontal orientation.
```
>>>layout = s.layout('Horizontal.TScale') # 
>>>layout
[('Horizontal.Scale.trough',
  {'children': [('Horizontal.Scale.slider', {'side': 'left', 'sticky': ''})],
   'sticky': 'nswe'})]  # notice the changes that are specific to orientation
>>>d = s.element_options('Horizontal.Scale.trough') # using the component name
>>>d
('borderwidth', 'troughcolor', 'troughrelief')  # element names
>>>s.lookup('Horizontal.Scale.slider', 'troughcolor')
'#c3c3c3'
````
That wasn't too bad, we had to know whether the widget had orientation, which requires a capitalised first letter. 

Let's try a widget with an auxiliary class such as LabelFrame:-
````
>>>b=ttk.LabelFrame(None) # no properties are being set
>>>b.winfo_class()
'TLabelframe' # you noticed it's a small f didn't you, TLabelframe
>>>s.layout('TLabelframe')
 [('Labelframe.border', {'sticky': 'nswe'})]  # where is the label part then!!!?
>>>s.layout('TLabelframe.Label')    # OK I cheated, I knew the answer
[('Label.fill',
  {'children': [('Label.text', {'sticky': 'nswe'})], 'sticky': 'nswe'})]
````
It took a bit of web searching to find the answer in http://wiki.tcl.tk/37973 "Changing Widget Colors". Strictly the information is for
TCL so it may not be totally applicable to ttk, otherwise great information. In order to access all the elements of Notebook use
TNotebook and TNotebook.Tab, for Treeview use Treeview and Heading. (We can optionally use 'Treeview.Heading', it produces the same
results as for 'Heading'). Be careful with the component names used in the Treeview and Heading layouts (yes the Treeview class is
simply Treeview):-
````
>>>s.layout('Treeview')
[('Treeview.field',
  {'border': '1',
   'children': [('Treeview.padding',
     {'children': [('Treeview.treearea', {'sticky': 'nswe'})],
      'sticky': 'nswe'})],
   'sticky': 'nswe'})]
>>>s.layout('Heading')
[('Treeheading.cell', {'sticky': 'nswe'}),
 ('Treeheading.border',
  {'children': [('Treeheading.padding',
     {'children': [('Treeheading.image', {'side': 'right', 'sticky': ''}),
       ('Treeheading.text', {'sticky': 'we'})],
      'sticky': 'nswe'})],
   'sticky': 'nswe'})]
````
This now only leaves PanedWindow, the main class is TPanedwindow, the auxiliary class is either Horiontal.Sash or Vertical.Sash.

Rather than find out the class names every time we can use the table 02ClassNames.md instead. The main class name is formed from
the widget name where only the first letter is capitalised prefixed by a capital T, except for Treeview that retains its widget
name. Remember that those widgets that have orientation need to be prefixed by either 'Horizontal.' or 'Vertical.'.

After all that we now know the class and element names for all widgets for our chosen theme. We will use Style.configure().
As a first example let's change the button widget, we want to change the text properties, foreground, background and font.
Foreground and background are both colours which can be expressed as names or a six figure hexadecimal hash. Colour names in
tkinter are based on those used by TCL/TK colors — symbolic color names recognized by Tk https://tcl.tk/man/tcl8.6/TkCmd/colors.htm,
note TCL is using RGB values that must first be converted to hash values to be valid in tkinter. Haven't we got all the element names
for button already? No, then well we'll have to use the right component name in our query (and it wasn't highlight). Using your
interactive session, and if you were on the right track you should get the answer together with 11 other elements. Now you are no
longer limited to just foreground, background and font. 

As an aside we may wish to have the colours expressed in a different manner. The colour names used by various programs do not all
agree, so use 02colour_codes.py as an aid, each input will produce an alternative code style and the colour is shown on a label. Be
warned that green shows half the true value, (0,128,0) instead of (0,256,0) - this appears to be associated with winfo_rgb() -
otherwise it works well. We can detect how light a colour may be by using the luminance property of yiq, from the NSTC television
colour system, then we can adjust the foreground to produce the required contrast to the background colour.

When using Style.configure we require a reference to the style change using the format *newStyleName.oldStyleName*, where oldStyleName
corresponds to our class name, in this case TButton. Normally we choose a descriptive name for the newStyleName, so for the button
widget we can write :-
````
s.configure('green.TButton', foreground='green')
b = ttk.Button(self, text='Friday', style='green.TButton')
````
The style property of Button agrees with the style name for the relevant Style configuration. The configuration name can be
built on a previously named style, so we could create red.green.TButton using a red background, say. If we need to configure
another element just list the extra element.
````
s.configure('green.TButton', foreground='green')
s.configure('red.green.TButton', background='red') # our compound style
b = ttk.Button(self, text='Friday', style='red.green.TButton') 
# now change both style and configure from red.green.TButton to mix.TButton
````
We can modify /examples/01two_buttons.py to incorporate the colour changes, we should see something like 
/examples/02two_coloured_buttons.py. Did you notice that the background colour on the second ttk button changed as the mouse
moved over it also when the button was pressed. The widget inherits all expressly styled properties not overwritten by our style
changes, in our case shades of grey from the parent theme. 

That was easy wasn't it, feel like a challenge? Let's try modifying a horizontal scrollbar, use the layout and element_options
to find all likely element candidates for the classic theme. We need to use place and set (instead of pack or grid) when 
displaying the widget or else the scrollbar remains squashed and you can't see your results. If we make the scrollbar green with
a blue border the result should look like 02scrollbar.py. When querying the element_options you should see that both the arrows
and thumb have background and borderwidth elements so the appearance is matched. I have created a second scrollbar where the
borderwidth is not changed, look at the arrows. In reality there was not a great deal of difference to the button example, just
that we had to remember to add the orientation to the configuration name. If you try one of the other themes alt, clam or
default we have the additional option of arrowcolor, try out this element with pink say. Classic has no arrowcolor element but if you
forget to take away this element, then there is no reaction, not even a warning.

The last type of widget are those with auxiliary parts. Taking LabelFrame as an example, we would normally wish to modify the
label part rather than the Frame. We can fill the frame with a tkinter coloured frame to show off the widget. A second
labelframe, by contrast, has a coloured frame. It is important to emphasise that Style.configure calls either TLabelframe or
TLabelframe.Label, depending whether we wish to alter the label or the frame, but in both cases the style property only refers
to TLabelframe with no suffix. This is illustrated in /examples/02labelframe.py. The next example 02treeview.py shows how to
select a theme then apply some colour changes to the widget treeview, this has two sets of colours so we can confirm which works
best by first testing, then try uncommenting 'Heading' so that the treeview style reads 'Custom.Treeview.Heading '. The first
part of the script displays the widget layout in a form that is easy to read - there probably is an easier way to do this! To
view the colour changes we use 2 treeview widgets, the first has not been customised.

Generally try to keep it simple, try looking for an element that looks as though it should work, test it and see. Load a common
theme such as clam, remember that if working in a windows or mac environment it will not work as straightforwardly if the theme
is not changed. Look at 02Entry.py, if we use the clam theme it should create an entry with a blue background, however if
the clam theme is not used and you are running with windows or mac OS, then the entry widget has to change by adding an
element_create and adding the newly created element to layout. To find the correct element option, either check out "Changing
Widget Colors" or use query layout and element_options, then we see that Entry.field has ('bordercolor', 'lightcolor',
'darkcolor', 'fieldbackground') whereas Entry.textarea has ('font', 'width'). If you had used the element name background as we did for
button the entry widget would not have reacted.

We are now in a position to change the element colour and size of any widget, but whenever the state changes, such as pressing the
widget, it will revert to a style inherited from the parent theme, so the interaction of states and style will be our next topic.

## 03 Linking Style with State

Every widget exists with a state that for some widgets can be directly changed by the user's actions, such as moving the
mouse over the widget, or by selecting or pressing the widget. Whenever the state changes the widget changes in colour, relief and/or
size thus providing the user feedback. Other states which are not being changed dynamically are changed by the program. States are
a fundamental part of styles and themes. Check out the table /tables/03states.md. All states also have an opposite condition in which
the name is prefixed by an exclamation mark, so the opposite of disabled is !disabled and not one of the other states, such as active.

Some widgets, such as Frame would hardly ever need a state other than the normal state, others such as Button only really are 
useful if they use different states. When programming with states be aware that a widget with no named state is in the "normal"
state even though normal cannot be directly referenced, it is implicitly the state we have used when making simple changes to the
widget with Style.configure. When we survey states some are never used, or as the captain of the Pinafore might say - hardly
ever used.

We can determine what states are currently being used in a theme. Just as in the simple style change we need to know the class
name and the element we are interested in. So if we wished to find the situation for the relief element on a button we use 
Style.map() in the following manner:-
```
from tkinter.ttk import Style, Button
>>>s = Style()
>>>s.theme_use('default')
>>>s.map('TButton', 'relief')
[('!disabled', 'pressed', 'sunken')]
```
In this case the theme uses a compound state, in that the pressed state only applies when the button is not disabled, and the
relief element is 'sunken'. These mapped states vary with both widget and theme. Within a theme we can have a common mapping.
```
>>>s.theme_use('default')
>>>s.map('TButton', 'background')
[]
```
Weird - we know that the background changed in our button examples, so how to find out what is going on. Let's see if we have a common
mapping working here.
```
>>>s.theme_use('default')
>>>s.map('.', 'background') # '.' is the shorthand for common mapping
[('disabled', '#d9d9d9'), ('active', '#ececec')]
```
Ahha - now we can see that all widgets with a "background" element will react in a similar way, so if you haven't done it see what
happens when you pass the cursor over our scrollbar example. By the by if we test for relief, which we tested on button, with a
common mapping we get an empty result, so "." is a specific instance and not some form of wildcard.
```
>>>s.map('.', 'relief')
[]
```
Since the common and button mapping may have more than one state what happens if we query it without any elements:-
```
>>>s.map('.')
{'background': [('disabled', '#d9d9d9'), ('active', '#ececec')],
 'foreground': [('disabled', '#a3a3a3')]}
 
>>>s.map('TButton')
{'relief': [('!disabled', 'pressed', 'sunken')]} # added element name
```
Note how the element name has been added with the extra curly brackets and full colon.

Some of the behaviours and properties of ttk widgets are now a little more explainable when we use the common mapping system to
enforce uniformity in a theme. If we are working with a widget such as label with no dynamic states, it makes no sense to send 
warning messages if a widget does not have that particular element or state. The other minor problem is that only widgets with
the exact element name will react in a similar manner, so button has 'background', whereas entry has 'fieldbackground' and must be
programmed separately.

One way to change the properties of a widget is to expand upon our simple method, so the normal state is set by configure(), we
can then set the other states using map(). This means that any single element could have several properties corresponding to 
more than one states. Related states should be listed with tuples. We can see this in the example for common above, we have an element
called background with a list of two tuples, the first tuple is for the disabled state ('disabled', '#d9d9d9') and the second 
tuple ('active', '#ececec') applies to the active state.

In the example 03map_button.py we have configure which sets up the general widget appearance then uses map to set the active
state by changing the background colour. Both configure and map utilise the same reference used by the style property. For a bit
of fun we have a random selection from 6 colours, so we can set the active colour we first find the RGB colour using
winfo_rgb(color) - color is the variable - then we change each of the RGB components and finally convert back to the hash value.
Simple colour manipulations are straightforward in the RGB scheme. A further frill is that we use a white foreground for a dark
background and a black foreground for a yellow background.

When using Style.configure and Style.map you should notice that these are separate clauses within the program, if we use
theme_settings configure and map can then be run together into a single clause. Review 03combobox.py and note how configure and
map are now quoted followed by a full colon. (If you are running under windows or mac when the "theme_use" command is commented out
the combobox will be white, not green). Since we are running the program as a theme, combobox will react to our settings without
the need for Combobox to have a property style setting. Now is a good time as ever to review the punctuation, in particular all
the brackets being used. Theme_settings is a function so it has opening and closing round brackets, all those curly brackets
look suspiciously like nested dictionaries, especially when we note the full colons following "Combobox", "configure" and "map" 
(our erstwhile functions), "background", "fieldbackgrond" and "foreground" are the relevant elements. The states and their relevant
values (in these cases colours) are contained as pairs in tuples - round brackets. When we have two or more states used on a
single element then we have a list of tuples - square brackets. But you probably already knew that. Just look at 03map_button.py
again and compare how the programming differs when using style.configure or style.map, where they behave as normal functions
with explicit properties. 

When using a standalone theme, coming up soon, the method of theme_settings is the same as that used in theme_create. Theme_settings 
changes the style of the parent theme for a widget or two, all the other widgets still appear as normal - so theme_use refers to the
parent theme, whilst theme_create supplants the parent theme and theme_use would refer to the newly created theme name.

As we can see keeping to the style system we can easily have two or more widgets with differing properties - this is useful when
comparing appearances and state changes during the testing phase and helping in choosing the most appropriate settings.

Mapping is primarily concerned with dynamic widgets and their states, but we know that there are states that need to be selected from
the program - in this case use the following construct for ttk themes, (see 03states_themes.py):-
```
checkbox.state(['selected'])  # ticks the checkbox
checkbox.state(['!selected']) # clear the checkbox
```
whereas in tkinter we would use the following construct
```
listbox['state']='normal' 
listbox['state']='disabled'
```

The order of mapping states for the element is important. If the active tuple is placed before the pressed tuple then when the button
or scrollbar is pressed the colour remains as the active colour without changing for other states. As ever - test first.

It is useful to be able to see the individual widgets when changing their states. 03states_themes.py gives you the abilty to do just
that, there is no problem changing themes, however when changing states we need to cancel the previous state by applying the opposite
state (you remember the state prefixed with an exclamion mark), we also have to ensure that we are dealing with a string rather than a
tuple, further we must ensure that the tuple is not empty. In our example we are changing the state of a button, you can modify this
or add another widget as required. Anticipating what is coming later I have enabled standard themes or additional themes from
ttkthemes. 

It should be noted that states are not only used singly, they may be used in combination, particularly in dynamic situations. The 
common themes do not use the same states for any particular widget, if we are building custom widgets keep this in mind, as ever test
using different themes. Check out the table 03mapped_states.md to see what states the themes commonly use with which widget.

## 04 Image - First Steps

Tkinter and ttk can work with gif, pgm or ppm images using PhotoImage or xbm images if we use BitmapImage modules, loaded from
tkinter. If your version of tkinter is 8.6 or higher then PhotoImage also works with png files directly. Some widgets have a
property called image (check out if it is shown on Tkinter 8.5 reference: a GUI for Python) so once the image is initiated in 
PhotoImage it can be loaded directly onto the widget. All the images I will be working with will be found in the directory
"images". and the programs will be run assuming that the images sub-directory has the same parent directory as the examples sub-
directory on your computer.

Check out your tkinter version - either look at the python version then deduce the tkinter version or use an active session:-
```
import tkinter
print(tkinter.TkVersion)
```

First off we shall load just an image onto a button and see what happens when we pass the cursor over it, and press the button.
Load up 04button_image.py not forgetting to place the images butImage.png and butImageTrans.png in your images file (if you are
running tkinter 8.5 uncomment the lines as indicated, also comment out the lines indicated, this will load Image and Imagetk from PIL
then use Image.open and Imagetk.PhotoImage finally comment out the lines where PhotoImage is being used by itself). 
```
# with tkinter 8.6

        self.buttonPhoto = PhotoImage(file='../images/butImage.png') 
        buttonPhotoTrans = PhotoImage(file='../images/butImageTrans.png')

# with tkinter 8.5
from PIL import Image, ImageTk

        im1 = Image.open('../images/butImage.png') 
        im2 = Image.open('../images/butImageTrans.png') 
        self.buttonPhoto = ImageTk.PhotoImage(im1)  
        buttonPhotoTrans = ImageTk.PhotoImage(im2)

``` 
PhotoImage is imported from tkinter and loads the image into PhotoImage, where a reference is required which will be used within the
widget's property option "image". When working with images in a class there is always the problem that the image will not show unless
special precautions are taken. When the image is a local variable, reload the image directly after referencing it with the widget,
alternatively in class ensure that the image variable is prefixed by self, (compare how the two images self.buttonPhoto and
buttonPhotoTrans are treated). 

Using 04button_image.py you should see three buttons, the top one with just an image, the second uses the same image with the
centre made transparent - you may think it looks quite promising, until we see the third button and its text. As it stands it is
obvious that the image option is not always useful, since it does not change dynamically with the widget. Where a widget can work with
a single sized widget, as in a pictogram, then this option should be considered. We can load the pictogram image and text
simultaneously by using the "compound" property option. 

If multiple pictograms are available we can change these according to state. Check out the example 04button_pictograms.py, this
has three pictograms linked to 3 states which must have the active state listed last, just as we needed to do in the mapping 
situation. When using the image property always ensure that the first state remains anonymous, corresponding to the normal state.

Be careful when referencing the image in the image property:-
```
im1 = PhotoImage("ref1", file='myimage.gif')
```
We can use "ref1" as our image reference or im1 (unquoted).

## 05 Image - Create Widgets with Rounded Corners and Shadow Effects

The 4 themes common to tkinter can be found where your python program is installed under the directory python36/tcl/tk8.6/ttk. They are
found there listed with their own names suffixed with ".tcl", apart from default which is listed as defaults.tcl. There are
obvious differences between the scripting language tcl and tkinter but we can recognise some commands such as map and configure,
we can also spot the element and state names. A new part of the mix is when we look at the OS specific themes such as aqua or
vista which have variables that are system dependant. Even so we should be able to recognise how some of our scripts will respond. It
would seem that the common themes allow us to modify all the components and elements and are able to give the widest possible support
to any style alterations we wish to make. By contrast it will be found that if one tried to modify one of the OS dependant themes we
would require not so straightforward an approach. On the other hand the OS specific themes look up-to-date and ready to use as is. 

So far we have seen that the ttk themes achieve uniformity across all widgets, by using common changes on dynamic states, also 
by using the same element name within a widget or from widget to widget. A third aid to uniformity is by using using descriptive colour
aliases rather than the colour names or hash values.

As I said at the beginning there are remarkably few instances of the more interesting style changes found when trawling the
internet. Up until this point most of the examples could have been made referring "Tkinter 8.5 reference: a GUI for Python". The
few instances I did find that displayed rounded corners and shadow effects I will reproduce here.

The first example is based on that created by Bryan Oakley, a stalwart of StackOverflow. His original script created visible
frames around entry and text widgets, example 05rounded_frame.py. Since he is using encoded data there is no reference to a
file, instead PhotoImage refers to this data directly. Normally we have no states in the frame widget so he introduces lambda
functions tied into *FocusIn* and *FocusOut* events. He is using 2 separate images, the first is where the frame's contents have
focus, the second where it loses focus. Click within the upper and lower frames, see how the outer colour changes, also note
that the frame has decidedly rounded corners and a shadow on the right hand and lower sides. 
 
Let's remind ourselves about the layout and elements for frame:-
```
>>>s.theme_use('default')
>>>s.layout('TFrame')
[('Frame.border', {'sticky': 'nswe'})]
>>>s.element_options('Frame.border') # only one component to query
('background', 'borderwidth', 'relief')
```
In our example script, Bryan created an extra state and changed the border, using the command
```
style.element_create("RoundedFrame", "image", "frameBorder", # he was working on the RoundedFrame, so he added an image 
    ("focus", "frameFocusBorder"), border=16, sticky="nsew") # added the state focus  set to an image and changed the border to 16
```
The border size, 16, is important, it is the allowance needed to create the rounded corners and shadows, without this the 
resulting widget would look jagged. The single figure 16 is the equivalent of having (16,16,16,16), a border of 16 along all
sides. The lower frame has obviously grown in comparison to the upper frame and looks pretty smart, both frames have the same style
'RoundedFrame'. Now is a good time to have a look at the underlying image. To do this we will need to decode the coded image. Since the
script is quite old it was assumed to be a gif image. (Use all the lines of the coded image - the dotted line below is just a shortcut
for continuity).
```
import base64
with open ('frameFocusBorder.gif','wb') as f:
    decoded = base64.decodebytes(b"""
R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
..... 
Ry/99NIz//oGrZpUUEAAOw==""")
    f.write(decoded)
```
Use the code from img1 (frameFocusBorder) within 05rounded_frame.py, we should see that an image file frameFocusBorder.gif is
created. You should see a file that is 64 by 64 pixels large. Load this on an image editor, zoom in so that the pixels are shown
as squares and move your cursor to the centre of the corner, we then can see why we need to have a border of 16 all round. If we
reduce this figure to 8 say we will see about 13 indentations on the long side. A border of 12 will still show indentations, 
although not as pronounced, by 16 the indentations have disappeared altogether. It would seem that when a widget image needs to extend
only the inner part of the image between the border extremities is utilised for the extension, in this case the middle 32 pixels of
each side are used during an image extension. Think about what you have just seen, it's pretty awesome isn't it? That small image was 
automagically enlarged to the required size with the barest of input, apart from telling the widget to change itself by creating an
element and placing our image at the border.

What happens when we adapt the above method for a labelframe? What about the top part of the frame where the text is written
between a visible frame? Will we need a special method to create the gap? Ah well, fools rush in where angels fear to tread. Run
05rounded_labelframe.py. The labelframe reacts well, we see the label sitting in the frame break, and the colour changes as a
result of the program logic, try reversing the selection order and choosing one of the widgets with orientation. The
style.element_create and style.layout remain the same as for the frame example. Since we no longer depend upon an event linked
to the mouse being clicked the lambda functions are no longer needed, but we do change the state of the labelframes triggered by
command options of the widgets. You did notice the the frame has a different colour - first obtain the decoded image, make the changes
to the colour then encode back once again. 
```
import base64
with open('borderGrey1.gif', 'rb') as f:
    encoded = base64.encodestring(f.read())
    print(encoded.decode('latin1')) # contains all western characters but not the €
```
I altered the colour of the grey image. The output from the print command is saved as our coded image.

The next example, found by trawling the internet, 05search_entry.py will create a special frame, resembling the mac search element.
Once
again the image is loaded as encoded data, this time the programmer uses the gif property to make multiple images. Look at the
PhotoImage lines of code at the format property. The programmer is altering the entry widget, using the PhotoImage alias names "search1"
rather than the s1 variable. 
```
s1 = PhotoImage("search1", data=data, format="gif -index 0")
.......
style.element_create("Search.field", "image", "search1",
    ("focus", "search2"), border=[22, 7, 14], sticky="ew")
style.layout("Search.entry", [
    ("Search.field", {"sticky": "nswe", "border": 1, "children":
        [("Entry.padding", {"sticky": "nswe", "children":
            [("Entry.textarea", {"sticky": "nswe"})]
        })]
    })]
)
```
Compare its layout to that of a normal entry widget.
```
[('Entry.field',
  {'border': '1',
   'children': [('Entry.padding',
     {'children': [('Entry.textarea', {'sticky': 'nswe'})],
      'sticky': 'nswe'})],
   'sticky': 'nswe'})]
```   
The other item to note is how he deals with the border width. Originally it was 1 all round, now it is ```border=[22, 7, 14]```.
This follows the same convention as used for padding found in our Tkinter reference for 8.5, the left side is 22 and the right side 7
meanwhile top and bottom sides are 14. Check out table 05padding_border_layout.md. Since we are using the normal interactive states of
the entry widget, no additional programming is required as was necessary for the label example. Using our newly acquired image decoding
skills we can see how the border layout numbers are derived. 22 pixels clears the tail of the magnifiying glass, 7 pixels clears the
corner and the top clearance, whilst 14 pixels clears the right hand end. As it stands this widget could be lengthened horizontally, but
there is no way we can extend it vertically without a strange looking magnifiying glass formed as a result. When substituting an image
for a border ensure there is a section that can be repeated on complementary sides, that is repeated both left and right, also top and
bottom. We should now be able to understand how to manage themes. When we use a simple style change the affected widgets must have that 
style property cross referenced. When a theme change is made affected widgets require no reference, therefore the reference used in the
style changes, such as "search1" in 05search_entry.py, would not be appropriate. Instead we should be thinking of class names, once a
style has been tested and is ready to be part of the customised theme we would use just "TButton" rather than "new.TButton" say,
then all buttons would be altered by the style change within that themed script. 

Now would be a good a time as any to inspect what ttkthemes has to offer. Apart from the interface to python most is written in 
TCL scripting language. We can take stock of the themes on offer, most work with gif images, that are used as substitutes for
the border part of the relevant widget. Almost all ttkthemes use one of the 4 common themes as a parent, clam is the most popular,
although if you were to use a ttktheme it would be hard to tell which theme is the parent without inspecting the code. It is
interesting to note that Aquativo uses coded images, whereas the black theme has no images. Three themes use png images, but these are
only usable with tkinter 8.6 and above. Finally most images are quite small, about 30 by 30 pixels, with corners of one or three pixels
apparent radius - what apparent, yep there is no actual curved line, though it looks like there are corners there.

If you want to modify the gif images in an image editor there should be no great problem, provided you do not try converting to another
format and back again. Use the image editor for small simple changes. When checking out or modifying an image pixel by pixel using PIL
(Pillow) remember that gif only has 256 colours, requiring special programming, it would probably be better to use png from the outset.
The rgb and hsv values for gif images you see in your image editor are for your convenience.

If you were to install ttkthemes it is easy to switch between the normal themes and ttkthemes. Running the standard ttk Style module
excludes ttkthemes, however if you load up ttkthemes with the following script:- 
```
.....
        try:  
            import ttkthemes as ts 
            self.s = ts.themed_style.ThemedStyle()
        except (NameError, AttributeError):
            self.s = Style()
```
then any normal command used by Style can be used unchanged, providing we use the same prefix system, in our case "self.s.", so
list(sorted(self.s.theme_names())) would work for both the standard themes and the ttkthemes.

When comparing the script of a ttktheme with a standard theme the first obvious difference is that we are loading the image files and
using photo (known as PhotoImage in tkinter) on all the images, which are then later referred to by their image name without the gif or
png suffix. Thereafter the ttkthemes closely follow the standard themes by first loading up the colour aliases, then configuring the
general settings using configure, followed by mapping the general states. From thereon the themes configure and map out the
individual widgets, often the simple widgets are left out in which case the parent theme's widgets are used. The images are loaded
using $I(image filename) as opposed to "image" in python. The padding and border sizes would be shown as:-
```
-padding {6 2 6 2} or -border {22 7 14}
compared to using python
padding = [6, 2, 6, 2] or border=[22, 7, 14]
```
After all that we see that ttkthemes show one or two major differences to the standard themes - all states require their own separate
images for each widget, which if properly used allows a more pleasing effect, look at the different ways that the combobox downward
arrow is depicted. Check some of the images - you may notice that a pressed image is the same as a normal image except that it has been
inverted (this is often the case where a button has a surface with a 3D effect). Some themes could be easily adopted as they stand,
others just may be of use in showing you how to obtain certain effects. Note that radiance and ubuntu are very nearly the same except
that ubuntu uses png as opposed gif images. So once you are aware of how the themes work you may decide to devise your own. It takes
quite a bit of time but is relatively straighforward.

## 06 So you want to roll your own

Anything you do should be separated from working directories, use copies of anything you want. Pretty obvious really.

How will a widget look when the style or theme is changed. Tkinter is rather forgiving, which may make tracking errors
difficult, but we can have a list of too many changeable elements and see just how they will react. Using this property we can see how
and which elements affect our widget, look at the script 06checkbox_themes.py, not only do we have an excess of element names, but we
can change the theme, we also display the layout of the widget. It is a simple edit to display another widget. Remember as we have seen
in ttkthemes a widget is affected both by the image and general colours. In this regard tkinter's Text is a useful tool in that the
name and its colour representation can be made in one line. In 06combobox_text_themes.py we have a dictionary of element_options
containing a list of elements with their options, colour, size and font, these are then listed in style configure these can then be
added to the Text widget so that we display each element its option and a colour shows the hash value and a rectangle of colour. Almost
all the elements react as expected except for the font for combobox, which is unusual in that it will not react with configure and the
style property, nor will it change with the font property - as the Entry widget does. A special class is therefore required to allow us
to change the font of a specified combobox, which is written to allow other properties to be included. A simpler method is to use
option_add but it seems to affect all the other comboboxes. Combobox is derived from the entry and listbox widgets and this might
explain this anomoly in some way.

When using font we can refer to each instance of the font directly - such as 'Helvetica 12 Bold' - or we can use the generic names
used by Tk 06tkfonts.md, this has the advantage that they are compatible to all operating systems, and no special precautions should be
necessary. If you do use custom fonts obviously check on their availability on other os - maybe easier said than done.

Let us refresh our memory of how a widget looks in the various themes, try 06theme_notebook.py, this has most of the important widgets
together with a theme selector. It has been set up to incorporate ttkthemes. The first tab contains most of the normally used widgets,
the second tab has a treeview, in order to see the scroll bars work it will be necessary to adjust the height and width using the
sizegrip, the third tab has the scale and progress bars. There may be widget styles that appeal in different themes, it should be
possible to mix and match to your taste provided that you copy widget definitions together with any required images.

Once individual styles have been tested, we need to to incorporate these into a theme that can be called directly from the 
application with a single import and a single call. Obviously it would be foolish to work directly on the tkinter.ttk directory.
One can concoct a complete standalone theme definition together with the appropriate images - but this is not for the
fainthearted. A simpler solution is to use the ttkthemes module, adding your own theme name.  

1. Create a new directory - give it an expressive name - say green
2. Choose a ttktheme and copy its main tcl file and image subdirectory together with their contents to the green directory. So
  just as with the original theme, we have a main directory called green, a main file renamed green.tcl, and a subdirectory also
  called green.
3. Edit green.tcl replacing the name of the original by your name - so using elegance as our example ttktheme 
```
  namespace eval ::ttk::theme::green {
    package provide ttk::theme::green 0.1
    ....
    LoadImages [file join [file dirname [info script]] green]
    ....
    ::ttk::style theme create green -settings {
    ....
``` 
4. Copy one of the pkgindex.tcl files from one of the themes to your main directory, replace the name of the original ttktheme
  by your chosen name
```
if {![file isdirectory [file join $dir green]]} { return }
if {![package vsatisfies [package provide Tcl] 8.4]} { return }

package ifneeded ttk::theme::green 0.6.2 \
    [list source [file join $dir green.tcl]]
```
5. Edit the pkgindex.tcl found under the parent directory of ttkthemes, add an extra line to the list of theme sources
```
  source [file join $themesdir green green.tcl]
```
6. edit ``` _widgets.py ``` file, in the main ttkthemes directory, in the section of pixmap_themes  add your theme to the list:-
```
pixmap_themes = [
        "arc",
        "blue",
        "clearlooks",
        "elegance",
        "green",
        "kroc",
        "plastik",
        "radiance",
        "ubuntu",
        "winxpblue
]
```
7. That should do it. Test that everything works after your editing. Now you can start to replace original widgets with your
  preferred widgets.
  
The alternative to the above is to create a standalone package that I said was not for the fainthearted, but is in reality not
too difficult. The main problems are the package will need to replicate what a tcl based ttktheme does but using python, loading
the image files while ensuring that the configure and map scripts for the various widgets run as a single script. We can use the
script for plastik_theme.py https://github.com/enthought/Python-2.7.3/blob/master/Demo/tkinter/ttk/plastik_theme.py as a basis
for our standalone - this should shortcut a lot of the work. Convert this script from python2 to 3, you should notice that the image
directory location has to be referenced by the calling program. Notice that the script uses Style.theme_create and follows the pattern
already seen in 03combobox.py for theme_settings. When testing copy the image files found in ttkthemes plastik to a suitable test
location, these will eventually be replaced by new files of your own making.

We can test the python version of the plastik theme by running the script 06treeview.py directly from your os system not using python's
Idle, under the main function we call install from plastik_theme, you will notice that it has plastik as a variable, so plastik is a
subdirectory where the plastik images have been copied to. We can now change the plastik directory and subdirectory, these can be
renamed after your theme name, say orange, then wherever we find plastik referenced in plastik_theme.py we should change it to our
orange theme name, orange_theme.py.
```
style.theme_create("orange", "default", settings={
.....
style.theme_use("orange") # right at the end
```

We now have either an extra theme in ttkthemes controlled by a tcl file or we have a standalone theme running under a python
file. Associated with these control files is a subdirectory of image files. Either system is as valid as the other, the choice
is yours. The approach on using either is similar, after creating a good quality working widget with all the required states, we
just replace the ttktheme widget in either green.tcl or orange.py, change the references to any images, altering the border
sizes as necessary, then add your images to the image subdirectory. When everything works satisfactorily delete the unused images found
in green or orange image directories. Occasionaly it may be necessary to change the widget layout. In both methods we normally
translate between tcl and python, use the files plastik.tcl and plastik.py to help spot the differences and similarities between the
two languages.

Let's see if we can pin the above on an example or two. First let us change the combobox on both our test themes to that used by
radiance using green.tcl. On my computer, Windows 64 bit python 3.6, the combobox from elegance aka green looks like
``` 
```
![combobox:elegance](/images/elegance_cb.png) 
```
```
whereas radiance looks like
```
```
![combobox:radiance](/images/radiance_cb.png)
``` 
```
We need to compare the files and we see that radiance.tcl consists of the following :-
```
        ## Combobox.
        #
        ttk::style configure TCombobox -selectbackground

        ttk::style element create Combobox.downarrow image \
            [list $I(comboarrow-n) \
                 disabled $I(comboarrow-d) \
                 pressed $I(comboarrow-p) \
                 active $I(comboarrow-a) \
                ] \
            -border 1 -sticky {}

        ttk::style element create Combobox.field image \
            [list $I(combo-n) \
                 {readonly disabled} $I(combo-rd) \
                 {readonly pressed} $I(combo-rp) \
                 {readonly focus} $I(combo-rf) \
                 readonly $I(combo-rn) \
                ] \
            -border 4 -sticky ew
```
whereas green.tcl looks like :-
```
        # Combobox
        #
        ::ttk::style element create Combobox.field image \
            [list $I(combo-active) \
                {readonly} $I(button-active) \
                {active}   $I(combo-active) \
            ] -border {9 10 32 15} -padding {9 4 8 4} -sticky news
        ::ttk::style element create Combobox.downarrow image \
            [list $I(stepper-down) disabled $I(stepper-down)] \
            -sticky e -border {15 0 0 0}
```
In both cases the combobox consists of an element create for the components field and downarrow. Radiance has fewer images, which
luckily do not have a name clash. It seems that we can just replace the relevant script parts and copy all the radiance image files to
the green image directory. When this is done we can test with one of our files such as 06themed_notebook.py, or
06combobox_text_theme.py. If we look at the combobox created by green we get

![combobox:green_orig](/images/green_cb_orig.png)

which as you can see on my windows box is not quite the same as the radiance combobox, look at the position of the down arrow. If we
check green.tcl we see that there is no parent theme in the line 
```
::ttk::style theme create green -settings {
```
unlike radiance.tcl where we find
```
ttk::style theme create radiance -parent clam -settings {
```
since elegance aka green was probably created in Linux the normal theme would have been default. Using default as the parent theme the
combobox is not altered enough - let's try the clam theme instead - ahh far better.

![combobox:green_post](/images/green_cb_post.png)

Now for the orange theme taken from the py file. 
```
"Combobox.field": {"element create":
            ("image", 'combo-n',
                ('readonly', 'active', 'combo-ra'),
                ('focus', 'active', 'combo-fa'),
                ('active', 'combo-a'), ('!readonly', 'focus', 'combo-f'),
                ('readonly', 'combo-r'),
                {'border': [4, 6, 24, 15], 'padding': [4, 4, 5],
                 'sticky': 'news'}
            )
        },
        "Combobox.downarrow": {"element create":
            ("image", 'arrow-d', {'sticky': 'e', 'border': [15, 0, 0, 0]})
         },
```
We have to be careful not to overwrite combo- image files with our new files imported from radiance, give them a new designation,
say combor- so the old files remain until all has been tested. Also we have to ensure that we have the corresponding python taken
from the tcl in radiance.tcl. It's probably best to run a python test file such as 06orange_widget_test.py. Copy the necessary radiance
image files to a suitable images directory, adjusting the names as necessary. When running theme_create you can experiment having the
parent directory as default instead of clam - the results should be similar to those given in the green.tcl test. The resulting python
script within theme_create can be used to overwrite the combobox part of orange.py. We can test whether orange.py is correct using
06combo_orange.py, run under our OS directly rather than using python's Idle.

When working with radiance note how often the widgets have their images added by using "element create" - there are relatively few
widgets that require a layout and mapping. This bodes well for any future designs we may have since this is a relatively simple
construct. 

Onto our next exercise - let us create a button where the focus state's dashed line surrounds the button. In radiance we see that the
button part of the script looks like:-
```
        ## Buttons.
        #
        ttk::style configure TButton -width -11 -anchor center
        ttk::style configure TButton -padding {10 0}
        ttk::style layout TButton {
            Button.focus -children {
                Button.button -children {
                    Button.padding -children {
                        Button.label
                    }
                }
            }
        }
```
followed by an element create, which we can ignore as it does not concern focus. The first configure clause can be ignored as it 
concerns itself with size and anchor, however the second configure is interesting. Let us just insert this clause into the green.tcl
button widget.
```
        # Button
        #
        ttk::style configure TButton -padding {10 0}
        ::ttk::style layout TButton {
            Button.background
            Button.button -children {
                Button.focus -children {
                    Button.label
                }
            }
        }
```        
Testing this we see no effect which might not be surprising when we see that at this stage the button widget has no element named
padding. We can test this finding out the component and their element names from an active session. We can change the button layout of
the green theme and test again. It works! Let's try it out on the orange theme. Checking out the button we see we have a configure and
a layout that already has padding, so hopefully it works with only minimal changes. First we add padding to configure. When testing
this does not work, so we swop the button and padding positions.
```
        "TButton": {
            "configure": {"width": 10, "anchor": "center", "padding": [10, 0]},
            "layout": [
                ("Button.focus", {"children":
                    [("Button.button", {"children":
                        [("Button.padding", {"children":
                            [("Button.label", {"side": "left", "expand": 1})]
                        })]
                    })]
                })
            ]
        },
```
This works. The conclusion is that one may have to test the configure and layout options with a small script such as
06orange_widget_test.py adapted to suit your needs.

When dealing with states it helps to keep in mind what will be required in the program in relation to that widget. It certainly helps
to view how various themes tackled that problem. Some widgets can operate with a bare minimum of states, others may require quite a
few, but don't forget that some themes use the common settings to help display states without the need for additional images.

## 07 Blue Sky Thinking

We may decide to adapt one of the existing ttktheme themes, using constructs copied from other themes as demonstrated previously - that
is not what I mean by "Blue Sky Thinking", I mean something a little more unconventional.

The first example is probably best run as a standalone style for frame. The idea is copied from a website 
https://datatofish.com/how-to-create-a-gui-in-python/ that demonstrated how to use the tkinter canvas to contain the background image
and some other widgets together with a matplotlib interface. This works but the geometry management is limited to the canvas system. If
we use frame as our parent widget all the normal geometry managers - grid, pack and place - can be used. The only minor problem is that
it works best with a full view of the background image. Use the example 07frame_background_image.py to see what I mean, use a jpg image
of your choice as backdrop, typically a panoramic view. We are using jpg as the image type so that it can be downloaded from many
digital cameras and is usually half the size of a png or gif of equivalent size.
    
The next example can be used as a template for subsequent more complex widgets. In my quest for blue sky thinking I'm using piratz as a
theme, that certainly is different, but should not be taken too seriously, on the other hand it was fun to dream up the widgets and
their necessary images then see how to display them. The first example 07pirate_label.py can be used as a template for our subsequent
pirate examples, it can also be used to build up a standalone python script. We need to create our image, this invokes a Caribbean
island, the palm tree poses a challenge, particularly if the label grows in height. We choose border sizes that give the desired
effect, then we test using the theme construct rather than styling as an individual widget with configure, layout and map. With this
widget both theme_create and theme settings work equally well. To increase the height of the widget we can create two lines of text -
certainly easier than adding a configure clause. Try changing the border size to [20, 6, 4, 4], it looks reasonable if we have sticky
"ew" and only one line of code, however let's keep it suitable for more than one line of text and change back to the original border
size [19, 9, 7, 7] and sticky "news". Having created the image it is relatively easy to make it grey in our image editor and save the
image for the disabled state. The padding [19,5,3,3] is required to position the text. If we look at an enlarged image which shows the
pixels we can estimate the border sizes, after this is made to work the padding can be sorted out. If there is a surrounding area
around the image (maybe needed for shading) include this in your calculations. The text area has been made transparent, in fact the
appearance may look better without a white surround, instead make the surround transparent. When calculating sizes remember the first
line is 0 and we count from left to right on the first entry but right to left on the third, look at the image to get a feel.

![label:grid](/images/pir-label-grid.jpg)

Note we are using png images as later on it will help in subsequent widgets.

The labelframe was created, and the label was also invoked to ensure that there was no unexpected interaction between the two widgets.
The labelframe required padding to ensure that any widget placed inside the frame did not overwrite the frame.

The next widget we may consider is the Separator. At first glance it may seem to be a simple widget to alter, but if we try to do so
we will find that the separator has an orientation, but its only component consists of Separator.separator with no orientation. There
is no easy way to make the vertical separator react correctly as there is no vertical component. I have created 2 separator images in
the images directory which can be tested in an edited copy of 07pirate_label.py, 07pirate_separator.py - the relevant part of
theme_create is:-
```
    'Separator.separator': {"element create":
          ('image', "separator",
           {'border':[2], 'sticky': 'nsew'})}
```           
The horizontal separator works as expected, but the vertical separator image is forced to react as the horizontal image. As with the
scrollbar example use the place manager to display the widget and make the horizontal separator widg.place(x=5, y=5, width=150) then
vertical separator has widg1.place(x=75, y=50, height=150, width=5) which gives the best looking widget, but not perfect. We can
improve the situation if we add a second state then the vertical separator improves considerably, but we require a call to this second
state in the vertical mode.

Let us try the entry widget. The thinking here is that we have a fairly simple widget, so an image of an old yellowed document may be
appropriate. The image has irregular edges, so instead of a smooth expansion I have purposefully chosen border values that create more
jagged borders. If required we could impose an old font such as the equivalent of "Palace Script MT" in Windows. As with pirate label
there was no need to create a layout, element create is all we need.

Say we look at the combobox, it is best not to alter this too much - since we need to incorporate a drop down list - so let's use the
images from ubuntu. Remember ubuntu uses png, which are easier to manipulate than gif within PIL. We can see that ubuntu uses theme
create but has no need for layout. All the ubuntu images have a brown-beige look which we can change to aquamarine based colours using
07list_colours.py and 07shift_colours.py, this then matches our label widget. If we list the colours sorted by the sum of the colour
components, we can detect the different shades, then we apply the darkest shade of brown-beige to the shift colours as our main source
colour. The shift script sorts out the shades of brown-beige and substitutes shades of aquamarine. It is best to skip over arrows which
are grey by commenting out the relevant mask. Afterwards the arrows are removed by painting over using the appropriate image background
colour using an image editor. The arrow is then replaced by an anchor. There are various options available to change the colours, the
system chosen is not the most rigorous, but seems to produce surprisingly good results. To create a finished colour 3 colours are
required, the source pixel, a notional main source colour (called pivot in the program) by which each pixel is compared and a target
colour from which the required colour is produced by lightening the target colour. If a widget appears to use a different hue we can
substitute new pivot and target colours - a commented example is included. The 3 colour channels are linearly adjusted based on 
two constant points, if the source was white then the sum of the channels would be 765 and the individual channel of the final colour
would would be 255, the other point we know is that if the source is the same as our pivot colour, then the channel values of the final
colour would be the same as our target colour.

If we look at the scrollbars next, they have components which will change with orientation, so with changes of state there are
quite a few images used. 07pirate_scrollbar.py is the relevant script. I like the images from ubuntu so we can change their colours to
aquamarine and subsititute the coconut tree from pirate_label for the arrows (steppers). The thumb image is a coconut, so there is no
real need for grip. The trough has been copied from elegance, with a colour change, this shows how the trough can be created from an
image. Ubuntu used the trough from the parent theme and changed its colour with a configure command - obviously both approaches are
equally valid, but the image can give more flexibility. Since there are changes to the arrangement compared to the parent theme we will
need a layout, which will need to be copied and changed as appropriate for the other orientation. It is important that the thumb
component has the element "expand" set to True or 1, otherwise the thumb cannot be moved using the mouse - this in turn means that the
thumb will no longer remain circular but becomes oval. Just as it was necessary to set the border limits in pirate_label so thumb needs
to have its border set (try experimenting with a border of 1). An oval coconut is not really what we want, we can keep it circular if
we change the layout slightly - borrowed from the plastik theme - we utilise a thumb and grip, the grip is our coconut and the thumb is
a beach, as in the first script the thumb expands and has differing states, but the grip only changes between vertical and horizontal
orientations. If you want you can uncomment out the third arrow in the layout in this script. The flexibility of the tkinter theme is
shown to its full limits - quite impressive.

Both radio- and check buttons are created in a similar fashion, in that multiple images were created for the various states. All images
need to be the same size.

The widgets notebook and treeview both use sails for their tabs, the adjustment of the border and padding was a little tricky, but
followed along the lines already developed for label. Treeview had used a bordercolor with an alias name, so do not forget to set it
up in the piratz_theme.py.

The button widget is based on the rear view of a sailing ship. This gives us an opportunity to create rather different states from the
normal, where we can use the lights and raise the flag. The vertical border was limited to a few pixels so that the name stays intact. 
An outside dashed line was wanted, which required both configure and layout. These do not work if run as separate clauses, it is best
to run them under a single call to the button class "TButton". This differs from the tcl scripts where configure and layout are run
separately.

The last two are on the face of it not particularly exciting. Check out how a progressbar and scale work in an ordinary theme, or even
a ttktheme, not exactly gripping stuff is it? However with a bit of thought we can "improve" these somewhat. In progressbar the
graphics come from the game funny boat, I'm no artist, so the horizontal progressbar is a pirate ship sailing left to right, all we
need is to detect the value then use this to trigger another state just as the value reaches 100. I am using the "after" universal
widget function that fires after a time delay and calls a customised function which checks on the widget value, if it reaches 100 it
changes the state and the direction flag. When the value reaches 0 it changes back to the original state and direction flag. The states
in element_create and the customised function need compound states that have a negative second state as well as the called state. The
vertical progressbar is slightly more complicated as we have a flapping seagull, therefore we require 3 states, and the negative states
have to include both the other two as negative states apart from the selected state. Run both progressbars in "indeterminate" mode and
make the length the same as your trough image. In the scale widget we have a similar situation but we can use the command property to
trigger our external function, which simplifies matters somewhat, we need only concentrate on obtaining the scale value then trigger
the state changes at pre-determined settings. The horizontal scale not only has several states for the slider but the trough as well.
Ensure that the trough images match up to the slider images by using the correct state. Alright we needed customised functions but I
think it a small price to pay - or else you would need to build customised widgets and that is another ballgame entirely.

Once the widgets have been all tested we can build up piratz_theme.py, we may also require common colours and a common tkfont. When
testing choose a suitable test program, such as 07piratz_notebook - based on 06themed_notebook - put the piratz images in a 
sub-directory and make sure that the script points to your sub-directory (probably "piratz"), the file piratz_theme needs to be on the
same directory as your main program. A few sub-programs have been added to ensure that the progressbar and scale react as expected. The
result will probably make you say "With a little effort I could do better" - good have a go, in general the images are the most time
consuming, but the whole is surprisingly straightforward

## 08 Down to Earth
  ### 08.1 Introduction

As we have seen it is relatively simple to find an image then use this for a widget. What may be more difficult is to design a widget
from scratch. If we use an existing widget as a template, as we did in the previos chapter, we can alter its colours to produce similar
looking widgets. We can use simple drawing tools such as PIL ImageDraw or tkinter Canvas and as all the widgets are quite small more
sophisticated tools might be unnecessary. We are lucky in that we can see what has already been achieved in ttktheme. If we enlarge an
image such as comboarrow-n.png from the Ubuntu theme, we see that the outer border is one pixel wide, there are highlights and shadows
also one pixel wide. The corners are made from a simple angle construction. The most tricky part is probably the arrow, which has a
dark grey outer part and a light grey inner part. Several pixels of varying grey hues surround the arrow and the diagonal lines,
exactly how these were produced will become clearer a little later.

Comparing this widget to others it becomes clear that many of the widgets are made in a similar manner. They are all of a similar size
there are no arcs, all lines are one pixel wide and diagonals are used to give the impression of rounded corners. Angled lines require 
a special antialias treatment to remove their jagged appearance. At present all screens have a rectangular pixel display, which means
that angled lines are displayed within the same limitations which we can see in the following image:-

![lines:grid](/images/08enlargedlines.png)

The vertical and horizontal lines are smooth, but the diagonal lines have been drawn jagged (aliased) and antialiased where
we see that the pixels between the line pixels have an intermediate colour between the line and background colour. You will also 
notice that the diagonal line has a larger spacing between pixel centres than either the vertical or horizontal lines. This means that 
diagonal lines will appear to be slightly lighter with no other change.

There are several approaches we may use to perform antialiasing. The simplest is to draw the image larger then resize to the original
size applying a resampling filter such as bicubic or lanczos (formerly known as antialias in PIL), this creates some differently
coloured pixels as we have already noticed exist in comboarrow-n.png. When applying this to a similar image you will notice that the
antialias pixels might not be as intense as the original image, this is a function of the image layout. The other effect that this
method has is that the colour is leached out of the existing lines, noticeably with the diagonal lines and the ends of the horizontal
and vertical lines, both these effects are unwanted particurly on the diagonal lines where we need to maintain the colour. 

Another promising approach might be to use an application that already has an option to create antialiased lines. We could use
applications such as aggdraw or cv2, unfortunately tkinter canvas has no such option. Testing aggdraw it has the advantage that it
creates antialiased lines as required, so vertical and horizontal lines can be left aliased, the antialiased lines create pixels
similar to those that occurred when the diagonal image was drawn large then reduced with a resampling filter. Unfortunately the colours
are not intense enough, so the effect of antialiasing is lost. The next problem occurred when trying to antialias an arrow, the lines
did not follow the original scheme and the arrow tip increased from one pixel to two pixels wide creating a noticeably worse looking
arrow. 

Using cv2 (cv3) the antialias pixels were more intense in colour but the antialiased line was foreshortened - in fact small lines of 3
or 4 pixels disappeared altogether, which is the critical diagonal size we wish to use. 

We could implement the Xialon Wu antialiasing algorithm, but unfortunately at 45 and its multiples it no longer works. All this means
it is probably best to rethink our antialiasing method.

It will be shown that the corners can be antialiased by drawing the image at a larger size, say nine times as large, then reduce the
image size while applying a resampling filter. The antalias pixel colour has been created by leaching some colour from the diagonals
but we are also compressing arcs into a pixel or two. Unfortunately the arrow has no such aid. If you look at the lines image above,
notice the two parallel lines on the right handside, the green one was drawn ascending the red one descending - see how the lines
follow slightly different paths. We can use a bresenham algorithm to predict the correct path, but most bresenham scripts strictly
follow only one path whichever way they are drawn, the script I managed to find does change with direction but in the opposite manner
to PIL.

  ### 08.2 Drawing with PIL(Pillow)
  
We could used tkinter canvas but the drawing can only be saved as a pdf file. This is not directly useful without conversion to a gif
or png to do this we need to capture the pdf output using PIL, so let's try only using PIL since the drawing is not too complicated
requiring some of the more sophisticated methods available in canvas.

If you have never drawn with PIL or require a refresher the following paragraphs should help. PIL has several modules, the two we
will require are Image and ImageDraw. Image deals with the file whereas ImageDraw gives us the ability to create lines, arcs and
polygons - a bit like tkinter canvas. We draw directly on the image without needing a canvas. After importing the necessary modules,
create a new file, then create a function for drawing. The coordinate system is the normal computer one with the upper left hand
corner being 0,0 (x,y coordinates) x increases across the screen y increases down the screen. Note that all coordinates are given to
the drawing methods as a list (square brackets) [x0,y0,x1,y1 ...] or a list of tuples (round brackets) [(x0,y0),(x1,y1) ...].
```
from PIL import Image, ImageDraw

w = 24  # used to set width
h = 24  # used to set height
transparent = (255,255,255,0) # used to set background colour - using an RGBA format

img = Image.new('RGBA', (w,h), transparent) # create a new image organized with RGBA pixels, 
# of a given size with the set background colour, in this instance transparent
idraw = ImageDraw.Draw(img) # create function for drawing within the new image img.

idraw.line([0,0,w-1,0],fill='black',width=1) # draw line on upper part of the image
idraw.line([0,0,0,h-1],fill='black',width=1) # draw line on left part of the image
idraw.line([w-1,0,w-1,h-1],fill='black',width=1) # draw line on left part of the image
idraw.line([0,h-1,w-1,h-1],fill='black',width=1) # draw line on lower part of the image

img.save('line_test.png') # save to file
```
This should create a square formed from four black lines one pixel wide - we could have used the default values and drawn the lines as
a single line in order. Note that we needed to use the width-1 and height-1 (w-1, h-1), this ensures that the lines fit and are 24
pixels long, since the starting point is zero and our image size is 24x24.

```
idraw.line([0,0,w-1,0,w-1,h-1,0,h-1,0,0]) # alternative method to draw lines, calling line only once
```
Note that we start and finish at the same point (in this case 0,0), also note that the default colour is white. 

If we had used polygon then there normally is no need to close off. Note the outside of the polygon is called outline, fill can be used
as an internal filling method.
```
idraw.polygon([0,0,w-1,0,w-1,h-1,0,h-1],outline='#FFFFFF',fill='red') # the colours specified here are a hash and a named colour
```
We saw that often the widget corners look as though they are rounded, without directly using a curved line, we will need to draw an
arc, ellipse or a pieslice in order to find out how the various corner arrangements came into being maybe on a larger image then
reduce the image in size, this solves the size problem and helps with the antialiasing requirement. 

In order to draw curved lines we need to know the bounding rectangle that defines the size and position of the curve. We can use the
square we drew before and utilise its upper left and lower right points to define the bounding rectangle for a circle - a special case
of the ellipse. Ellipses also use the same methods to colour as used by polygons. PIL is flexible when specifying colours - we can use
RGBA, RGB, hash value, a named colour, or hsl. Be careful when using names it uses the X11 system that is similar to the CSS3, but it
may not always agree with the tkinter list of named colours.
```
idraw.ellipse([0,0,w-1,h-1],outline='red') # not quite right - too small
idraw.ellipse([0,0,w,h],outline='red') # also not right - too big
```
Maybe a case of the Goldilocks size, if h and w had been 23 then the first attempt would have been correct. If we draw a circle it has
a radius that must be an integer, so the bounding square must be an even number of pixels wide and high. The outside black square we 
drew corresponds to the bounding square, not the image size, we see that the circle overlaps the the bounding rectangle on all four
sides, and our case should touch all four sides of the image, in the real world lines have breadth which is why the bounding rectangle
is not a simple dimension, a similar system to canvas as shown in 8.5 Canvas Oval Objects in the tkinter 8.5 documentation.
```
idraw.arc([0,0,w-1,h-1],start=0,end=90,fill='red') # angles are measured from 3 o’clock, increasing clockwise
idraw.arc([0,0,w-1,h-1],start=90,end=180,fill='green') # the colour parameter is fill
idraw.arc([0,0,w-1,h-1],start=180,end=270,fill='yellow')
idraw.arc([0,0,w-1,h-1],start=270,end=360,fill='blue')
```
Note: the arc layouts and how start and end are specified, also the bounding rectangle size for the arc is exactly the same as for the
circle where the arc forms part of that same circle. A similar system is used for pieslice. However pieslice has both an outline and
fill method, just as we saw in ellipse and polygon whereas arc only colours the outside. 

If we wish to produce rounded corners in a large enough size so that curves can be drawn then we will need to enlarge everything,
image size, lines and their widths. Ordinary lines can be directly drawn with their width without too much trouble. Arcs pose a 
problem since they have no width or fill method. Pieslice is the solution, we first draw a larger pieslice that picks up on
the required outside radius, then we draw a smaller pieslice that picks up on the inner radius. The larger pieslice has a colour
corresponding to the borders whilst the smaller pieslice has a background colour. Both pieslices use the same centre.

In the first configuration the two borders run along the outside edges then are joined by an arc of the same width as the borders. 
Let's start a new file:-
```
from PIL import Image, ImageDraw

e = 9  # enlargement
d = (e-1)//2 # displacement
w = 23 # normal image width
h = 23 # normal image height
we = w*e # enlarged image width
he = h*e # enlarged image height
g = 1 # gap
s = g*e # space (enlarged gap)


img = Image.new('RGB', (we,he), 'white') # nothing fancy using an enlarged size
idraw = ImageDraw.Draw(img)

idraw.line([s,0,we-1,0],fill='black',width=e) # draw line on upper part of the image, gap at the upper left
idraw.line([0,s,0,he-1],fill='black',width=e) # draw line on left part of the image, gap at the upper left

img.save('corner_test'+str(g)+'.png') # save to file - seeing what we have drawn in the enlarged size
```
Not quite right, the lines are thick but the full width does not show (magnify until you can see the pixels), therefore we need to
adjust both lines. Wider lines appear to be referenced from a location close to their centre rather than an outside edge. Lines with
odd sized widths use the central measurement less 1, whereas lines with even sized widths use the same size as the previous odd value.
This means that lines of 1 or 2 pixels width need no adjustment whereas wider lines will need either a vertical or horizontal
displacement.

Now we can add a pieslice, using a different colour so we can detect errors a little easier ...
```
idraw.line([s,d,we-1,d],fill='black',width=e) # adjusted for linewidth using d
idraw.line([d,s,d,he-1],fill='black',width=e) # adjusted for linewidth
idraw.pieslice([0,0,16-1,16-1],fill='yellow',outline='yellow') # if alright, change to black and resize
# idraw.pieslice([0,0,16-1,16-1],fill='black',outline='black')

imgx=img.resize((w,h)) # changed the image to our reduced size 
imgx.save('corner_testx'+str(g)+'.png', quality=95) # save to file final size with no resampling filter
# the corner pixels are all black - might be improved with a filter

imgb=img.resize((w,h),Image.BICUBIC) # LANCZOS
imgb.save('corner_testb'+str(g)+'.png', quality=95) # save to file using bicubic filter
```
There is no real space for the filter to get to grips, all it can do is produce very dark greys along the borders, with a lighter grey
at the junction of the 2 lines at 1,1 but this is unlikely to fool most people into believing that we have a rounded corner.

When we enlarge the gap the internal part of the pieslice needs to be taken out with a second pieslice using the same colour as the
background. As the gap increases the pieslice (arc) changes its bounding rectangle not only with increasing pieslice radius but where 
it is centred. It is much easier to control the pieslice, or any of the other regular curved lines using a simple helping function, 
such as create_pieslice. 
```
def create_pieslice(idraw,c,r,outline='#888888',fill='#888888',start=0,end=90):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          outline=outline,fill=fill,start=start,end=end)
```
As we increase the gap size we can see the effects of the resampling filter and compare whether a bicubic or lanczos works better. Also 
check what happens if we use an enlargement factor of 8, in particular on the original size and whether the pieslice marries up with
the border lines and whether this noticeably affects the final image after filtering. As we increase the gap size the final filtered
image at the corner layout changes, a line is drawn diagonally across the gap, first of all just a simple diagonal line then at a gap
of 3 the diagonal has a stepped inward part, at a gap of 4 the line becomes straight, while at a gap of 5 the diagonal becomes stepped
again this time outwards. To aid our investigations each file has a separate name for differing gap sizes. As an exercise it is
instructive to save the reduced image without any filter, then resize this image back to the enlarged size. This should create an
angular image which we can now once again resize but with a lanczos filter the result should be similar to the image created when we
used pieslices, but the antialias pixels will be washed out and the result would not fool many. 

The example file 08corner_investigation.py has collated the above script excerpts. We could alter the script to include an outer border
with the inner border being tied together with the pieslice. This produces similar results to the first script, but is helpful in that
the differences help us to better guess what the original widget looked like. You should look at the differences between combo-n.png
and comboarrow-n.png, apart from image size note that the plain combo has an outer lighter border and that the corner diagonal has no
step, whereas the comboarrow image has a plain border and a stepped diagonal facing outwards. From this information we can now deduce
the gap size and hence the required arc radius. 

![corner:borders](/images/08corners.png) 

The upper row of the corner image shows the result of using various gaps starting on the upper line from 1 and increasing to 5 used on
a simple border, the lower row uses an outer border and the gaps progress from 2 to 6. 

It should be noted that we can create rectangles directly using rectangle, this uses a bounding rectangle, just as we used in pieslice,
and if we use it like pieslice we can create thick rectangles. However what is important is that we can simplify the script
08corner_investigation.py and the following uses principles derived from http://nadiana.com/pil-tutorial-basic-advanced-drawing.
The bounding rectangle helps to compensate for size of the image relative to the rectangle. Let us create a rectangle with rounded
corners, in this instance we shall create an image with diminishing rectangles that start as large as the image, then decrease by 1
pixel times our enlargement factor. At this stage all we need do is determine the rectangle colours, the corners will be dealt with
later. We are going to create 3 rectangles, the outer will be a light colour, the next one darker and the last filled with a
background. Also note that if we only use fill then the rectangle is drawn the same size as if we had used outline - this differs from
tkinter canvas.
```
from PIL import Image, ImageDraw

e = 9 # enlargement
w,h = 16,24
we,he = w*e,h*e

def create_rectangle(size, outer, border, background, width):
    wi,ht = size
    box = 0,0,wi-1,ht-1 # adjust the size of the rectangle to suit the image size
    rect = Image.new('RGBA', (wi, ht), (0, 0, 0, 0))
    draw = ImageDraw.Draw(rect)
    draw.rectangle(box, fill=outer) # The outer rectangle
    draw.rectangle( # The border rectangle
        (box[0] + width, box[1] + width, box[2] - width, box[3] - width),
        fill=border)
    draw.rectangle( # The background rectangle
        (box[0] + 2*width, box[1] + 2*width, box[2] - 2*width, box[3] - 2*width),
        fill=background)
    return rect

inp = create_rectangle((we,he), "lightblue", "blue", 'white', e)
inp.save('rect.png')
```
Apart from the initial size adjustment to the image size, the script has no variable requiring "-1", also we have no need to compensate
for the fact that a line is displaced when it is thick. All we needed to adjust for was the width of the required rectangle. 

The next part is to create the corners, for this we use pieslice as before, but using a small corner image that is pasted in turn on
all four corners. Where the corners are pasted the rectangles are overdrawn, so no immediate adjustment is necessary to the border and
outer rectangles. As before we find it useful to have an assist function so that pieslice is dependant on its centre and radius, rather
than a bounding rectangle. 08rounded_rectangle.py and 08rounded_rectangle_outer.py are the two scripts that we can base many of our 
widget scripts, the first script has the corner running from the outer border, whereas the second script joins the inner border.

  ### 08.3 Simple Gradients and Colour Schemes
  
If you check out some of the widgets, you should be able to detect the use of gradients. Since we are dealing with small images we 
should be able to use gradients based on simple linear interpolation. Keep the colour change simple, otherwise more complex methods
will be needed. The colour representation can be simply an rgb representation, rather than hsv, hsl or cielab. If we take a 
straightforwaed approach we have a starting and finishing colour for each of the separate rgb components. 
```
r,g,b = from_colour
dr = float(to_colour[0] - r)/steps # change of r component
dg = float(to_colour[1] - g)/steps # likewise g
db = float(to_colour[2] - b)/steps # and b
 
for i in range(steps):
    r,g,b = r+dr, g+dg, b+db # first colour in gradient
    idraw.line([x0, y0+i, x0+wi, y0+i], fill=(int(r),int(g),int(b)))
```
The above snippet of code might be found for use on images larger than our widgets, if used as it stands the first colour will be
found to be different to our starting colour. The finishing colour also needs to be processed correctly. This small error becomes more
noticeable as the image becomes smaller.
```
r,g,b = from_colour
dr = float(to_colour[0] - r)/(steps-1) # slightly increase the change to r 
dg = float(to_colour[1] - g)/(steps-1) # likewise g
db = float(to_colour[2] - b)/(steps-1) # and b
r,g,b = r-dr, g-dg, b-db # correction for first colour in gradient
 
for i in range(steps):
    r,g,b = r+dr, g+dg, b+db
    idraw.line([x0, y0+i, x0+wi, y0+i], fill=(int(r),int(g),int(b)))
```
The starting colour has been adjusted so that the first line depicts the right colour, so now we need to ensure that the last line is
on the finishing colour, so the component differences have been enlarged slightly.

We can use an assisting function that produces the required linear interpolation.
```
import numpy as np
white = np.array([255, 255, 255])
my_color = np.array([30, 198, 244])

def lerp(a, b, t):
    return a*(1 - t) + b*t
    
lightened25 = lerp(my_color, white, 0.25)
>>>array([ 86.25, 212.25, 246.75])
```
When using a numpy function the interpolation function lerp is easy to follow, however it may not always be so easy to set all the
information as numpy arrays. For the small sizes we are using the advantages of numpy are not so obvios, therefore I will be
using a different function.
```
def LerpColourRGB(c1,c2,t): # suitable for RGB 
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),
            int(c1[2]+(c2[2]-c1[2])*t))
```
The function is similar to the numpy function, except that the rgb components are treated separately. We have also ensured that the
result is an integer. The line gradient now becomes:-
```
for i in range(steps):
    idraw.line([x0, y0+i, x0+wi, y0+i], fill=LerpColour(from_colour,to_colour,i/(steps-1))
```
All the component differences are being handled in our function - much simpler.

Using the same principal of linear interpolation we can create a more two dimensional look by using a rectangle or an ellipse,
remembering to make allowance for the fact that the figure has width as well as height. This gives the apperance of a radial gradent.
The figure can be drawn off centre allowing us to create a more realistic highlight. We can also create a radial gradient using
points, this has a similar effect when if we were to make the ellipse larger than the required gradient enclosing rectangle - this
creates corners that are filled with the starting colour and the rest having a gradient tending towards the finishing colour.

When creating colour schemes it is best to stick to the following colour guidelines. White, black and grey can be used in any option
to produce gradients if used as end colours. However if grey is produced as an intermediate colour then the gradient normally needs
adjustment. When selecting a colour scheme the normal wheel helps but remember gradients will be created in RGB. 

First option - stick to one hue adjusting the saturation and value - for this the hsv colour space is useful. Neutral colours probably
work best, which means almost anything that is not bright red, orange or yellow. Gradients should be straightforward. Note that the
HSV colour space is related to the RGB colour space in that the HSV hues are the same as the rgb perimeter colours, so red in RGB is
(255,0,0) and this is in HSV (0,100,100), yellow (255,255,0) is (60,100,100), green (0,255,0) is (120,100,100) and so on. You should 
notice that the RGB perimiter colours produce hsv colours with 100 in both saturation and value components.

Second option - use 2 colours - use adjacent colours. 

Third option - use 2 colours - if we use complimentary colours which are exactly opposite in the normal colour wheel. This produces
vibrant colours especially if both have a large saturation. They will automatically produce a warm and a cool colour. Gradients will
be tricky since both colours are used as the end colours, intermediate colours may need to be defined to avoid bad looking gradients.
If you should use the HSV colour scheme it will produce the perimeter rgb colours which will probably not look too clever.

Fourth option - use 3 colours - choosing adjacent colours should look harmonious, it works best if one colour dominates.

Fifth option - uses 3 colours - the colours are evenly spaced around the normal wheel. As with complimentary colours gradients may not
be so straightforward.

Sixth option - use 3 colours - choose one colour then select the adjacent colours to the complimentary colour. This should produce a
toned down complimentary colour scheme. Also be careful of gradients.

The single hue and adjacent hue options can produce pleasing gradients, without too much trouble, however if we have one of the other
options then there could be an unwanted colour produced if the end colours too far apart. Say we have two adjacent colours or only one
value apart then the gradient will transition smoothly, so yellow to green will transition through yellow-green and appear 
satisfactory, however if we tried purple to green then in the RGB colourspace we will see a greyish intermediate colour, whereas HSV
will produce purple-blue, blue, blue-green as intermediate colours. Say we tried to transition between blue and yellow then force the
intermediate colour to be halfway between at green to avoid the grey, additional intermediate colours should make an even better
transition. If you wish to transition with an alpha change only (transparency) then ensure the starting and finishing hue are the
same. 

If you wish to understand what works best in colour schemes it may be helpful to look at the colorspace documentation, 
https://python-colorspace.readthedocs.io/en/latest/ where some relevant points about what is required to help design the colour scheme
for visually impaired people, who represent quite a sizeable proportion of your clients.

  ### 08.4 Replicating the Widget Images
  
We are now in a position to replicate the widget images.  

If we replicate a widget image in the same size we need only need draw lines one pixel wide and place pixels. In this case we would
probably choose PIL as we need only work directly in our chosen png image, and it is simple to change the image format or size. Look at
08combo_new.py, we load matplotlib purely to provide an image of our work, since PIL uses a bmp file to show the image which can have
problems displaying in Windows. There is nothing sophisticated in the programming, create your colour aliases, create the new image
with its background colour, then create the widget background with gradient, create the outer border and corners. The transparent
outer corners are made next, followed by the highlights and shadow then the arrow. Finally we save and display the image. The colours
and sizes are picked up directly from the original drawing. There are no arcs since at this size the results would be most
unsatisfactory. 

In order to make a new widget it would probably be better to work at a much larger size, draw the widget, then save it at the reduced
size. When drawing at larger sizes there is no simple way to maintain the colour without using thick lines, since if we were to use a
single pixel line in our large image, the lines in the final image would have a really washed-out colour. Say we choose a working image
9x as large our lines and corners will all need to be 9 pixels wide. At this level of magnification arcs can be used. PIL ImageDraw
cannot create thick arcs directly without resorting to two pieslices. The problem with tkinter canvas is that we can only save images
as pdf files, which either need to be converted or captured. In this respect PIL is far more flexible, as we have seen we can change
the image size with or without a filter and save directly as a png image. 

When we tested our corners we found that they could be produced with a reasonable antialiasing effect if we made an enlarged image,
then drew the corners with pieslice afterwards reducing the image to the widget size. Using the corners image above we can deduce the
correct gap size and find the closest match to the layout of the image widget. With simple borders no further adjustment should be
necessary where we have an outer border we have to be careful that the darker pixels match our required widget, also check the extreme
top left corner that the layout of the white pixels corresponds to the required widget. Probably the middle corner selection will not
be needed as the widget will be based upon both outer and inner borders being joined.

This leaves the antialiasing on the arrow to be resolved. Our approach is that any antialiasing pixel adjacent to one border pixel
should have half the colour change to those adjacent to two border pixels, there can never be a situation where it is adjacent to three
border pixels. We can treat the arrow and corners as separate entities as they are far enough apart as not to influence each other. If
we draw the arrow in after the image has been resized no arrow colour correction is required. If we can predict where the line will be
drawn it is comparatively simple to establish where the antialising pixels should be. 

Compare 08combo_resize_new.py with 08combo_new.py and judge whether the difference can be seen in the resulting image we can use
08compare_combobox.py to assist. When it comes to creating new widget images either approach is just as valid just use the one that
suits the situation best.

When it comes to new widgets there appears to be only a limited choice what can be achieved. All widgets that can expand produce a line
that grows linearly with no real opportunity to replicate a pattern along the widget - look how the coconut tree grew in size in the
previous chapter. The most intricate parts are pushed to the corners. Any widget with an arrow, such as scrollbar or combo, may lend 
itself to a bit of change. The arrow in Ubuntu is rather bland, just a darker border surrounding a grey fill, in fact most themes use 
this construction. We could base the arrow on the classic arrow with a wider border as we produced in 02scrollbar.py, we should see
an arrow divided into three, where we can use highlights and shadows.

Some widgets could be livened up with a colour gradient. In this respect a colour gradient based on the RGB values is probably
adequate, since we are only altering the colours between similar hues and not across a spectrum. Where we do find gradients they are
mostly a simple gradient which can be copied from 08create_gradient.py, the script creates a button based on button-n.gif used 
by clearlooks. Before using the script the background should be checked to confirm we do have a gradient, as the pixels are found to
be a patchwork of colours. First convert the gif format to RGB for ease of analysis, next each pixel of the background is averaged line
by line and the RGB value printed. When we are satisfied that we are dealing with a gradient then apply 08create_gradient.py. Some 
buttons have more complex gradients, a simple split should cause no real problem, but a highlight is more of a problem, look at the
buttons in elegance and keramik.
