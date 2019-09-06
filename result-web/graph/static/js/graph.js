loadingData = data => {
  let datasets = [];
  for (let i = 0; i < data.length; i++) {
    datasets = [
      ...datasets,
      {
        label: emotions[i],
        data: data[i],
        fill: false,
        borderColor: colors[i],
        borderWidth: 3
      }
    ];
  }
  return datasets;
};

setChart = (labels = [1], defaultData = [[0,0,0,0,0,0,0]]) => {
  datasets = loadingData(defaultData);

  var ctx = document.getElementById("myChart");
  myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: datasets
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              suggestedMax: 1
            }
          }
        ]
      }
    }
  });
};

realtimeUpdate = (label, data) => {
  datasets = loadingData(data);
  myChart.data.datasets = datasets;
  myChart.data.labels = label;
  myChart.update();
};

recordingEmotionData = (data, face_name) => {
  $.ajax({
    url: "http://localhost:3000/face/new/",
    type: "PUT",
    data: JSON.stringify({
      face: face_name,
      emotion_detail: data,
      action: "insert_new_record"
    }),
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    success: data => {
      console.log("Record ", data);
      recordingData = [];
    },
    error: err => {
      console.log(err);
    }
  });
};
