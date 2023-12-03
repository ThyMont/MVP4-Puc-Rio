from pydantic import BaseModel, Field


class StressForm(BaseModel):
    """
    Formulário de avaliação de estresse
    """
    sleep_quality: int = Field(1, description='Qualidade do sono?')
    headaches: int = Field(
        1, description='Quantas vezes por semana sente dor de cabeça?')
    academic_performance: int = Field(
        1, description='Como você avaliaria seu desempenho acadêmico?')
    study_load: int = Field(
        1, description='Como você avaliaria sua carga de estudos?')
    extracurricular_activities: int = Field(
        1, description='Quantas vezes por semana você pratica atividades extracurriculares?')
