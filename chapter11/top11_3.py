# 1. 클래스 정의 (객체 생성을 위한 설계도)
class Building:
    def __init__(self, address, color):	# 생성자 메서드: 속성 초기화
        self.address = address	# 속성(데이터): 건물의 주소
        self.color = color		# 속성(데이터): 건물의 색상
    def show_info(self):		# 메서드(기능): 건물의 정보를 출력
        print(f"이 건물의 주소는 [{self.address}]이며, 내부 색상은 {self.color}입니다.")

# 2. 건물 객체 생성 (설계도에 따라 건물 짓기)
# 동일한 설계도(Building)를 사용하지만, 서로 다른 실체(객체)가 만들어집니다.
house1 = Building("경상남도 창원시 마산합포구...", "흰색")	# house1: 건물 객체1을 참조하는 변수
house2 = Building("서울특별시 종로구...", "녹색")		# house2: 건물 객체2를 참조하는 변수

# 3. 건물 객체 활용 (참조 변수인 house1, house2를 통해 각 메서드 호출)
print("--- 건물 객체의 정보 확인 ---")
house1.show_info()
house2.show_info()

# 4. 건물 객체의 주소 확인 (id()로 객체의 고유 식별자를 가져와 hex()로 16진수 주소 변환)
print("\n--- 건물 객체의 고유 식별자(ID) 확인 ---")
print(f"house1의 객체 ID: {hex(id(house1))}")
print(f"house2의 객체 ID: {hex(id(house2))}")