## Project Goals
Expand automating tasks from a post-production facility to a triple-A studio, where multiple facilities are involed.

## What the script does:
* Now accepts user input by using Argparse, a Python library, to handle command line arguments. The user can
specify the files to work with, which makes working with multiple and different files easier. (check import_files for files ingested)
* Stores information to a MongoDB database, as well as calls information from the database.

## Results:
Here is the command-line format to run the script.
```python project_2.py --files "folder_location/Baselight Files" "folder_location/AutoDesk Flame Files" --xytech "Xytech File" --verbose```

Example:
```python project_2.py --files .\import_files\Baselight_JJacobs_20230323.txt .\import_files\Flame_DFlowers_20230323.txt .\import_files\Flame_MFelix_20230323.txt --xytech .\import_files\Xytech_20230323.txt --verbose```

The following is an example when the script is ran:

```---------------Baselight File: -------------------
/ddnsata5/production/Avatar/reel1/partA/1920x1080 32-34    
/ddnsata5/production/Avatar/reel1/partA/1920x1080 67-69    
/ddnsata5/production/Avatar/reel1/partA/1920x1080 122-123  
/ddnsata5/production/Avatar/reel1/partA/1920x1080 155      
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1023     
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1111-1112
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1160
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1201-1205
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1211-1214
/ddnsata7/production/Avatar/reel1/VFX/Hydraulx 1251-1253
/ddnsata7/production/Avatar/reel1/VFX/Hydraulx 1260
/ddnsata7/production/Avatar/reel1/VFX/Hydraulx 1270-1272
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1302-1303
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1310
/ddnsata5/production/Avatar/reel1/partA/1920x1080 1500
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5000-5002
/ddnsata4/production/Avatar/pickups/shot_1ab/1920x1080 5010-5014
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5111
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5122
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5133
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5144
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5155
/ddnsata5/production/Avatar/reel1/partA/1920x1080 5166
/ddnsata3/production/Avatar/reel1/VFX/Framestore 6188-6191
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6200-6201
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6209
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6212
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6219
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6233-6234
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6267
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6269
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6271
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6278
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6282
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6288-6290
/ddnsata5/production/Avatar/reel1/partA/1920x1080 6292-6294
/ddnsata2/production/Avatar/reel1/partB/1920x1080 6409-6411
/ddnsata2/production/Avatar/reel1/partB/1920x1080 6413
/ddnsata2/production/Avatar/reel1/partB/1920x1080 6450
/ddnsata2/production/Avatar/reel1/partB/1920x1080 6666-6668
/ddnsata2/production/Avatar/reel1/partB/1920x1080 6670-6671
/ddnsata2/production/Avatar/reel1/partB/1920x1080 6680-6684
/ddnsata9/production/Avatar/reel1/VFX/AnimalLogic 6832-6834
/ddnsata9/production/Avatar/reel1/VFX/AnimalLogic 6911-6914
/ddnsata2/production/Avatar/reel1/partB/1920x1080 8845
/ddnsata4/production/Avatar/pickups/shot_1ab/1920x1080 10001-10002
/ddnsata4/production/Avatar/pickups/shot_1ab/1920x1080 10008
/ddnsata4/production/Avatar/pickups/shot_1ab/1920x1080 11113
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12011
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12021
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12031
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12041
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12051
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12111
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12121
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12131
/ddnsata2/production/Avatar/reel1/partB/1920x1080 12141

---------------Flame File: -------------------
/ddnsata7/production/Avatar/reel1/VFX/Hydraulx 1260-1262
/ddnsata7/production/Avatar/reel1/VFX/Hydraulx 1267
/ddnsata9/production/Avatar/reel1/VFX/AnimalLogic 2850

---------------Flame File: -------------------
/ddnsata3/production/Avatar/reel1/VFX/Framestore 6195```