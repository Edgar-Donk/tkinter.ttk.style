
| Widget | Class Name | mapped states alt | mapped states clam |mapped states classic |mapped states default |
|--------|:------------:|:------------:|:------------:|:------------:|:------------:|
| Common | "." | disabled, active | disabled, active, !focus |disabled, active, focus |disabled, active |
| Button	  | TButton	  | {pressed !disabled}, {active !disabled}, alternate| disabled, pressed, active, alternate|{!disabled pressed}|{!disabled pressed}|
| Checkbutton	| TCheckbutton| disabled, pressed| disabled, pressed|pressed, selected|pressed, selected|
| Combobox	  | TCombobox	| readonly, disabled|active, pressed, {readonly focus}|readonly, disabled|readonly, disabled|
| Entry	      | TEntry	| readonly, disabled| readonly, focus|readonly, disabled|readonly, disabled|
| Notebook	| TNotebook.Tab	| selected |selected |selected |selected |
| Radiobutton	| TRadiobutton		| disabled, pressed | disabled, pressed|pressed, selected|pressed, selected|
| Scale	| TScale		| | |{pressed !disabled}|
| Scrollbar	| TScrollbar | | |{pressed !disabled}| disabled|
| Treeview	| Treeview	| selected  | selected  |selected |selected |
