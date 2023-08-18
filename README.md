# Bad Apple Projection
 
This is the simple code for creating a projection of the [Bad Apple video](https://www.youtube.com/watch?v=FtutLA63Cp8&ab_channel=kasidid2) on an image with distinct cells, in this case a map of the counties of the United States. More generally however, this base code can be used to project any video onto any base image that has distinct cells (where the pixels can be projected) that are white and bordered in black. 

To run, just modify the source video name in the [frames.py](/frames.py#L25) script, and then running the file to render each frame of the video. Then, specify the base image, as well as the resizing properties for the video overlay, in the [main](/main.py#L4) file, and then run this script to create the output video's frames.
