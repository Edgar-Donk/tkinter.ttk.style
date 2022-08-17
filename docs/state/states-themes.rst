=================
States and Themes
=================

.. figure:: /figures/03themes_states.jpg
   :width: 215px
   :height: 300px
   :align: center

Script 03states_themes.py
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. topic::   Anticipating ttkthemes

   The additional themes from ttkthemescan can be enabled, the standard 
   themes will still be available whether ttkthemescan are enabled or not.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 03states_themes.py

   .. literalinclude:: /examples/03states_themes.py
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

.. raw:: html

   <details>
   <summary><a>Show/Hide <b> Table </b> 03mapped_states.csv </a></summary>

.. csv-table:: 03mapped_states.csv
   :file: /tables/03mapped_states.csv
   :delim: ;
   :header-rows: 1
   :widths: 20, 20, 55,45,25,25

.. raw:: html

   </details>

|
