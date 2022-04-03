import cv2
  
# Read the input image

i=1

while(i<21):

    image_count=i
    image_name=str(image_count)+".jpg"
    img = cv2.imread(image_name)
    
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        detect_count=1
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        cv2.imshow("face",faces)
        cv2.imwrite("azraakin-"+str(detect_count)+image_name, faces)
        detect_count+=1
    i+=1


