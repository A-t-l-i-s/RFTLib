import cv2
from RFTLib.Camera import *







if (__name__=="__main__"):
	cap=Webcam("192.168.1.180",9999,"Atlis","6013")
	vir=VirtualCamera(1920,1080,60)



	while cap.running:
		result,frame=cap.readVideo()

		if (result):
			frame=cv2.resize(frame,(vir.width,vir.height))
			frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)


			vir.data=frame
			vir.wait()




