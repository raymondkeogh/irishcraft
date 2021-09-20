    
    $(function () {
        

      var $productChart = $("#product-chart");
      $.ajax({
        url: $productChart.data("url"),
        success: function (data) {

          var ctx = $productChart[0].getContext("2d");

          new Chart(ctx, {
            type: 'bar',
            data: {
              labels: data.labels,
              datasets: [
                {
                label: 'Product Views',
                backgroundColor: '#e05f5f',
                data: data.data
                },
                {
                label: 'Purchased',
                backgroundColor: '#00bd19',
                data: data.data2
                }]           
            },
            options: {
              responsive: true,
              legend: {
                position: 'top',
              },
              title: {
                display: false,
                text: 'Product Activity'
              }
            }
          });

        }
      });

    });
