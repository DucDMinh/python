import quy_doi

def main():
    try:
        so_dam_bay = float(input("Nhap so dam bay: "))
        so_tien_VND = float(input("Nhap so tien VND: "))
        tong_tien = so_tien_VND * so_dam_bay
        print(f"Tổng số tiền phải trả bằng VNĐ: {tong_tien}")
        print("-" * 40)
        tien_quy_doi = quy_doi.quy_doi(tong_tien)
        print("QUY ĐỔI RA NGOẠI TỆ:")
        print(f"USD (Đô la Mỹ) : {tien_quy_doi['USD']:,.2f} $")
        print(f"EUR (Euro)     : {tien_quy_doi['EUR']:,.2f} €")
        print(f"JPY (Yên Nhật) : {tien_quy_doi['JPY']:,.2f} ¥")
    except ValueError:
        print("Khong hop le")

if __name__ == "__main__":
    main()