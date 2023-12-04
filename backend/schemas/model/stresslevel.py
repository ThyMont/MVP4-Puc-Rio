from enum import Enum


class StressLevel(Enum):
    TRANQUILIDADE = 0
    MUITO_BAIXO = 1
    BAIXO = 2
    MODERADO = 3
    ALTO = 4
    MUITO_ALTO = 5

    def to_dict(self):
        return {
            'stress_level': self.value,
            'title': self.get_title(),
            'description': self.get_description()
        }

    def get_title(self):
        # Adicione títulos melhorados para cada nível de estresse conforme necessário
        titles = {
            StressLevel.TRANQUILIDADE: 'Nível 0 de Estresse: Tranquilidade',
            StressLevel.MUITO_BAIXO: 'Nível 1 de Estresse: Muito Baixo',
            StressLevel.BAIXO: 'Nível 2 de Estresse: Baixo',
            StressLevel.MODERADO: 'Nível 3 de Estresse: Moderado',
            StressLevel.ALTO: 'Nível 4 de Estresse: Alto',
            StressLevel.MUITO_ALTO: 'Nível 5 de Estresse: Muito Alto',
        }
        return titles.get(self, 'Nível de Estresse Desconhecido')

    def get_description(self):
        # Adicione descrições personalizadas para cada nível de estresse
        descriptions = {
            StressLevel.TRANQUILIDADE: 'Você está em um estado de tranquilidade. Continue assim!',
            StressLevel.MUITO_BAIXO: 'Seu nível de estresse é muito baixo. Continue assim!',
            StressLevel.BAIXO: 'Seu nível de estresse é baixo. Ótimo trabalho!',
            StressLevel.MODERADO: 'Você está experimentando um nível moderado de estresse. Fique atento aos sinais do seu corpo.',
            StressLevel.ALTO: 'Seu nível de estresse está alto. Considere maneiras de reduzir o estresse em sua vida.',
            StressLevel.MUITO_ALTO: 'Alerta! Seu nível de estresse está muito alto. Procure apoio e encontre maneiras de relaxar.',
        }
        return descriptions.get(self, 'Descrição padrão para o nível de estresse.')
