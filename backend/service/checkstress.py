import pickle
from pydantic import ValidationError


def predict_stress(form):
    try:
        # Verifica os tipos das variáveis antes de continuar
        if not all(isinstance(value, int) for value in form.dict().values()):
            raise ValueError("Todos os campos devem ser números inteiros.")

        # Carrega o modelo treinado a partir do arquivo pickle
        with open('modelo_treinado.pkl', 'rb') as pickle_in:
            modelo = pickle.load(pickle_in)

        # Faz a previsão usando o modelo
        predict = modelo.predict([[form.sleep_quality, form.headaches,
                                   form.academic_performance, form.study_load, form.extracurricular_activities]])

        # Retorna o resultado da previsão
        return {'stress_level': int(predict[0])}, 200

    except ValidationError as ve:
        # Em caso de erro de validação, retorna uma mensagem de erro com código de status 422
        error_detail = ve.json() if hasattr(ve, 'json') else str(ve)
        return {'error': error_detail}, 422

    except Exception as e:
        # Em caso de outros erros, retorna uma mensagem de erro com código de status 500
        return {'error': f'Erro na previsão de estresse: {str(e)}'}, 500
