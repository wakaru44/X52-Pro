# Installation of X52 Pro Elite Control scheme.

 * Download the .pr0 and .binds file by clicking the green ```"Clone or download" button and select "Download Zip"```.
  
 * Once the zip has been downloaded, Extract the files to a Folder of your chosing (Like the desktop).
  
 * Open ````"X52ProEliteV223.pr0"``` in the software then save it to ```"C:\Users\Public\Documents\SmartTechnology Profiles"```.
  
 * "X52ProElite v2.2.3.1.8.binds" needs to be copy & pasted into ```"C:\Users\<yourname>\AppData\Local\Frontier Developments\Elite Dangerous\Options\Bindings"```.
    * It will show up in the 'Controls' drop down ingame as ```"X52ProElite v2.2.3"```.

# Using the tool to deploy and collect files

If you have already python and make, nothing to worry about, just run `make deploy` and `make collect`. 

If you don't have python, install it and put it in the path, or install it and modify the Makefile with the path to your python.exe

If you don't want to use make, check the Makefile on how to run the script and just do that.


# GOTchas when editing profiles

- the tool is shit. sorry, there is no way to put it softer. is just really bad. having said that, amazing people can get amazing results with it. I struggled.

- If you have a custom keyboard layout, there might be some issues with key mappings. with a custom keyboard layout, like Dvorak, you fucked. 
    - Change your layout during game to en_us, to have all the shortcuts function as expected.
    - And when you are editing the profile, make sure you also have the layout in en_us.
    - The profile will assign the _hardware key_ (not the actual symbol on the key) to the mapping. Which will make custom layouts flip.

- Start by changing the view mode, to Grid (So you can see all 6 modes at once, without the picture of the HOTAS)

- If you change 1 setting, in 1 of the modes, the other 3 will change too.

- If you want to change a setting, is better to do it first in the profile editor. 
  
    - If you want to change a setting that already has a button, and is assigned in ED, change it in the profile.
    - *NOTE:* If the setting alreay exists, change it by _right click_ on the field, instead of typing yourself.
      When you type yourself, it will mess the linked modes and what not. FFFFFFFFfff*¿/%?$)k

    - if it doesn't exist yet, add a key combination there. then go to E:D

- 

