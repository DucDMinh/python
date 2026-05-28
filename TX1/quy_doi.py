import ty_gia

def quy_doi(tien):
    ket_qua = {
        "USD": tien / ty_gia.USD,
        "EUR": tien / ty_gia.EUR,
        "JPY": tien / ty_gia.JPY
    }
    return ket_qua