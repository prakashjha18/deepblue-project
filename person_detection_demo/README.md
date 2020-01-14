# About the code

The code will give approximate number of persons in the frames.

Over-Crowding is one of the major reason in an hospital and thus identifying crowd densities at a particular time will prove useful for patient satisfaction.

The code uses feature matching in open-cv to achieve it.

# Run

You will need to install additional libraries - ` imutils, numpy, cv2 `

You can download the test video.

Just copy and run the code in your ide.

The code will give output of no. of persons in every frame in `peron_log.txt` file which will be created automatically

### Note

un-comment the lines for live video output--->(they are commented as `cv2.imshow()` does not run on Google Colab)
```
cv2.imshow("Before NMS", orig)

cv2.imshow("After NMS", image)
```
