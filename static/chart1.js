fetch("chart")
  .then((response) => response.json())
  .then((data) => {
    alert(data);
    var ctx = document.getElementById("lineChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.labels,
        datasets: [
          {
            label: "Cost in Ksh",
            data: data.cost_data,
            backgroundColor: ["rgba(85,85,85, 1)"],
            borderColor: "rgb(41, 155, 99)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
      },
    });
  })
  .catch((error) => {
    console.log(error);
  });
