Note: the variables quoted here are local variables, so style may be a reference to a widget class or cross-reference

| Command | Effect | 
|--------|------------|
| Style | class used to manipulate the style database |
| configure(*style, query_opt=None,* ***kw*) | query or set the default value of specified option(s) |
| element_create(_elementname, etype, *args, **kw_) | creates a new element in the current theme |
| element_names() | lists elements defined in current theme |
| element_options(*elementname*) | lists the options of elementname |
| layout(*style, layoutspec=None*) | defines the widget layout for a given style |
| lookup(*style, option, state=None, default=None*) | returns value of value specified by option in style |
| map(*style, query_opt=None,* ***kw*) | query or set dynamic states |
| theme_create(*themename, parent=None, settings=None*) | create a new theme |
| theme_names() | lists all known themes |
| theme_settings(*themename, settings*) | temporarily sets the current theme to specified settings |
| theme_use(*themename=None*) | if themename not given returns current theme, else it sets theme|
