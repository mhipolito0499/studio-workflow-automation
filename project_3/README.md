## Project Goals
Address the problem of visualizing the marked shots for reviewers, editorials, etc to use.

## What the script does:
* Processes a given video file to extract specific frames for thumbnail creation. Frames to be extracted
are specified by pulling marked shots stored in MongoDB database from previous project/script (Project 2)
* Prepares an Excel workbook/spreadsheet that contains information about the pulled frames/thumbnail.
The information includes: Folder location, Frame ranges, Timecode of frame relative to video, and middle-most frame for thumbnail.

## Results:
This is an example of how to run the script: <br />
```python .\project3.py --process [video file] --output [provide a name for Excel workbook]```

This is the output/result when running the script: <br />
_(Note: The output specifies if a new thumbnail was generated and provides folder location. If it exists, it will give the folder location)_

```New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_33.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_68.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_122.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_1111.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_1203.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_1212.png] was generated at sub-folder location: ['images']
New image [ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1252.png] was generated at sub-folder location: ['images']
New image [ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1271.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_1302.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel1-partA-1920x1080_5001.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-pickups-shot_1ab-1920x1080_5012.png] was generated at sub-folder location: ['images']
New image [ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1261.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-reel2-partA-1920x1080_301.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-reel2-partA-1920x1080_1112.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-reel2-partA-1920x1080_1401.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-reel2-partA-1920x1080_1406.png] was generated at sub-folder location: ['images']
New image [ddnsata3-production-Avatar-pickups-shot_2ab-1920x1080_1502.png] was generated at sub-folder location: ['images']
New image [ddnsata9-production-Avatar-reel2-VFX-AnimalLogic_1638.png] was generated at sub-folder location: ['images']
New image [ddnsata8-production-Avatar-reel2-VFX-Hydraulx_1800.png] was generated at sub-folder location: ['images']
New image [ddnsata8-production-Avatar-reel2-VFX-Hydraulx_1912.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel2-partB-1920x1080_4556.png] was generated at sub-folder location: ['images']
New image [ddnsata1-production-Avatar-reel2-VFX-Framestore_5123.png] was generated at sub-folder location: ['images']
New image [ddnsata1-production-Avatar-reel2-VFX-Framestore_5467.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-reel3-partA-1920x1080_135.png] was generated at sub-folder location: ['images']
New image [ddnsata4-production-Avatar-reel3-partA-1920x1080_712.png] was generated at sub-folder location: ['images']
New image [ddnsata1-production-Avatar-pickups-shot_3ab-1920x1080_1045.png] was generated at sub-folder location: ['images']
New image [ddnsata1-production-Avatar-pickups-shot_3ab-1920x1080_1167.png] was generated at sub-folder location: ['images']
New image [ddnsata7-production-starwars-reel3-VFX-Hydraulx_3045.png] was generated at sub-folder location: ['images']
New image [ddnsata3-production-Avatar-reel1-partA-1920x1080_201.png] was generated at sub-folder location: ['images']
New image [ddnsata3-production-Avatar-reel1-partA-1920x1080_423.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel5-partA-1920x1080_203.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel5-partA-1920x1080_359.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel5-partA-1920x1080_402.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel5-partA-1920x1080_467.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel5-partA-1920x1080_561.png] was generated at sub-folder location: ['images']
New image [ddnsata2-production-Avatar-reel5-partA-1920x1080_604.png] was generated at sub-folder location: ['images']
New image [ddnsata9-production-Avatar-reel5-VFX-Hydraulx_702.png] was generated at sub-folder location: ['images']
New image [ddnsata5-production-Avatar-reel5-VFX-Framestore_892.png] was generated at sub-folder location: ['images']
New image [ddnsata11-production-Avatar-pickups-shot_5ab-1920x1080_1045.png] was generated at sub-folder location: ['images']
New image [ddnsata6-production-Avatar-reel5-partB-1920x1080_4120.png] was generated at sub-folder location: ['images']
New image [ddnsata6-production-Avatar-reel5-partB-1920x1080_4123.png] was generated at sub-folder location: ['images']
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_33.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_68.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_122.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1111.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1203.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1212.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1252.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1271.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1302.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_5001.png
File exists. Location/name: images/ddnsata4-production-Avatar-pickups-shot_1ab-1920x1080_5012.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_33.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_68.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_122.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1111.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1203.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1212.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1252.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1271.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1302.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_5001.png
File exists. Location/name: images/ddnsata4-production-Avatar-pickups-shot_1ab-1920x1080_5012.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1261.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_33.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_68.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_122.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1111.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1203.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1212.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1252.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1271.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1302.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_5001.png
File exists. Location/name: images/ddnsata4-production-Avatar-pickups-shot_1ab-1920x1080_5012.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1261.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_33.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_68.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_122.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1111.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1203.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1212.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1252.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1271.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1302.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_5001.png
File exists. Location/name: images/ddnsata4-production-Avatar-pickups-shot_1ab-1920x1080_5012.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1261.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_33.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_68.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_122.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1111.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1203.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1212.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1252.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1271.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_1302.png
File exists. Location/name: images/ddnsata5-production-Avatar-reel1-partA-1920x1080_5001.png
File exists. Location/name: images/ddnsata4-production-Avatar-pickups-shot_1ab-1920x1080_5012.png
File exists. Location/name: images/ddnsata7-production-Avatar-reel1-VFX-Hydraulx_1261.png
Thumbnail creation completed.```
