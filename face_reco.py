from clock import end_face_reco
from speak import speak
from data_handle import find_record, mark_present
import face_recognition
import cv2
import os

def face_reco(course, end_time):
    cam = cv2.VideoCapture(0)

    known_face_encodings = [] # keeping face encodings
    known_enrols = [] # keeping enrolment numbers for the given course

    for files in os.scandir(f'data/{course}/images'): # searching images for the given course
        if files.is_file():
            file_face = face_recognition.load_image_file(f'{files.path}')
            known_face_encodings.append(face_recognition.face_encodings(file_face)[0])
            base = os.path.basename(files.path)
            stud_enrol, jpg = os.path.splitext(base)
            known_enrols.append(stud_enrol)

    speak_present = set() # if one name is done don't speak again

    while True: # face recognition continuous

        ret, frame = cam.read()

        rgb_frame = frame[:,:,::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            enr = "UNKNOWN"

            if True in matches:
                first_match_index = matches.index(True)
                enr = known_enrols[first_match_index]

            name = ""

            # if face with unencountered enrolment number is found speak name and mark present
            # mark the face encountered
            if(enr != "UNKNOWN"):
                name = find_record(enr, course)
                if enr not in speak_present:
                    mark_present(course, enr)
                    speak(f"{name} is present!")
                    speak_present.add(enr)
            else: # otherwise UNKNOWN
                name = enr


            # border on face with name at the bottom
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 225, 225), 2)
            cv2.rectangle(frame, (left, bottom-20), (right, bottom), (225, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, name, (left+6, bottom-6), font, 0.5, (0, 0, 0), 1)


        cv2.imshow("Video", frame)

        # if reaches the end time or pressed the 'q':quit key, stop the process.
        if end_face_reco(end_time):
            break
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face_reco("Course_2")