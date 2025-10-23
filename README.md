# PC
PC scripts and tools

# Running the Scripts

# copy-timestamp.ps1
1. In File Explorer, navigate to your user directory, usually C:\Users\<YourUsername>, then AppData\Roaming\Microsoft\Windows\Start Menu\Programs
Note: you can use %AppData% as a shortcut to C:\Users\<YourUsername>\AppData\Roaming
2. Create a new folder named "Shortcuts"
3. Inside that folder, right click > New > Shortcut
4. For "Location", enter:
`powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "C:\Scripts\copy-timestamp.ps1"`
(change the path of the script as needed - make sure the script is present there!)
5. Name it something like "Copy Timestamp"
6. Right click the shortcut > Properties
7. Under Shortcut key, choose something like Ctrl + Alt + T (unused by Windows and most apps)
8. You may have to restart File Explorer for the changes to take effect but try it first. There may be a slight delay but you should see the script window pop up for a second. 
Note: You can use Ctrl + Shift + Esc to open Task Manager faster! Then just right click "Windows Explorer" > Restart. Likely unnecessary.