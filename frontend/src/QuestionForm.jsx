import React, { useState } from "react";
import { Radio, Button } from "antd";

const QuestionForm = ({ onSubmit }) => {
  const [formValues, setFormValues] = useState({
    sleepQuality: 1,
    headaches: 1,
    academicPerformance: 1,
    studyLoad: 1,
    extracurricularActivities: 1,
  });

  const handleRadioChange = (e, key) => {
    setFormValues((prevValues) => ({ ...prevValues, [key]: e.target.value }));
  };

  const handleSubmit = () => {
    // Você pode fazer algo com os valores do formulário antes de enviar
    onSubmit(formValues);
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h2>Análise de estresse em alunos de Engenharia</h2>
      <p>Por favor, responda às perguntas selecionando valores de 1 a 5:</p>
      <div style={{ marginBottom: "10px" }}>
        <label>Por favor, avalie a qualidade do seu sono:</label>
        <br />
        <Radio.Group
          onChange={(e) => handleRadioChange(e, "sleepQuality")}
          defaultValue={formValues.sleepQuality}
        >
          {[1, 2, 3, 4, 5].map((value) => (
            <Radio key={value} value={value}>
              {value}
            </Radio>
          ))}
        </Radio.Group>
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Quantas vezes por semana você sofre de dores de cabeça?</label>
        <br />
        <Radio.Group
          onChange={(e) => handleRadioChange(e, "headaches")}
          defaultValue={formValues.headaches}
        >
          {[1, 2, 3, 4, 5].map((value) => (
            <Radio key={value} value={value}>
              {value}
            </Radio>
          ))}
        </Radio.Group>
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Como você avaliaria seu desempenho acadêmico?</label>
        <br />
        <Radio.Group
          onChange={(e) => handleRadioChange(e, "academicPerformance")}
          defaultValue={formValues.academicPerformance}
        >
          {[1, 2, 3, 4, 5].map((value) => (
            <Radio key={value} value={value}>
              {value}
            </Radio>
          ))}
        </Radio.Group>
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Como você avaliaria sua carga de estudos?</label>
        <br />
        <Radio.Group
          onChange={(e) => handleRadioChange(e, "studyLoad")}
          defaultValue={formValues.studyLoad}
        >
          {[1, 2, 3, 4, 5].map((value) => (
            <Radio key={value} value={value}>
              {value}
            </Radio>
          ))}
        </Radio.Group>
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label>Quantas vezes por semana você pratica atividades extracurriculares?</label>
        <br />
        <Radio.Group
          onChange={(e) => handleRadioChange(e, "extracurricularActivities")}
          defaultValue={formValues.extracurricularActivities}
        >
          {[1, 2, 3, 4, 5].map((value) => (
            <Radio key={value} value={value}>
              {value}
            </Radio>
          ))}
        </Radio.Group>
      </div>

      <Button type="primary" onClick={handleSubmit}>
        Enviar
      </Button>
    </div>
  );
};

export default QuestionForm;
