    
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
              datasets: [{
                label: 'product',
                backgroundColor: 'blue',
                data: data.data
              }]          
            },
            options: {
              responsive: true,
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Product Bar Chart'
              }
            }
          });

        }
      });

    });
