import Axios from "axios";

const axios = Axios.create({
  baseURL: "http://localhost:5001",
});

const evaluateStress = async (formValues) => {
  const formdata = new FormData();
  formdata.set("sleep_quality", formValues.sleepQuality);
  formdata.set("headaches", formValues.headaches);
  formdata.set("academic_performance", formValues.academicPerformance);
  formdata.set("study_load", formValues.studyLoad);
  formdata.set("extracurricular_activities", formValues.extracurricularActivities);
  return await axios
    .post("/teststress", formdata)
    .then((res) => res.data)
    .catch(() => null);
};

export { evaluateStress };
