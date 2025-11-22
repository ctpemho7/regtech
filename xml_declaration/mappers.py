""" Пример заполнения классов """
from ESADout_CU import DocumentID as ESADout_CU_DocumentID, CustomsProcedure, CustomsModeCode, ElectronicDocumentSign, RecipientCountryCode, EECEDocHeaderAddInfo, ESADout_CU

def fill_ESADout_CU_with_gt(
        document_id_str="C3311921-1FCD-42FB-B038-1786E96F85DE",
        g1_1= "ИМ",
        g1_2= "40",
        g1_3= "ЭД",
        
):
    
    def fill_goods_shipment_with_gt():
        pass


    # Создание объекта с данными
    document_id = ESADout_CU_DocumentID(document_id_str)
    customs_procedure = CustomsProcedure(g1_1)
    customs_mode_code = CustomsModeCode(g1_2)
    electronic_document_sign = ElectronicDocumentSign(g1_3)
    recipient_country_code = RecipientCountryCode("RU")

    # не уверен, что он генерируется так
    ece_doc_header_add_info = EECEDocHeaderAddInfo(
        e_doc_code="R.036",
        e_doc_date_time="2025-04-22T12:58:00",
        language_code="RU",
        source_country_code="RU",
        destination_country_code="RU"
    )

    esa_dout_cu = ESADout_CU(
        document_mode_id="1006058E",
        document_id=document_id,
        customs_procedure = customs_procedure,
        customs_mode_code = customs_mode_code,
        electronic_document_sign = electronic_document_sign,
        recipient_country_code = recipient_country_code,
        ece_doc_header_add_info = ece_doc_header_add_info,
        goods_shipment = fill_goods_shipment_with_gt(),
        # filled_person = get_filled_person(),
        # customs_representative=get_CUESADCustomsRepresentative(),
    )
    return esa_dout_cu


if __name__ == "__main__":

######  1 — ДЕКЛАРАЦИЯ

    ### g1_1 = st.text_input("1.1 — Вид ТП", value=default_kind_TP, label_visibility="collapsed")
    ### g1_2 = st.text_input("1.2 — Код ТП", value=default_code_TP, label_visibility="collapsed")
    ### g1_3 = st.text_input("1.3 — Электронное", value="ЭД", label_visibility="collapsed") #По умолчанию
    g1_1 = "ИМ"
    g1_2 = "40"
    g1_3 = "ЭД"
###### 8 — Получатель - скип по причине надо доработать 
    g8_1 = "" # st.text_input("8.1 — ИНН",
    g8_2 = "" # st.text_input("8.2 — КПП",
    g8_3 = "" # st.text_input("8.3 — Наименование",
    g8_5 = "" # st.text_input("8.5 — Страна",
    g8_4 = "" # st.text_input("8.4 — Код страны",
    g8_6 = "" # st.text_input("8.6 — Индекс", 
    g8_7 = "" # st.text_input("8.7 — Город", 
    g8_8 = "" # st.text_input("8.8 — Улица, дом",                                  
    g8_9 = "" # st.text_input("8.9 — Дом",                                  
    g8_10 ="" #  st.text_input("8.10 — ОГРН", 

###### 9 — Лицо, ответственное за финансовое урегулирование
    g9_1 = "" # st.text_input("9.1 — ИНН",
    g9_2 = "" # st.text_input("9.2 — КПП",
    g9_3 = "" # st.text_input("9.3 — Наименование",
    g9_5 = "" # st.text_input("9.5 — Страна",
    g9_4 = "" # st.text_input("9.4 — Код страны",
    g9_6 = "" # st.text_input("9.6 — Индекс", 
    g9_7 = "" # st.text_input("9.7 — Город",
    g9_8 = "" # st.text_input("9.8 — Улица",
    g9_9 = "" # st.text_input("9.9 — Дом",
    g9_10 = "" # st.text_input("9.10 — ОГРН", 

###### 14 — Декларант
    g14_1 = "" # st.text_input("14.1 — ИНН",
    g14_2 = "" # st.text_input("14.2 — КПП",
    g14_3 = "" # st.text_input("14.3 — Наименование",
    g14_5 = "" # st.text_input("14.5 — Страна", 
    g14_4 = "" # st.text_input("14.4 — Код страны",
    g14_6 = "" # st.text_input("14.6 — Индекс", 
    g14_7 = "" # st.text_input("14.7 — Город",
    g14_8 = "" # st.text_input("14.8 — Улица",
    g14_9 = "" # st.text_input("14.10 — Дом",
    g14_10 = "" # st.text_input("14.10 — ОГРН", 


###### 12 — Общая таможенная стоимость")
    g12_1 = "" # st.text_input("12.1 — Сумма", value=get_total_sum_rub(all_data), label_visibility="collapsed")

###### 11 — Торг. страна")
    g11_1 = "" # st.text_input("11.1 — Код страны", value=g2_4, label_visibility="collapsed")

###### 15 — Код и наименование страны отпр./эксп.")
    g15_1 = "" # st.text_input("15.1 — Код", value=get_country_code(g15_2), label_visibility="collapsed")
    g15_2 = "" # st.text_input("15.2 — Страна", value=normalize_country(get_any(all_data, [
        
###### 17 — Код и наименование страны назначения !Доделать коносамент")
    g17_2 = "" # st.text_input("17.2 — Страна", value=normalize_country(get_any(all_data, [
    g17_1 = "" # st.text_input("17.1 — Код", value=get_country_code(g17_2), label_visibility="collapsed")

###### 16 — Код и наименование страны происхождения")
    g16_2 = "" # st.text_input("16.2 — Страна", value=default_g16_2, label_visibility="collapsed")
    g16_1 = "" # st.text_input("16.1 — Код", value=default_g16_1, label_visibility="collapsed")

###### 18 — Идентификация и страна регистрации трансп.средства при отправлении/прибытии")
    g18_1 = "" #st.text_input("18.1 — Количество", value="", label_visibility="collapsed")
    g18_2 = "" #st.text_input("18.2 — Номера ТС (через ; прицеп через /)", value="", label_visibility="collapsed")
    g18_3 = "" #st.text_input("18.3 — Код страны регистрации ТС", value="", label_visibility="collapsed")
        
###### 21 — Идентификация и страна регистрации активного трансп.средства на границе")
    g21_1 = "" #st.text_input("21.1 — Количество", value=get_transport(all_data)[0], label_visibility="collapsed")
    g21_2 = "" #st.text_input("21.2 — Номера ТС (через ; прицеп через /)", value=get_transport(all_data)[1], label_visibility="collapsed")
    g21_3 = "" #st.text_input("21.3 — Код страны регистрации ТС", value=get_transport(all_data)[2], label_visibility="collapsed")

###### 19 — Конт.
    g19_1 = "" #st.text_input("19 — Бинарная", value = "1", label_visibility="collapsed") 


###### 20 Условия поставки")
    g20_2 = "" # st.text_input("20.2 — Место", value=get_incoterms(get_any(all_data, [
    g20_1 = "" # st.text_input("20.1 — Код инкотермс", value=get_incoterms(get_any(all_data, [
    g20_3 = "" # st.text_input("20.3 ЛЭП", label_visibility="collapsed") 

###### 22 — Валюта и общая сумма по счету")
    g22_1 = "" # st.text_input("22.1 — Валюта", value=get_currency(all_data), label_visibility="collapsed") 
    g22_2 = "" # st.text_input("22.2 — Сумма по инвойсу", value=get_total_sum_invoice(all_data), label_visibility="collapsed") 

###### 26 — Вид транспорта внутри страны")
    g26_1 = "" # st.text_input("26.1 — Код", value = "", label_visibility="collapsed") 

###### 23 — Курс валюты")
    g23_1 = "" # st.text_input("23.1 — Курс", value=cb_rate(date_declaration, get_currency(all_data)), label_visibility="collapsed") 

###### 24 — Характер сделки")
    g24_1 = "" # st.text_input("24.1 — Код характера сделки", value = "010", label_visibility="collapsed") 
    g24_2 = "" # st.text_input("24.2 — Код особенности сделки", value = nature_transaction(all_data), label_visibility="collapsed") 

###### 25 — Вид транспорта на границе")
    g25_1 = "" # st.text_input("25.1 — Код", value = get_transport_type(all_data, g21_2), label_visibility="collapsed") 


###### 30 - Местонахождение товаров")
    g30_1 = "" # st.text_input("30.1 — Код", value = "11", label_visibility="collapsed")
    g30_2 = "" # st.text_input("30.2 — Код таможенного органа", 
    g30_2 = "" # st.text_input("30.2 — Адрес", value = svh["Адрес"], label_visibility="collapsed")
    g30_3 = "" # st.text_input("30.3 — Номер лицензии", value = svh["Лицензия"].split("действует")[0], label_visibility="collapsed")
    g30_4 = "" # st.text_input("30.4 — Срок лицензии", value = svh["Лицензия"].split("действует")[1], label_visibility="collapsed")


###### 29 - Орган въезда/выезда")
    g29_1 = "" # st.text_input("29.1 — Код", value = g30_2, label_visibility="collapsed") 
    g29_2 = "" # st.text_input("29.2 — Остальная информация", value = svh_name, label_visibility="collapsed") 


###### 31 - Маркировка и кол. -Номера конт. - Кол. и отлич. особенности")
    g31_1 = "" # st.text_area("31.1 — Наименование, характеристики", value = "")
    g31_2 = "" # st.text_area("31.2 — Дополнение", value = "", label_visibility="collapsed")
    g31_3 = "" # st.text_input("31.3 - Количество", value = "", label_visibility="collapsed")
    g31_4 = "" # st.text_input("31.4 - Наименование единицы измерения", value = "", label_visibility="collapsed")
    g31_5 = "" # st.text_input("31.5 - Код единицы измерения", value = "", label_visibility="collapsed")
    g31_6 = "" # st.text_input("31.6 - Количество", value = "", label_visibility="collapsed")
    g31_7 = "" # st.text_input("31.7 - Наименование единицы измерения", value = "", label_visibility="collapsed")
    g31_8 = "" # st.text_input("31.8 - Код единицы измерения", value = "", label_visibility="collapsed")
    g31_9 = ""  #st.text_input("###### 31.9 - Регистрационный номер ОИС",value = "", label_visibility="collapsed")
    g31_10 = "" # st.text_input("###### 31.10 - Сведения о месторождении",value = "", label_visibility="collapsed")
    g31_11 = "" # st.text_input("31.11 - Общее кол-во мест", value = "", label_visibility="collapsed")
    g31_12 = "" # st.text_input("31.12 - Общее кол-во мест занимаемых частично", value = "", label_visibility="collapsed")
    g31_13 = "" # st.text_input("31.13 - Код наличия упаковки", value = "", label_visibility="collapsed")
    g31_14 = "" # st.text_input("31.14 - Вид грузю места", value = "", label_visibility="collapsed")
    g31_15 = "" # st.text_input("31.15 - Сведения о поддонах",value = "", label_visibility="collapsed")
    g31_16 = "" # st.text_input("31.16 - Сведения об индивидуальной таре",value = "", label_visibility="collapsed")
    g31_17 = "" # st.text_input("31.17 - Номера контейнеров",value = "", label_visibility="collapsed")
    g31_18 = "" # st.text_input("31.18 - Сведения об акцизах",value = "", label_visibility="collapsed")
    g31_19 = "" # st.text_input("31.19 - Сведения об условиях доставки",value = "", label_visibility="collapsed")
    g31_20 = "" # st.text_input("31.20 - Сведения о переработке",value = "", label_visibility="collapsed")
    g31_21 = "" # st.text_input("31.21 - Дата начала периода", value = "", label_visibility="collapsed")
    g31_22 = "" # st.text_input("31.22 - Дата окончания периода", value = "", label_visibility="collapsed")
    g31_23 = "" # st.text_input("31.23 - Количество нефтепродуктов", value = "", label_visibility="collapsed")
    g31_24 = "" # st.text_input("31.24 - Единицы измерения", value = "", label_visibility="collapsed")
    g31_25 = "" # st.text_input("31.25 - Сведения об электроенергии" , value = "", label_visibility="collapsed")
    g31_26 = "" # st.text_input("31.26 - Нанесенные контрольные знаки", value = "", label_visibility="collapsed")
    g31_27 = "" # st.text_input("31.27 - Количество нанесенных знаков", value = "", label_visibility="collapsed")
    g31_28 = "" # st.text_input("31.28 - Сведения о нанесенных знаках", value = "", label_visibility="collapsed")
    g31_29 = "" # st.text_input("31.29 - Признак нанесения идентификации", value = "", label_visibility="collapsed")
    g31_30 = "" # st.text_input("31.30 - Количество кодов идентификации", value = "", label_visibility="collapsed")
    g31_31 = "" # st.text_input("31.31 - Сведения о средствах идентификации", value = "", label_visibility="collapsed")
    g31_32 = "" # st.text_input("31.32 - Страна назначения при периодическом декларировании", value = "", label_visibility="collapsed")
    g31_33 = "" # st.text_input("31.33 - Кол-во товаров подлежащие последовательности", value = "", label_visibility="collapsed")
    g31_34 = "" # st.text_input("31.34 - Код единицы измерения ", value = "", label_visibility="collapsed")
    g31_35 = "" #st.text_input("31.35 - Наименвоание единицы измерения", value = "", label_visibility="collapsed")


###### 32 - Товар")
    g32_1= "" # st.text_input("32.1 - Доп информация о товаре", value = "", label_visibility="collapsed")

###### 34 - Код страны происхождения")
    g34_1 = "" # st.text_input("34.1 — Код", value = get_country_code(get_product_country(all_data)), label_visibility="collapsed")
    g34_2 = "" # st.text_input("34.2 - Код страны при преференциях", value = "", label_visibility="collapsed")

###### 35 - Вес брутто")
    g35_1 = "" # st.text_input("35 — Вес", value = get_brutto(all_data), label_visibility="collapsed")

###### 38 - Вес нетто")
    g38_1 = "" # st.text_input("38 — Вес", value = get_netto(all_data), label_visibility="collapsed")

 ###### 37 - Процедура")
    g37_1 = "" # st.text_input("37.1 - Код", value = default_code_TP + "00" + "000", label_visibility="collapsed") #КЛАССИФИКАТОР ОСОБЕННОСТЕЙ ПЕРЕМЕЩЕНИЯ ТОВАРОВ - по умолчанию 000

###### 40 - Общая декларация/Предшествующий документ") 
    g40_1 = "" # st.text_input("40.1 - Предшествующий документ", value = "", label_visibility="collapsed")

###### 41 - Дополнительные единицы")
    g41_1 = "" # st.text_input("41.1 - Количество/Единицы измерения/Код", value=get_product_unit(all_data), label_visibility="collapsed")
    g41_2 = "" # st.text_input("41.2 - ", value = "", label_visibility="collapsed")
    g41_3 = "" # st.text_input("41.3 - ", value = "", label_visibility="collapsed")

###### 42 - Цена товара")
    g42_1 = "" # st.text_input("42 - Цена в иностранной валюте", value=get_total_sum_invoice(all_data), label_visibility="collapsed")

###### 33 - Код товара")
    g33_1 = "" # st.text_input("33.1 — Номер", value = get_tnved(all_data), label_visibility="collapsed")

###### 36 - Преференции") 
    g36_1 = "" # st.text_input("36.1 — Преференция таможенных сборов", value = "OO", label_visibility="collapsed")
    g36_2 = "" # st.text_input("36.2 — Преференция пошлины", value = "OO", label_visibility="collapsed")
    g36_3 = "" # st.text_input("36.3 — Преференция акцизы", value = "-", label_visibility="collapsed")
    g36_4 = "" # st.text_input("36.4 — Преференция НДС", value = "OO", label_visibility="collapsed")
 
###### 39 - Квота
    g39_1 = "" # st.text_input("39.1 - Квота", value = "", label_visibility="collapsed")
    g39_2 = "" # st.text_input("39.2 - Единицы измерения квоты", value = "", label_visibility="collapsed")
    g39_3 = "" # st.text_input("39.3 - Код единицы", value = "", label_visibility="collapsed")

###### 43 - Код МОС")

    g43 = "" # st.text_input("Код признака", value = ch43["code"])

###### 44 - Дополнительная информация / Предоставленные документы")
    g44_1 = "" # st.text_area("44 - Список всех документов",value=docs_text,height=120, label_visibility="collapsed")

###### 45 - Таможенная стоимость")
    g45_1 = "" # st.text_input("45.1 Таможенная стоимость", value = "", label_visibility="collapsed")

###### 46 - Статистическая стоимость")
    g46_1 = "" # st.text_input("46.1 Таможенная стоимость", value = "", label_visibility="collapsed")
