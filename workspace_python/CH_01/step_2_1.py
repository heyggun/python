from pathlib import Path  # pathlib 패키지의 Path 클래스를 불러옴

WORK_DIR = Path(
    __file__
).parent  # 변수 WORK_DIR에 소스 코드의 절대 경로를 저장. Path(__file__)은 파일의 경로를 Path 객체로 저장하고 parent 속성은 현재 파일의 상위 디렉터리를 불러옴
OUT_DIR = (
    WORK_DIR / "output"
)  # 소스 코드의 절대 경로에 'output'을 붙여 변수 OUT_DIR에 저장

if __name__ == "__main__":  # 소스 코드를 최초로 실행하는 경우 if문 이하의 코드 수행
    OUT_DIR.mkdir(
        exist_ok=True
    )  # 함수 mkdir()를 사용해 OUT_DIR 경로에 폴더 생성. OUT_DIR 경로에 동일한 이름의 폴더가 이미 존재하는 경우 오류가 발생할 수 있어, 이를 무시하기 위해 매개변수 exist_ok에 True 전달
