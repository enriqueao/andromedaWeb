function abrirMenu() {
    var menu = document.querySelector('#menu');
    var img = document.querySelector('#img');
    if(menu.style.marginLeft == '-70%') {
      menu.style.marginLeft = '0%';
      img.src = '../static/images/back.svg';
    } else {
      img.src = '../static/images/menu.svg';
      menu.style.marginLeft = '-70%';
    }

}

function vistas(vista) {
  var contenido = document.getElementById('contenido-element');
  $.ajax({
    url: "/andromeda/"+vista+"/",
    type: "POST",
    success: function (response) {
       contenido.innerHTML = response;
       abrirMenu();
    }
  });
}

function graficar(){
  setTimeout("grafica()",700);
}

function grafica(){
  Highcharts.setOptions({
     colors: ['#40b797','#dd2c5b','#ddad2c']
    });
  Highcharts.chart('container', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: ''
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}% - {point.y} Recordatorios</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false
            },
            showInLegend: true
        }
    },
    series: [{
        name: 'Recordatorios',
        colorByPoint: true,
        data: [{name: 'Completadas',y: 56},{name: 'Eliminados',y: 51},{name: 'Pendientes',y: 4}]
    }],
    exporting: { enabled: false },
    credits: {enabled: false},
});
}


function nuevo(){
  var nuevo =  document.getElementById('nuevo');
    nuevo.classList.remove('animated','fadeOutDown');
    nuevo.classList.add('animated','fadeInUp');
    nuevo.style = '';
}

function down(){
  var nuevo =  document.getElementById('nuevo');
    nuevo.classList.remove('animated','fadeInUp');
    nuevo.classList.add('animated','fadeOutDown');
    setTimeout(function(){
      nuevo.style = 'display:none;';
    },400);
}
