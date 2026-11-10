# ==============================
#  주제 카드  (6교시)
# ==============================
# 팀 / 이름 : 승&진
# 프로젝트  : 가계부 프로그램 난이도: ★★ 
# 한 문장   : 수입지출을 기록하고 저장 할 수 있는 프로그램
# 필수 기능 : ① 내역 입력  ② 내역 확인  ③ 카테고리별(수입/지출) 합계  ④ 저장
# 쓸 개념   : 클래스 / 딕셔너리 / JSON / datetime


# 1. 메뉴 선택으로 수입, 지출 구분, 내용 입력시에 날짜 같이 자동으로 입력되게
# 2. 가계부 기록 불러오기
# 3. 카테고리(수입/지출로 구분)
# 4. 저장(json)


# 선택 기능
# 1. 메뉴 안에 서브메뉴로 편리성 확보
# 2. 가계부 수정기능
# 3. 월별 지출내역 비교


import json
from datetime import date

FILENAME = "MoneyBook.json"

class Record:
    def __init__(self, kind:str, item:str, amount: int)-> None:
        self.kind = kind
        self.item = item
        self.amount = amount
        self.day = str(date.today())

    def to_dict(self):
        return {"구분": self.kind, "내용": self.item,"금액": self.amount, "날짜": self.day}
        
    def __str__(self) -> str:
        """수입지출 내역 확인"""
        return f"|{self.day}| [{self.kind}] {self.item} : {self.amount:,}원"

class MoneyBook:
    """수입,지출 기록을 위한 공간마련"""
    def __init__(self) -> None:
        self.records: list[Record] = []

    def add_records(self) -> None:
        """수입,지출에 관한 내역을 추가하고 날짜를 기록한다"""
        kind = input("(1.수입 / 2.지출): ").strip()
        if kind == "1":
            kind = "수입"
        elif kind == "2":
            kind = "지출"
        else:
            print()
            print("1 혹은 2를 입력해주세요")
            print()
            return
    
        item = input("내용: ").strip()
        try :
            amount = abs(int(input("금액: ")))
        except ValueError :
            print()
            print("숫자를 입력해주세요")
            print()
            return
            
        self.records.append(Record(kind, item, amount))
        print()
        print(f"[{kind}] {item} : {amount:,}원")
        print()

    def show_records(self) -> None:
        """장부를 한번에 볼 수 있도록 호출"""
        if len(self.records) == 0:
            print()
            print("기록된 내용이 없습니다")
            print()
            return
        for i, r in enumerate(self.records, 1):
            print(f"{i}. {r}")
        print()

    def get_kind(self, kind:str) -> None:
        """수입,지출에 관한 내역을 선택해서 목록과 총액 호출"""
        total = 0
        for r in self.records:
            if r.kind == kind :
                total += r.amount
                print(r)
        print(f"{kind} 총합 : {total:,}원")
        print()

    def get_month(self) -> None:
            """수입,지출에 관한 내역을 조회하고 싶은 연월을 선택해서 목록과 총액 호출"""
            y_m = input("조회할 연도와 달(yyyy-mm) :")
            year_month = ""
            for d in y_m :
                if d in "0123456789":
                    year_month += d
            if len(year_month) != 6:
                print()
                print("잘못 입력하셨습니다")
                print()
                return
                    
            y = year_month[0:4]
            m = year_month[4:]
            if not 1<= int(m) <=12:
                print("1~12월 사이로 입력해주세요")
                print()
                return
            print()

            target_month = f"{y}-{m}"
            month_records = []
            month_total = 0
            for r in self.records:
                if target_month == r.day[:7]:
                    month_records.append(r)
                    if r.kind == "수입":
                        month_total += r.amount
                    elif r.kind == "지출":
                        month_total -= r.amount
                    print(r)
            
            if len(month_records) == 0:
                print("내역이 없습니다.")
                print()
                return

            print(f"=={target_month}== [총합] {month_total:+,}원")
            print()
            
    def revise(self) -> None:
        """기록된 내용을 수정 혹은 삭제"""
        self.show_records()
        try :
            num = int(input("수정/삭제할 번호를 입력해주세요: "))
        except ValueError :
            print("번호를 입력해주세요")
            print()
            return
        if num < 1 or num > len(self.records):
            print("없는 번호입니다")
            print()
            return
        
        record = self.records[num - 1]
        select = input("(1.수정 / 2.삭제): ")
        if select not in ("1","2"):
            print("1 또는 2를 입력해주세요")
            print()
            return
            
        if select == "1" :
            new_kind = input("(1.수입 / 2.지출): ").strip()
            if new_kind == "1":
                new_kind = "수입"
            elif new_kind == "2":
                new_kind = "지출"
            else:
                print("1 혹은 2를 입력해주세요")
                print()
                return
            
            new_item = input("수정할 내용: ").strip()
            try :
                new_amount = abs(int(input("금액: ")))
            except ValueError :
                print("숫자를 입력해주세요")
                print()
                return
            record.kind = new_kind
            record.item = new_item
            record.amount = new_amount
            print(f"수정 완료 : {record}")
            print()

        elif select == "2":
            self.records.remove(record)
            print(f"삭제 완료")
            print()

    def month_diff(self) -> None:
        """월별 수입지출 합계액 비교"""
        today = date.today()
        this_month = f"{today.year}-{today.month:02}"
        y_m = input("조회할 연도와 달(yyyy-mm) :")
        year_month = ""
        for d in y_m :
            if d in "0123456789":
                year_month += d
        if len(year_month) != 6:
            print()
            print("잘못 입력하셨습니다")
            print()
            return
        
        y = year_month[0:4]
        m = year_month[4:]
        if not 1<= int(m) <=12:
            print("1~12월 사이로 입력해주세요")
            return
        
        target_month = f"{y}-{m}"

        if target_month == this_month :
                    print()
                    print("이번 달 입니다")
                    print()
                    return
        
        target_income = 0
        target_expense = 0
        this_income = 0
        this_expense = 0
        
        for r in self.records:
            month = r.day[:7]
            if month == target_month:
                if r.kind == "수입":
                    target_income += r.amount
                elif r.kind == "지출":
                    target_expense += r.amount
            if month == this_month:
                if r.kind == "수입":
                    this_income += r.amount
                elif r.kind == "지출":
                    this_expense += r.amount

        target_total = target_income - target_expense
        this_total = this_income - this_expense

        print()
        print(f"|{target_month}| [수입] {target_income:,} / [지출] {target_expense:,}")
        print(f"|{target_month}| [총합] {target_total:,}원")
        print(f"|{this_month}| [수입] {this_income:,} / [지출] {this_expense:,}")
        print(f"|{this_month}| [총합] {this_total:,}원")
        print()
        print(f"|{target_month}| [대비] {this_total - target_total:+,}원")
        print()
    
    def save(self, filename: str) -> None:
        data = [r.to_dict() for r in self.records]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"{filename} 저장 완료했습니다")
        print()

    def load(self, filename: str) -> None:
        try :
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("파일을 찾을 수 없어 새 장부로 시작합니다")
            print()
            return
        
        except json.JSONDecodeError:
            print("저장 파일이 비어 있거나 손상되어 새 장부로 시작합니다")
            print()
            return
    
        for d in data :
            record = Record(d["구분"], d["내용"], d["금액"])
            record.day = d["날짜"]
            self.records.append(record)
        print("가계부 기록을 불러왔습니다")
        print()

def main():
    book= MoneyBook()
    book.load(FILENAME)
    while True:
        print("="*8,"가계부", "="*8)
        print("1.장부 기입  2.장부 확인")
        print("3.장부 수정  4.장부 저장")
        print("5.월별 비교  q.종료")
        print("=" * 24)
        choice = input("선택: ").strip()
        print()
        if choice == "1":
            book.add_records()
        elif choice == "2":
            print("1.전체 장부 출력")
            print("2.수입 장부 출력")
            print("3.지출 장부 출력")
            print("4.월별 장부 출력")
            select = input("번호를 선택하세요:")
            if select == "1":
                book.show_records()
            elif select =="2":
                book.get_kind("수입")
            elif select == "3":
                book.get_kind("지출")
            elif select == "4":
                book.get_month()

            else :
                print("잘못 입력하셨습니다")
                print()
        elif choice == "3":
            book.revise()
        elif choice == "4":
            book.save(FILENAME)
        elif choice == "5":
            book.month_diff()
        elif choice.lower() in ("q", "ㅂ"):
            break
        else:
            print("잘못 입력하셨습니다")
            print()
        

if __name__ == "__main__":
    main()