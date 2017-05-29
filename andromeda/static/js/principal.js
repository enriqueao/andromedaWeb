function abrirMenu() {
    var menu = document.querySelector('#menu');
    var img = document.querySelector('#img');
    if(menu.style.marginLeft == '-70%') {
      menu.style.marginLeft = '0%';
      img.src = '/static/images/back.svg';
    } else {
      img.src = '/static/images/menu.svg';
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

var pendientes = 0;
var completados = 0;
var eliminados = 0;


function graficar(){
  id = document.getElementById('id');
  $.ajax({
    url: "/andromeda/graficar/",
    type: "POST",
    data:{'idAndromeda':id.value},
    success: function (response) {
      pendientes = response['pendientes'];
      completados = response['completados'];
      eliminados = response['eliminados'];
      setTimeout("grafica()",700);
    }
  });
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
        data: [{name:'Completadas',y:completados},{name:'Eliminados',y:eliminados},{name:'Pendientes',y:pendientes}],
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
    descripcion = document.getElementById('descripcion').focus();
}

function down(){
  var nuevo =  document.getElementById('nuevo');
    nuevo.classList.remove('animated','fadeInUp');
    nuevo.classList.add('animated','fadeOutDown');
    setTimeout(function(){
      nuevo.style = 'display:none;';
    },400);
}

var myElement = document.body;
var mc = new Hammer(myElement);
mc.on("panleft", function(ev) {
  abrirMenu();
});
mc.on("panright", function(ev) {
  abrirMenu();
});

document.getElementById("diaRecordatorio").valueAsDate = new Date()

$(function(){
$('input[type="time"][id="horaRecordar"]').each(function(){
  var d = new Date(),
      h = d.getHours(),
      m = d.getMinutes();
  if(h < 10) h = '0' + h;
  if(m < 10) m = '0' + m;
  $(this).attr({
    'value': h + ':' + m
  });
});
});

function guardarRecordatorio() {
  prioridad = document.getElementById('prioridad');
  id = document.getElementById('id');
  diaRecordatorio = document.getElementById('diaRecordatorio');
  descripcion = document.getElementById('descripcion');
  horaRecordar = document.getElementById('horaRecordar');

  paraRecordar = diaRecordatorio.value+' '+horaRecordar.value+':00';
  $.ajax({
    url: "/andromeda/guardarRecordatorio/",
    type: "POST",
    data:{'idTipoRecordatorio':prioridad.value,'diaRecordatorio':diaRecordatorio.value,'descripcion':descripcion.value,'horaRecordar':horaRecordar.value,'id':id.value},
    success: function (response) {
       if(response == '1'){
          alert('Andromeda te recordara '+descripcion.value+' en '+calcularTiempo(paraRecordar))
          recor();
          down();
          descripcion.value = '';
       } else {
         console.log(response);
       }
    }
  });
}

function calcularTiempo() {
  var fecha1 = moment().format('YYYY-MM-DD HH:mm:ss');
  var fecha2 = moment(paraRecordar, "YYYY-MM-DD HH:mm:ss");
  var dias = fecha2.diff(fecha1, 'd'); // Diff in days
  var horas = fecha2.diff(fecha1, 'h'); // Diff in hours
  var minutos = fecha2.diff(fecha1, 'm'); // Diff in hours

  if(dias != '0') {
      return dias+' días y '+horas+' horas';
  } if(horas != 0){
    return horas+' horas';
  } else {
    return minutos+' minutos';
  }
}

function recor(){
  setTimeout("recordatorios()",500);
}

function recordatorios() {
  var id = document.getElementById('id');
  var recordatoriosinner = document.getElementById('recordatorios');
  var numPendientes = document.getElementById('numPendientes');
  var recordatoriosPendientes = '';
  var importancia = '';
  $.ajax({
    url: "/andromeda/recordatoriosPendientes/",
    type: "POST",
    data:{'id':id.value},
    success: function (response) {
      var recordatorios = response;
      numPendientes.innerHTML = recordatorios.length+' Recordatorios Pendientes';
      for (var i = 0; i < recordatorios.length; i++) {
        formato = recordatorios[i]['fields'];
        if(formato.idTipoRecordatorio == 1){importancia = 'alta'}if(formato.idTipoRecordatorio == 2){importancia = 'moderada'}else{importancia = 'baja'}
        recordatoriosPendientes += '<div id='+recordatorios[i].pk+' class="recordatorio importancia-'+importancia+' animated pulse"> <div class="recordatorio-hora"> <p>'+formato.horaRecordar+'</p> </div> <div class="recordatorio-info"> <p>'+formato.descripcion+'</p> </div> <div class="recordatorio-action delete"><a onclick="eliminar('+recordatorios[i].pk+')"><img src="/static/images/rubbish-bin.svg" alt=""></a></div><div class="recordatorio-action complete"><a onclick="completar('+recordatorios[i].pk+')"><img src="/static/images/tick-inside-circle.svg" alt=""></a></div> </div>';
      }
      recordatoriosinner.innerHTML = recordatoriosPendientes;
    }
  });
}


function completar(id) {
  var elemento = document.getElementById(id);
  if(confirm("¿Deseas Completar este recordatorio?")){
    $.ajax({
      url: "/andromeda/completarRecordatorio/",
      type: "POST",
      data:{'primary':id},
      success: function (response) {
          if(response == '1'){
            elemento.classList.remove("pulse");
            elemento.classList.add("zoomOutUp");
            recordatorios();
          } else {
            elemento.classList.remove("pulse");
            elemento.classList.add("shake");
          }
        }
      });
    }
}

function eliminar(id) {
  var elemento = document.getElementById(id);
  if(confirm("¿Quieres eliminarlo?, ya no se te será recordado")){
    $.ajax({
      url: "/andromeda/eliminarRecordatorio/",
      type: "POST",
      data:{'primary':id},
      success: function (response) {
        if(response == '1'){
          elemento.classList.remove("pulse");
          elemento.classList.add("zoomOutUp");
          recordatorios();
        } else {
          elemento.classList.remove("pulse");
          elemento.classList.add("shake");
        }
      }
    });
  }
}
