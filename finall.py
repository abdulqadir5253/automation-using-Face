import cv2,time
import numpy as np

#setting font for puttext
font=cv2.FONT_HERSHEY_SIMPLEX

#loading and reading data from the saved training files
face_data=np.load('training_faces.npy')
labels=np.load('training_labels.npy')

#creating recognizer
recognizer=cv2.face.LBPHFaceRecognizer_create()

#training the recognizer
recognizer.train(face_data,np.array(labels))

#flag for the detected face
detected=0
#cascading
cascade=cv2.CascadeClassifier('face.xml')
# opening camera
cam=cv2.VideoCapture(0)
while cam.isOpened():
    # reading frame
    frame=cam.read()[1]
    #converting frame to gray 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    
    for (x,y,w,h) in faces:
        #drawing rectangle on the faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        
        #predicting the label and confidence
        label,confidence=recognizer.predict(gray_frame[y:y+h,x:x+w])
        print("confidence "+ str(confidence))        
        #checking for confidence (the lower the confidence the more accurate the prediction is)
        if confidence<50:
            msg="Face Detected"
            
            #printing the message 
            cv2.putText(frame,msg,(20,50),font,1,(255,255,255),3,cv2.LINE_AA)
            
            #changing flag to 1
            detected=1
    cv2.imshow('live',frame)

    #handler
    if cv2.waitKey(2) & 0xFF == ord('q'):		
        break
    elif cv2.waitKey(2) & detected==1:
        time.sleep(0.5)
        break
cv2.destroyAllWindows()
cam.release()

if detected == 1:
    
    from selenium import webdriver 
    from time import sleep 

    usr="abdul5152@ymail.com"
    pwd="m8963859920"

    #opening Firefox
    driver = webdriver.Firefox() 

    #going to page Facebook
    driver.get('https://www.facebook.com/') 
    print ("Opened facebook") 
    sleep(1) 

    #entering email id
    username_box = driver.find_element_by_id('email') 
    username_box.send_keys(usr) 
    print ("Email Id entered") 
    sleep(1) 

    #entering password
    password_box = driver.find_element_by_id('pass') 
    password_box.send_keys(pwd) 
    print ("Password entered") 


    #Logging you inss
    login_box = driver.find_element_by_id('loginbutton') 
    login_box.click() 

    #Print done in terminal when user is logged in successfully
    print ("Done") 

    #press any word in terminal to quit
    input('Press anything to quit ') 
    print()
    driver.quit() 
    print("Finished") 

if detected == 0:
    print("hi")
    