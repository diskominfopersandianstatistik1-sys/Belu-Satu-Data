<!DOCTYPE html>
<html>
<head>
  <title>Dashboard Statistik Sektoral</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body style="background: transparent; color: white;">

  <h3>Jumlah UMKM per Tahun</h3>
  <canvas id="myChart" width="400" height="200"></canvas>

  <script>
    const data = {
      labels: ['2021', '2022', '2023', '2024'],
      datasets: [{
        label: 'Jumlah UMKM',
        data: [500, 620, 668, 720],
        borderWidth: 2
      }]
    };

    const config = {
      type: 'line',
      data: data,
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    };

    new Chart(
      document.getElementById('myChart'),
      config
    );
  </script>

</body>
</html>
