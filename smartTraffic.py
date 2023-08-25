import cv2
# import numpy as np

cap = cv2.VideoCapture('cars0.mp4')
cap1 = cv2.VideoCapture('cars9.mp4')
cap2 = cv2.VideoCapture('cars4.mp4')
cap3 = cv2.VideoCapture('cars10.mp4')
# frame1=cv2.imread('pic3.png')

peak0=0;max0=0
peak1=0;max1=0
peak2=0;max2=0
peak3=0;max3=0

min=10 #min dur
avg=20 #avg dur

dur0=0;dur1=0;dur2=0;dur3=0

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('haarCascadeCARS.xml')
  
read=0
time=0

while True:


    # ----------cap0-----------
    

    ret0, frame0 = cap.read()
    # resize = cv2.resize(frame1, (700, 500))
    if ret0:
        gray = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
        
        cars0 = car_cascade.detectMultiScale(gray, 1.1, 1)
        
        cnt0 = 0

        for (x,y,w,h) in cars0:
            cv2.rectangle(frame0,(x,y),(x+w,y+h),(255,0,0),2)
            cnt0 += 1
        # print(cnt0, " cars found at c1 & prevdur0 is ",dur0)
        
        if dur0>0:
            dur0=dur0-1
            cv2.putText(frame0,'GO %d'%dur0,(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 255, 0),2,cv2.LINE_4)
        else:
            cv2.putText(frame0,'STOP',(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame0,'live_count %d'%cnt0,(20, 70),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame0,'time : %d'%time,(450, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.imshow('video0', frame0)

        wait=1e4
        while wait!=0 :
            wait=wait-1
    else:
        break


    # ----------cap1-----------


    ret1, frame1 = cap1.read()
    # resize = cv2.resize(frame1, (700, 500))
    if ret1:
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

        cars1 = car_cascade.detectMultiScale(gray, 1.1, 1)

        cnt1 = 0

        for (x,y,w,h) in cars1:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)
            cnt1 += 1
        # print(cnt1, " cars found at c1 & prevdur1 is ",dur1)

        if dur0==0 and dur1>0:
            dur1=dur1-1
            cv2.putText(frame1,'GO %d'%dur1,(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 255, 0),2,cv2.LINE_4)
        else:
            cv2.putText(frame1,'STOP',(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame1,'live_count %d'%cnt1,(20, 70),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame1,'time : %d'%time,(450, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.imshow('video1', frame1)

        wait=1e4
        while wait!=0 :
            wait=wait-1
    else:
        break


    # ----------cap2-------------


    ret2, frame2 = cap2.read()
    # resize = cv2.resize(frame2, (700, 500))
    if ret2:
        gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        cars2 = car_cascade.detectMultiScale(gray, 1.1, 1)

        cnt2 = 0

        for (x,y,w,h) in cars2:
            cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,0,0),2)
            cnt2 += 1

        if dur0==0 and dur1==0 and dur2>0:
            dur2=dur2-1    
            cv2.putText(frame2,'GO %d'%dur2,(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 255, 0),2,cv2.LINE_4)
        else:
            cv2.putText(frame2,'STOP',(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame2,'live_count %d'%cnt2,(20, 70),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame2,'time : %d'%time,(450, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.imshow('video2', frame2)

        wait=1e4
        while wait!=0 :
            wait=wait-1
    else:
        break


    # -------------cap3--------------


    ret3, frame3 = cap3.read()
    # resize = cv2.resize(frame3, (700, 500))
    if ret3:    
        gray = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)    
    
        cars3 = car_cascade.detectMultiScale(gray, 1.1, 1)      
        
        cnt3 = 0

        for (x,y,w,h) in cars3:
            cv2.rectangle(frame3,(x,y),(x+w,y+h),(255,0,0),2)
            cnt3 += 1
        

        if dur0==0 and dur1==0 and dur2==0 and dur3>0:
            dur3=dur3-1    
            cv2.putText(frame3,'GO %d'%dur3,(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 255, 0),2,cv2.LINE_4)
        else:
            cv2.putText(frame3,'STOP',(20, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame3,'live_count %d'%cnt3,(20, 70),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.putText(frame3,'time : %d'%time,(450, 35),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 0, 255),2,cv2.LINE_4)
        cv2.imshow('video3', frame3)

        wait=1e4
        while wait!=0 :
            wait=wait-1
    else:
        break

    # Hori1 = np.concatenate((frame1, frame1), axis=1)
    # Hori2 = np.concatenate((frame2, frame3), axis=1)
    # Verti = np.concatenate((Hori1, Hori2), axis=0)    
    # cv2.imshow('VERTICAL', Verti)

    # readings per cycle
    if dur0==0 and dur1==0 and dur2==0 and dur3==0:
        avgcount=(cnt0+cnt1+cnt2+cnt3)/4
        read=read+1
        if max0<=cnt0:
            max0=cnt0
            peak0=time
        if max1<=cnt1:
            max1=cnt1
            peak1=time
        if max2<=cnt2:
            max2=cnt2
            peak2=time
        if max3<=cnt3:
            max3=cnt3
            peak3=time
        dur0=int(min+(cnt0/avgcount)*(avg-min))
        dur1=int(min+(cnt1/avgcount)*(avg-min))
        dur2=int(min+(cnt2/avgcount)*(avg-min))
        dur3=int(min+(cnt3/avgcount)*(avg-min))
        print("\n------- cycle",read,'-------')
        print('dur0 = ',dur0,'| cnt0 = ',cnt0)
        print('dur1 = ',dur1,'| cnt1 = ',cnt1)
        print('dur2 = ',dur2,'| cnt2 = ',cnt2)
        print('dur3 = ',dur3,'| cnt3 = ',cnt3)
        # print(dur0+dur1+dur2+dur3,"\n\n")
    
    time=time+1    
    # ESC to exit
    if cv2.waitKey(33) == 27:
        break

print('\ntotal time :',time)
print('\n------------------')
print('| peak durations |')
print('------------------')

if(peak0>=4*avg):
    print('max. count at way0 =',max0,'at time',peak0-4*avg,'-',peak0,'units')
else:
    print('max. count at way0 =',max0,'at time','N/A -',peak0,'units')

if(peak1>=4*avg):
    print('max. count at way1 =',max1,'at time',peak1-4*avg,'-',peak1,'units')
else:
    print('max. count at way1 =',max1,'at time','N/A -',peak1,'units')

if(peak2>=4*avg):
    print('max. count at way2 =',max2,'at time',peak2-4*avg,'-',peak2,'units')
else:
    print('max. count at way2 =',max2,'at time','N/A -',peak2,'units')

if(peak3>=4*avg):
    print('max. count at way3 =',max3,'at time',peak3-4*avg,'-',peak3,'units')
else:
    print('max. count at way3 =',max3,'at time','N/A -',peak3,'units')
print()

cv2.destroyAllWindows()