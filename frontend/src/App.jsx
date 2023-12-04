import { useState } from "react";
import QuestionForm from "./QuestionForm";
import StressResult from "./StressResult";
import Layout from "antd/es/layout/layout";
import { evaluateStress } from "./api";

const App = () => {
  const [currentPage, setCurrentPage] = useState("form");
  const [stressLevel, setStressLevel] = useState(null);

  const handleFormSubmit = async (formData) => {
    const res = await evaluateStress(formData);
    console.log(res);
    setStressLevel(res);
    setCurrentPage("result");
  };

  const handleReturn = () => {
    setCurrentPage("form");
  };

  return (
    <Layout>
      {currentPage === "form" && <QuestionForm onSubmit={handleFormSubmit} />}
      {currentPage === "result" && (
        <StressResult stressLevel={stressLevel} onReturn={handleReturn} />
      )}
    </Layout>
  );
};

export default App;
