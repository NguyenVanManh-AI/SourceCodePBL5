import face_recognition
import numpy as np
from datetime import datetime
import pandas as pd

# read encodeListKnow + classnames
df = pd.read_csv('../../../../SaveDir/know_face_encode.csv')
encodeListKnow = list(np.array(df))
dfname = pd.read_csv('../../../../SaveDir/know_face_classnames.csv')
classnames = list(map( lambda x: x[0],  list(np.array(dfname))))
print(classnames)
# read encodeListUnKnow + classnames
dfUnknow = pd.read_csv('../../AnacondaFace/system/SaveDir/face_rasp_recog.csv')
encodeListUnknow = list(np.array(dfUnknow))
# dfnameCorrect = pd.read_csv('../../../../SaveDir/not_know_classnames_correct.csv')
# classnamesCorrect = list(map( lambda x: x[0],  list(np.array(dfnameCorrect))))
# print(classnamesCorrect)

def thamdu(name):
    with open("../../AnacondaFace/system/thamdu.csv", "r+") as f:
        myDatalist = f.readlines()
        nameList = []
        timeList = []
        for line in myDatalist:
            entry = line.split(",")
            nameList.append(entry[0])
            timeList.append(entry[1])

        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{dtstring}")
        else:
            # thay doi thoi gian truoc do thanh thoi gian sau
            indexSearch = nameList.index(name)
            timeList[indexSearch] = datetime.now().strftime("%H:%M:%S")
            if indexSearch != len(timeList)-1:
                timeList[indexSearch] += "\n"
            with open("../../../../thamdu.csv", "w") as f1:
                for name1, time in zip(nameList, timeList):
                    f1.writelines(f"{name1},{time}")

classnames_guess = []

for encodeFaceNotKnow in encodeListUnknow:
    matches = face_recognition.compare_faces(encodeListKnow, encodeFaceNotKnow)
    print(matches)
    faceDis = face_recognition.face_distance(encodeListKnow, encodeFaceNotKnow)
    print(faceDis)
    matchIndex = np.argmin(faceDis)
    if faceDis[matchIndex] < 0.60:
        print(matchIndex)
        name = classnames[matchIndex].upper()
        thamdu(name)
    else:
        name = "UNKNOW"
    classnames_guess.append(name)

dfname_guess = pd.DataFrame(classnames_guess)

# Save the DataFrame to a CSV file
dfname_guess.to_csv("SaveDir/not_know_classnames_guess.csv", index=False)

# # calc hiệu suất của thuật toán
# exactly = 0
# for correct, guess in zip(classnamesCorrect, classnames_guess):
#     print(correct, guess)
#     if guess!='UNKNOW':
#         guess = guess[guess.index('_'):]
#     correct = correct[correct.index('_'):]
#     exactly += 1 if guess.upper()==correct.upper() else 0
# efficiency = exactly/len(classnamesCorrect) *100
# print("efficiency: ", efficiency, "%")
