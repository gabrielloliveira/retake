def test_process_01(process_data_01):
    parts = [
        dict(part="Eduardo Amoroso", category="EXEQUENTE"),
        dict(part="Jose Fonseca", category="ADVOGADOS EXEQUENTE"),
        dict(part="Daniele Caldas", category="EXECUTADA"),
    ]
    assert process_data_01.number == "1004030-81.2016.0.00.0008"
    assert process_data_01.class_name == "Execução de Título Extrajudicial"
    assert process_data_01.subject == "Locação de Imóvel"
    assert process_data_01.judge == "Mariana"
    assert process_data_01.parts == parts


def test_process_02(process_data_02):
    parts = [
        dict(part="Eduardo Silva", category="REQUERIDO"),
        dict(part="Banco Bandeira", category="REQUERENTE"),
        dict(part="Junior Barriga", category="ADVOGADOS REQUERENTE"),
    ]
    assert process_data_02.number == "1007944-79.2020.0.00.0361"
    assert process_data_02.class_name == "Busca e Apreensão em Alienação Fiduciária"
    assert process_data_02.subject == "Alienação Fiduciária"
    assert process_data_02.judge == "Domingos Parra Neto"
    assert process_data_02.parts == parts
