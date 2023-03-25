import cv2 

img = cv2.imread(r'C:\Users\Win10\Desktop\InterFace\Images\img1.jpg')
print(img)
pixsel = img.size 
dimesions = img.shape 
# cv2.imshow('hamza',img)
# print("this picture has ".capitalize() + str(pixsel )+ " pixsels ".capitalize())
# cv2.waitKey(0)

# # changing the size of  img 
# new_img = cv2.resize(img , (200,600))
# cv2.imshow('hamza',new_img)
# cv2.waitKey(0)

gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('hamza',gray)
# cv2.waitKey(0)

# cv2.imshow('hamza',img)
# k = cv2.waitKey(0)
# if k == ord('q') :
#     cv2.destroyAllWindows()
# elif k == ord('S') :
#     cv2.imwrite(r'C:\Users\Win10\Desktop\InterFace\Images\img2.jpg', gray)
#     cv2.destroyAllWindows()

# cv2.line(img , (300,20) , (20,300) ,(0,255,0) ,4)
# cv2.imshow('hamza',img)
# cv2.waitKey(0)

cv2.putText(img ,"person" , (200,30) , cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0,0) , 2)
cv2.imshow('hn',img)
cv2.waitKey(0)



