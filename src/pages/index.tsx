import React from "react";

const fetchDataFromFastAPI = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/endpoint");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

const Home = () => {
  fetchDataFromFastAPI();
  return (
    <>
      <h1>Webapp</h1>
    </>
  );
};

export default Home;
