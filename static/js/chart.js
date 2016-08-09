function buildchart(node_id){
  /*the main function*/

  function build_values(sensor_selector, sensorHTML, min, max, avg){
    /*Add min, max and avg values to each graph*/
    var sensorHTML = '<ul class="bulleted">';
    sensorHTML += '<li>';
    sensorHTML += 'Min: '+ min + '</li>';
    sensorHTML += '<li>';
    sensorHTML += "Max: " + max + '</li>';
    sensorHTML += '<li>';
    sensorHTML += "Avg: " + avg + '</li>';
    sensorHTML += '</ul>';
    $(sensor_selector).html(sensorHTML)
  }

  function build_highchart(container_selector, sensor_tile, yAxis_title, series_name, sensor_data){
    /*Highcharts function to build graphs*/
    $(container_selector).highcharts('StockChart', {
      chart: {
          zoomType: 'x'
      },
      rangeSelector: {
        allButtonsEnabled: true,
        selected: 1
      },
      yAxis: {
          title: {
              text: yAxis_title
          }
      },
      title: {
          text: sensor_tile
      },
      series: [{
          name: series_name,
          data: sensor_data,
          tooltip: {
              valueDecimals: 1,
          }
      }]
    });
  }; //end of build_highchart function

  function show_rgb(light_colors){
    /*Build modal box for rgb values*/
    // Get the modal
    var modal = document.getElementById('myModal');
    // Get the button that opens the modal
    var btn = document.getElementById("modal_button");
    // Get the <span> element that closes the modal
    //$('.modal-content').html('<span class="close">x</span>')
    //var span = document.getElementsByClassName("close")[0];
    // When the user clicks the button, open the modal
    btn.onclick = function() {
      modal.style.display = "block";
      console.log(light_colors)
      var sensorHTML = '<table class="rgb_table">';
      sensorHTML += '<tr>'
      sensorHTML += '<th>DateTime</th>'
      sensorHTML += '<th>RGB</th>'
      sensorHTML += '</tr>'

      for (var i = 0; i < light_colors.length; i++){
          sensorHTML += '<tr>'
            sensorHTML += '<td>' + light_colors[i][0] + '</td>'
            sensorHTML += '<td style="background-color:rgb(' + light_colors[i][1] + ');">'  + light_colors[i][1] + '</td>'
          sensorHTML += '</tr>'
      }
      sensorHTML += '</table>'
      $('.modal-content').html(sensorHTML)
    }
    // When the user clicks on <span> (x), close the modal
    /*span.onclick = function() {
        modal.style.display = "none";
    }*/
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
  }; // end of show_rgb function

  $.getJSON('http://0.0.0.0:8000/api/v1/nodes/' + node_id + '/aci/', function (data) {
    var aci = [];
    var aci_only = [];
    var aci_avg = 0;
    var count = 0;

    for (var i = 0; i < data.length; i++){
      new_date = Date.parse(data[i].timestamp)
      aci_avg += data[i].aci
      aci_only.push(data[i].aci)
      aci.push([new_date, data[i].aci])
      count += 1;
    }; // loop end

    var aci_min = Math.min.apply(null, aci_only).toFixed(3);
    var aci_max = Math.max.apply(null, aci_only).toFixed(3);
    var aci_avg = (aci_avg/count).toFixed(3);
    build_values('#aci_values', 'aciHTML', aci_min, aci_max, aci_avg)
    build_highchart('#container_aci', 'Acoustic complexity index', 'ACI', 'ACI', aci)

  }); //end of getJSON for ACI

  $.getJSON('http://0.0.0.0:8000/api/v1/nodes/' + node_id + '/sensors/', function (data) {

    var temperature = [];
    var temperature_only = [];
    var temperature_avg = 0;
    var humidity = [];
    var humidity_only = [];
    var humidity_avg = 0;
    var pressure = [];
    var pressure_only = [];
    var pressure_avg = 0;
    var light_colors = [];
    var count = 0;

    for (var i = 0; i < data.length; i++){
      new_date = Date.parse(data[i].timestamp)

      temperature_avg += data[i].temperature
      temperature_only.push(data[i].temperature)
      temperature.push([new_date, data[i].temperature])

      humidity_avg += data[i].humidity
      humidity_only.push(data[i].humidity)
      humidity.push([new_date, data[i].humidity])

      pressure_avg += data[i].pressure
      pressure_only.push(data[i].pressure)
      pressure.push([new_date, data[i].pressure])

      var light_rgb = [data[i].light_red, data[i].light_green, data[i].light_blue]
      light_colors.push([data[i].timestamp, light_rgb])

      count += 1;
    }; //end of loop

    var temperature_min = Math.min.apply(null, temperature_only);
    var temperature_max = Math.max.apply(null, temperature_only);
    var temperature_avg = (temperature_avg/count).toFixed(3);
    build_values('#temp_values', 'tempHTML', temperature_min, temperature_max, temperature_avg)

    var humidity_min = Math.min.apply(null, humidity_only);
    var humidity_max = Math.max.apply(null, humidity_only);
    var humidity_avg = (humidity_avg/count).toFixed(3);
    build_values('#humidity_values', 'humidityHTML', humidity_min, humidity_max, humidity_avg)

    var pressure_min = Math.min.apply(null, pressure_only);
    var pressure_max = Math.max.apply(null, pressure_only);
    var pressure_avg = (pressure_avg/count).toFixed(3);
    build_values('#pressure_values', 'pressureHTML', pressure_min, pressure_max, pressure_avg)

    build_highchart('#container_temp', 'Temperature', 'Temperature (°C)', 'Temperature', temperature)
    build_highchart('#container_humidity', 'Humidity', 'Humidity', 'Humidity', humidity)
    build_highchart('#container_pressure', 'Air Pressure', 'Air Pressure', 'Air Pressure', pressure)
    show_rgb(light_colors);
  }); //end of getJSON for sensors
}; //end of main function
