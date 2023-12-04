import { Result, Button } from "antd";

const StressResult = ({ stressLevel, onReturn }) => {
  return (
    <div style={{ textAlign: "center" }}>
      <Result status="success" title={stressLevel.title} />
      <p style={{ marginTop: "20px", fontSize: "18px" }}>{stressLevel.description}</p>
      <p style={{ marginTop: "50px" }}>
        *Este teste não possui validade médica. Consulte um profissional de saúde para avaliações
        precisas sobre o seu estado emocional e mental.*
      </p>
      <Button onClick={onReturn}>Voltar</Button>
    </div>
  );
};

export default StressResult;
