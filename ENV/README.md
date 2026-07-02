# CV/ML 아나콘다 가상환경 설정 가이드

## OpenMP 충돌(threadpoolctl RuntimeWarning) 방지

`Found Intel OpenMP ('libiomp') and LLVM OpenMP ('libomp') loaded at the same time` 경고는 `conda-forge`와 `defaults` 채널을 함께 쓸 때 자주 발생합니다. `defaults`의 numpy/scipy/scikit-learn은 Intel MKL(libiomp)을 쓰고, `conda-forge`의 opencv 등은 LLVM OpenMP(libomp)를 쓰기 때문입니다. 그래서 이번 `env.yml`은 다음 두 가지로 충돌을 원천 차단합니다.

- **채널을 `conda-forge`로 통일** (`defaults` 채널 사용 안 함)
- **`nomkl` 패키지 포함** → numpy/scipy/scikit-learn이 MKL 대신 OpenBLAS를 쓰도록 강제 → opencv와 동일하게 LLVM OpenMP 계열로 통일

기존에 설치된 환경(`cv-ml-env`)에서 `mkl`, `numpy`, `scipy`만 따로 지우면 그 패키지들에 의존하는 다른 패키지들이 깨지면서 오류가 납니다. **부분 삭제로는 해결되지 않으니, 기존 환경을 완전히 삭제하고 이 yaml로 새로 만드는 것을 권장합니다.**

```bash
conda env remove -n ML_ENV
conda env create -f env.yml
```

## 포함된 패키지

- **python** 3.10
- **numpy** — 수치 연산
- **pandas** — 데이터프레임 처리
- **scikit-learn** — 머신러닝
- **matplotlib** — 시각화
- **seaborn** — 통계 시각화
- **nomkl** — Intel MKL 대신 OpenBLAS를 쓰도록 강제 (OpenMP 충돌 방지용)
- **opencv** — 컴퓨터 비전 (cv2)
- **pillow** — 이미지 입출력
- **jupyterlab / notebook / ipykernel** — 노트북 환경
- **icrawler** — 이미지 크롤링 (pip로 설치, conda 채널에는 없음)

## 설치 방법

1. 이 폴더에 `env.yml`과 `README.md`를 함께 둡니다.
2. 기존에 같은 이름(`ML_ENV`)의 환경이 있다면 먼저 삭제합니다.

```bash
conda env remove -n ML_ENV
```

3. 터미널(Anaconda Prompt)에서 `env.yml`이 있는 경로로 이동한 뒤 아래 명령으로 새로 생성합니다.

```bash
conda env create -f env.yml

conda env create -f env.yml --prefix D:\conda_envs\cv-ml-env
```

4. 환경 생성이 끝나면 활성화합니다.

```bash
conda activate ML_ENV
```

5. 설치가 잘 되었는지 확인하려면:

```bash
python -c "import cv2, sklearn, pandas, seaborn, matplotlib, icrawler; print('모든 패키지 정상 설치')"
```

## 자주 쓰는 명령

| 목적 | 명령 |
|------|------|
| 환경 목록 확인 | `conda env list` |
| 환경 비활성화 | `conda deactivate` |
| 환경 삭제 | `conda env remove -n ML_ENV` |
| 패키지 추가 설치 (conda) | `conda install -n ML_ENV <패키지명>` |
| 패키지 추가 설치 (pip) | `pip install <패키지명>` (환경 활성화 후) |
| Jupyter Lab 실행 | `jupyter lab` (환경 활성화 후) |

## 환경 이름 변경

`env.yml` 맨 위 `name: ML_ENV` 부분을 원하는 이름으로 수정하면 됩니다.

## 참고

- `icrawler`는 conda 채널에서 제공되지 않아 `pip` 섹션에 포함되어 있습니다. conda가 먼저 나머지 패키지를 설치한 뒤, 같은 환경 안에서 pip로 icrawler를 설치합니다.
- 운영체제(Windows/Mac/Linux)에 따라 opencv 빌드 차이로 설치 오류가 날 경우, `opencv` 대신 `pip install opencv-python`으로 대체할 수 있습니다.






----------------------------------------------------------
1. Anaconda Power Shell 열기
2. yml 파일이 있는 폴더 경로로 이동하기
```bash
(base)  >cd yml 파일이 있는 폴더 경로  C:\KDT\VS_KDT_14\ENV
```
3. yml파일로 가상환경 및 패키지 설치하기
```bash
(base)C:\KDT\VS_KDT_14\ENV>conda env remove -n ML_ENV
(base)C:\KDT\VS_KDT_14\ENV>conda env create -f env.yml
```
4. 생성된 가상환경 확인하기
```bash
(base)C:\KDT\VS_KDT_14\ENV>conda env list              # 확인
(ML_ENV)C:\KDT\VS_KDT_14\ENV>conda activate ML_ENV    # 생성된 가상환경
``` 
5. 설치된 패키지 버전 체크 및 VSCODE 가상환경 설정