from pydantic import ValidationError
from schemas.form import StressForm
from service.checkstress import predict_stress


def test_stress_form_validation():
    # Teste para validação do StressForm - deve passar sem levantar exceções
    try:
        valid_stress_form = StressForm(
            sleep_quality=3, headaches=2, academic_performance=4, study_load=3, extracurricular_activities=1)
        valid_stress_form.dict()
    except ValidationError as ve:
        assert False, f"A exceção ValidationError foi levantada: {ve}"


def test_predict_stress_valid_input():
    # Teste para entrada válida - deve retornar uma previsão com código de status 200
    try:
        valid_stress_form = StressForm(
            sleep_quality=3, headaches=2, academic_performance=4, study_load=3, extracurricular_activities=1)
        result, status_code = predict_stress(valid_stress_form)
        assert status_code == 200
        assert 'stress_level' in result
        assert isinstance(result['stress_level'], int)
    except ValidationError as ve:
        assert False, f"A exceção ValidationError foi levantada: {ve}"


def test_predict_stress_invalid_input_validation():
    # Teste para validar a entrada inválida do StressForm - deve levantar exceção de validação
    try:
        invalid_form = StressForm(sleep_quality='invalid', headaches=2,
                                  academic_performance=4, study_load=3, extracurricular_activities=1)
        invalid_form.dict()
        assert False, "A exceção ValidationError não foi levantada."
    except ValidationError as ve:
        assert "value is not a valid integer" in str(ve.errors())


def test_predict_stress_type_error_validation():
    # Teste para validar tipos inválidos do StressForm - deve levantar exceção de validação
    try:
        type_error_form = StressForm(sleep_quality='invalid', headaches='invalid',
                                     academic_performance='invalid', study_load='invalid', extracurricular_activities='invalid')
        type_error_form.dict()
        assert False, "A exceção ValidationError não foi levantada."
    except ValidationError as ve:
        assert "value is not a valid integer" in str(ve.errors())
