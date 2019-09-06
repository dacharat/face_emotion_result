loadData = (defaultData, range) => {
  let datasets = [];
  for (let i = 0; i < defaultData.length; i++) {
    data = defaultData[i].slice(range.start, range.end + 1);
    datasets = [
      ...datasets,
      {
        label: emotions[i],
        data: data,
        fill: false,
        borderColor: colors[i],
        borderWidth: 3
      }
    ];
  }
  return datasets;
};

setChart = (labels, defaultData, range, datasets = []) => {
  datasets = loadData(defaultData, range);
  labels = labels.slice(range.start, range.end + 1);

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

updateChart = (labels, defaultData, range) => {
  datasets = loadData(defaultData, range);
  labels = labels.slice(range.start, range.end + 1);
  myChart.data.datasets = datasets;
  myChart.data.labels = labels;
  myChart.update();
};

rangeOfDate = () => {
  return { start: getStartIndex(), end: getEndIndex() };
};

getStartIndex = () => {
  let startIndex = 0;
  for (let i = 0; i < labels.length; i++) {
    if (moment(labels[i]).isSameOrBefore(startTime)) {
      startIndex = i;
    }
  }
  return startIndex + 1;
};

getEndIndex = () => {
  let endIndex = 0;
  for (let i = 0; i < labels.length; i++) {
    if (moment(labels[i]).isSameOrBefore(endTime)) {
      endIndex = i;
    }
  }
  return endIndex;
};