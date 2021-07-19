from data_handle import find_record
import face_recognition
import cv2
import os

def face_reco(course):
    cam = cv2.VideoCapture(0)

    known_face_encodings = [] # keeping face encodings
    known_enrols = [] # keeping enrolment numbers for the given course

    for files in os.scandir(f'data/{course}/images'):
        if files.is_file():
            file_face = face_recognition.load_image_file(f'{files.path}')
            known_face_encodings.append(face_recognition.face_encodings(file_face)[0])
            base = os.path.basename(files.path)
            stud_enrol, jpg = os.path.splitext(base)
            known_enrols.append(stud_enrol)

    while True:
        ret, frame = cam.read()

        rgb_frame = frame[:,:,::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Random"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_enrols[first_match_index]

            if(name != "Random"):
                name = find_record(name, course)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 225, 225), 2)
            cv2.rectangle(frame, (left, bottom-20), (right, bottom), (225, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, name, (left+6, bottom-6), font, 0.5, (0, 0, 0), 1)


        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face_reco("Course_1")