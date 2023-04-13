import pandas as pd
import time
import os

read_file=pd.read_csv('학교기본정보_2023년02월28일기준.csv')

while True:
    os.system("tput reset")
    print("찾을수 있는 학교급\t초등학교~고등학교")
    print("찾을 학교의 이름을 입력하세요 \t~~초등학교 등과 같이 입력")
    print("입력 :",end=" ")
    loc_num=-1
    num=-1
    cnt=0
    school_name=input()
    for lat in read_file['학교명']:
        loc_num+=1
        if lat==school_name:
            cnt+=1
            num=loc_num  

    if 1<cnt:       # 중복처리
        os.system("tput reset")
        print("전국에 {}가 2개 이상 있습니다.".format(school_name))
        print("상세 주소를 입력하세요")
        print("주소지 입력 :",end=" ")
        location=input()
        # 입력한 데이터로 재 검색후 값  출력하는기능 만들어야됨
    elif 1==cnt:
        os.system("tput reset")
        print("\t--- {}의 상세정보 ---".format(school_name))
        print(read_file.loc[num])
    else:
        print("검색되지 않는 학교입니다.")


    while True:
        print("계속 검색 하시겠습니까(y/n) : ",end=" ")
        answer=input()
        if answer=="y" or answer=="Y" or answer=="yes" or answer=="YES":
            os.system("tput reset")      # windos os 에선 cls명령
            break
        elif answer=="n" or answer=="N" or answer=="no" or answer=="NO":
            print("종료합니다")
            time.sleep(1)
            exit()
