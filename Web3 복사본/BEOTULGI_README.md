# 비틀기: Unseen Creators 프로젝트 가이드

## 파일 구조

```
Web3/
├── beotulgi.html          # 메인 HTML 파일
├── assets/
│   ├── staff/            # 스태프 이미지 파일들
│   │   ├── staff_1.jpg
│   │   ├── staff_2.jpg
│   │   ├── staff_3.jpg
│   │   └── ...
│   └── models/           # 3D 모델 파일
│       └── face.obj      # 얼굴 3D 모델 (선택사항)
```

## ⚠️ 중요: 실행 방법

**이 프로젝트는 반드시 로컬 서버를 통해 실행해야 합니다!**

HTML 파일을 직접 열면 CORS 정책 때문에 이미지를 로드할 수 없습니다.

### 로컬 서버 실행 방법

터미널에서 프로젝트 폴더로 이동한 후:

```bash
cd /Users/bangseoyeon/Desktop/CD2/P2/Web3
python3 -m http.server 8000
```

그 다음 브라우저에서 다음 주소로 접속:
```
http://localhost:8000/beotulgi.html
```

또는 Node.js가 설치되어 있다면:
```bash
npx serve
```

## 사용 방법

### 1. 스태프 이미지 추가
- `assets/staff/` 폴더에 `staff_1.jpg`, `staff_2.jpg`, `staff_3.jpg` 등의 이름으로 이미지 파일을 추가하세요.
- 코드에서 자동으로 랜덤하게 각 조각에 매핑됩니다.
- 이미지가 없어도 기본 색상 타일로 대체됩니다.

### 2. 3D 얼굴 모델 추가 (선택사항)
- `assets/models/face.obj` 파일을 추가하면 실제 얼굴 굴곡에 맞춰 조각이 배치됩니다.
- OBJ 파일이 없으면 기본 구체(Sphere) 형태로 작동합니다.
- OBJ 파일은 Three.js의 OBJLoader로 로드됩니다.

### 3. 기능 설명

#### 이미지 맵핑
- 각 조각은 `assets/staff/` 폴더의 이미지를 랜덤하게 사용합니다.
- 이미지 로드 실패 시 자동으로 색상 타일로 대체됩니다.

#### 3D 모델 적용
- `face.obj` 파일이 있으면 그 지오메트리를 기반으로 조각이 배치됩니다.
- 없으면 기본 구체를 사용합니다.

#### 호버 애니메이션
- 마우스를 조각 위에 올리면:
  - 조각이 앞으로 살짝 튀어나옵니다
  - 반짝이는 효과가 나타납니다

#### 확대 효과
- 조각을 클릭하면:
  - 카메라가 해당 조각으로 부드럽게 줌인됩니다
  - 우측에 정보 패널이 표시됩니다
  - "닫기" 버튼을 누르면 원래 위치로 복귀합니다

## 커스터마이징

### 스태프 이미지 파일명 변경
`beotulgi.html` 파일의 다음 부분을 수정하세요:
```javascript
const staffImageFiles = [
    'staff_1.jpg', 'staff_2.jpg', 'staff_3.jpg', ...
];
```

### 조각 개수 조정
조각 생성 부분의 `i += 5` 값을 변경하면 조각 밀도를 조절할 수 있습니다:
```javascript
for (let i = 0; i < positions.count; i += 5) { // 숫자를 줄이면 조각이 많아집니다
```

### 애니메이션 속도 조정
- 호버 애니메이션: `tile.userData.hoverOffset += (tile.userData.hoverTarget - tile.userData.hoverOffset) * 0.2;`의 `0.2` 값을 변경
- 줌인 속도: `const duration = 1000;` 값을 변경 (밀리초 단위)

## 브라우저 호환성
- Three.js 0.160.0 사용
- ES6 모듈 지원 브라우저 필요
- WebGL 지원 필요

