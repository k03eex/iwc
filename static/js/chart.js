function buildchart(node_id){
  $.getJSON('http://0.0.0.0:8000/api/v1/nodes/' + node_id + '/sensors', function (data) {
    var aci = [];
    var aci_only = [];
    var aci_avg = 0;
    var temperature = [];
    var temperature_only = [];
    var temperature_avg = 0;
    var humidity = [];
    var humidity_only = [];
    var humidity_avg = 0;
    var pressure = [];
    var pressure_only = [];
    var pressure_avg = 0;
    var light = [];
    var light_only = [];
    var light_avg = 0;
    var count = 0;

    for (var i = 0; i < data.length; i++){
      new_date = Date.parse(data[i].timestamp)

      aci_avg += data[i].aci
      aci_only.push(data[i].aci)
      aci.push([new_date, data[i].aci])

      temperature_avg += data[i].temperature
      temperature_only.push(data[i].temperature)
      temperature.push([new_date, data[i].temperature])

      humidity_avg += data[i].humidity
      humidity_only.push(data[i].humidity)
      humidity.push([new_date, data[i].humidity])

      pressure_avg += data[i].pressure
      pressure_only.push(data[i].pressure)
      pressure.push([new_date, data[i].pressure])

      light_avg += data[i].light
      light_only.push(data[i].light)
      light.push([new_date, data[i].light])

      count += 1;
    };

    var aci_min = Math.min.apply(null, aci_only).toFixed(3);
    var aci_max = Math.max.apply(null, aci_only).toFixed(3);
    var aci_avg = (aci_avg/count).toFixed(3);
    var aciHTML = '<ul class="bulleted">';
    aciHTML += '<li>';
    aciHTML += 'Min: '+ aci_min + '</li>';
    aciHTML += '<li>';
    aciHTML += "Max: " + aci_max + '</li>';
    aciHTML += '<li>';
    aciHTML += "Avg: " + aci_avg + '</li>';
    aciHTML += '</ul>';
    $('#aci_values').html(aciHTML)

    var temperature_min = Math.min.apply(null, temperature_only);
    var temperature_max = Math.max.apply(null, temperature_only);
    var temperature_avg = temperature_avg/count;

    var humidity_min = Math.min.apply(null, humidity_only);
    var humidity_max = Math.max.apply(null, humidity_only);
    var humidity_avg = humidity_avg/count;

    var pressure_min = Math.min.apply(null, pressure_only);
    var pressure_max = Math.max.apply(null, pressure_only);
    var pressure_avg = pressure_avg/count;

    var light_min = Math.min.apply(null, light_only);
    var light_max = Math.max.apply(null, light_only);
    var light_avg = light_avg/count



    $('#container_aci').highcharts('StockChart', {
      chart: {
          zoomType: 'x'
      },
      rangeSelector: {
        allButtonsEnabled: true,
        selected: 1
      },
      yAxis: {
          title: {
              text: 'ACI'
          }
      },
      title: {
          text: 'Acoustic complexity index'
      },
      series: [{
          name: 'ACI',
          data: aci,
          tooltip: {
              valueDecimals: 1,
          }
      }]
    });

    $('#container_temp').highcharts('StockChart', {
      chart: {
          zoomType: 'x'
      },
      rangeSelector: {
        allButtonsEnabled: true,
        selected: 1
      },
      yAxis: {
          title: {
              text: 'Temperature (°C)'
          }
      },
      title: {
          text: 'Temperature '
      },
      series: [{
          name: 'Temperature',
          data: temperature,
          tooltip: {
              valueDecimals: 1,
              valueSuffix: '°C'
          }
      }]
    });

    $('#container_humidity').highcharts('StockChart', {
      chart: {
          zoomType: 'x'
      },
      rangeSelector: {
        allButtonsEnabled: true,
        selected: 1
      },
      yAxis: {
          title: {
              text: 'Humidity'
          }
      },
      title: {
          text: 'Humidity'
      },
      series: [{
          name: 'Humidity',
          data: humidity,
          tooltip: {
              valueDecimals: 1,
              valueSuffix: ''
          }
      }]
    });

    $('#container_pressure').highcharts('StockChart', {
      chart: {
          zoomType: 'x'
      },
      rangeSelector: {
        allButtonsEnabled: true,
        selected: 1
      },
      yAxis: {
          title: {
              text: 'Air Pressure'
          }
      },
      title: {
          text: 'Air Pressure'
      },
      series: [{
          name: 'Pressure',
          data: pressure,
          tooltip: {
              valueDecimals: 1,
              valueSuffix: ''
          }
      }]
    });

    $('#container_light').highcharts('StockChart', {
      chart: {
          zoomType: 'x'
      },
      rangeSelector: {
        allButtonsEnabled: true,
        selected: 1
      },
      yAxis: {
          title: {
              text: 'Light Level'
          }
      },
      title: {
          text: 'Light Level'
      },
      series: [{
          name: 'Light',
          data: light,
          tooltip: {
              valueDecimals: 1,
              valueSuffix: ''
          }
      }]
    });
  });
};
