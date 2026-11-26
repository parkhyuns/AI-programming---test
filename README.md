# AI-programming---test

# 성적 관리 프로그램

 ① 무엇을 하나요 (What)
성적 CSV 파일을 읽어 유효한 점수(0~100점 정수)만 골라내고, 잘못된 형식의 행은 이유와 함께 따로 기록하는 프로그램입니다.

 ② 왜 만들었나요 (Why)
현장의 성적 데이터 파일에는 빈 줄, 공백, 숫자가 아닌 점수, 범위(0~100)를 벗어난 값이나 동명이인이 섞여 있어 단순 반복문으로 읽으면 프로그램이 중간에 멈추거나 데이터가 유실됩니다. 오류 행 때문에 전체 처리를 중단하지 않고 정상 데이터만 안전하게 추출하면서 누락된 행의 원인을 추적하기 위해 만들었습니다.

 ③ 어떻게 쓰나요 (How)
```bash
설치
pip install pytest pytest-cov

실행
python load_scores.py scores.csv

④ 어떻게 테스트하나요Bashpytest test_load_scores.py
======================== test session starts ========================
collected 10 items

test_load_scores.py ..........                                [100%]

======================== 10 passed in 0.03s =========================
⑤ 파일 구성파일하는 일load_scores.py성적 CSV 파일을 읽어 유효한 점수(kept)와 건너뛴 줄 기록(skipped)을 반환하는 핵심 프로그램test_load_scores.py정상·예외·경계값 케이스를 자동으로 검증하는 pytest 단위 테스트 코드scores.csv정상 실행 및 테스트에 사용하는 샘플 성적 데이터 파일empty.csv헤더만 있는 빈 데이터 예외 상황을 확인하기 위한 샘플 파일.gitignore파이썬 캐시(__pycache__), .pytest_cache, 임시 CSV 파일 제외 설정LICENSE오픈소스 이용 허락 조건(MIT License) 명시⑥ 만든 사람 · AI를 어디에 썼는지만든 사람 : (이름 · 학번을 입력하세요)AI를 쓴 곳 : pytest의 @pytest.mark.parametrize 및 tmp_path 문법 작성, 프롬프트 A/B 테스트 비교 실험(test_ai_A.py, test_ai_B.py)내가 직접 판단한 것 : 코드를 보기 전 명세서 6칸을 기준으로 정상·예외·경계값 테스트 케이스를 직접 설계하고, AI가 생성한 테스트 코드 중 명세와 다르거나 버그를 정답으로 고착화한 코드를 판별하여 검증 기준을 확정함
