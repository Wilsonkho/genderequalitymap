//global variables
var literacyCategories = [];
var literacyFemale = [];
var literacyMale =[];
var unemploymentCategories = [];
var unemploymentMale = [];
var unemploymentFemale = [];
var parlimentCategories = [];
var parlimentMale = [];
var parlimentFemale = [];
var indexes = [];
var selected = [];
var map;

$(function() {
	$( "#radio" ).buttonset();
});



//graphing layer
    function pop(div) {
        document.getElementById(div).style.display = 'block';
    }
    function hide(div) {
        document.getElementById(div).style.display = 'none';
    }
			//To detect escape button
			document.onkeydown = function(evt) {
				evt = evt || window.event;
				if (evt.keyCode == 27) {
					hide('popDiv');
				}
			};

//graph function
function drawLitGraph() {
    var graphIndex = [];
    var countries = [];
    var men = [];
    var women = [];

    for (i = 0; i < selected.length; i++){
        graphIndex.push(literacyCategories.indexOf(selected[i]));
    }

    for (i = 0; i < graphIndex.length; i++){
        countries.push(literacyCategories[graphIndex[i]]);
        men.push(literacyMale[graphIndex[i]]);
        women.push(literacyFemale[graphIndex[i]]);
    }

	$('#literacy-graph').highcharts({
        chart: {
            type: 'bar',
        },
        title: {
            text: 'Global Literacy by Gender'
        },
        xAxis: [{
            categories: countries,
            reversed: false

	}, { // mirror axis on right side
	    opposite: true,
	    reversed: false,
	    categories: countries,
	    linkedTo: 0
	}],
	yAxis: {
	    title: {
	        text: null
	    },
	    labels:{
	    	formatter: function () {
	    		return(Math.abs(this.value));
	    	}
	    }

	},

	plotOptions: {
	    series: {
	        stacking: 'normal'
	    }
	},

	tooltip: {
	    formatter: function () {
	        return '<b>' + this.point.category +" "+ this.series.name + '</b><br/>' +
	        'Literacy Rate: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0) + "%";
	    }
	},

	series: [{
	    name: 'Men',
	    data: men
	}, {
	    name: 'Women',
	    data: women
	}]

	});
};

//graph function
function drawEmpGraph() {
    var graphIndex = [];
    var countries = [];
    var men = [];
    var women = [];

    for (i = 0; i < selected.length; i++){
        graphIndex.push(unemploymentCategories.indexOf(selected[i]));
    }

    for (i = 0; i < graphIndex.length; i++){
        countries.push(unemploymentCategories[graphIndex[i]]);
        men.push(unemploymentMale[graphIndex[i]]);
        women.push(unemploymentFemale[graphIndex[i]]);
    }

	$('#unemployment-graph').highcharts({
        chart: {
            type: 'bar',
        },
        title: {
            text: 'Global Unemployment by Gender'
        },
        xAxis: [{
            categories: countries,
            reversed: false

	}, { // mirror axis on right side
	    opposite: true,
	    reversed: false,
	    categories: countries,
	    linkedTo: 0
	}],
	yAxis: {
	    title: {
	        text: null
	    },
	    labels:{
	    	formatter: function () {
	    		return(Math.abs(this.value));
	    	}
	    }

	},

	plotOptions: {
	    series: {
	        stacking: 'normal'
	    }
	},

	tooltip: {
	    formatter: function () {
	        return '<b>' + this.point.category +" "+ this.series.name + '</b><br/>' +
	        'Unemployment Rate: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0) + "%";
	    }
	},

	series: [{
	    name: 'Men',
	    data: men
	}, {
	    name: 'Women',
	    data: women
	}]

	});
};
//graph function
function drawParGraph() {
    var graphIndex = [];
    var countries = [];
    var men = [];
    var women = [];

    for (i = 0; i < selected.length; i++){
        graphIndex.push(parlimentCategories.indexOf(selected[i]));
    }

    for (i = 0; i < graphIndex.length; i++){
        countries.push(parlimentCategories[graphIndex[i]]);
        men.push(parlimentMale[graphIndex[i]]);
        women.push(parlimentFemale[graphIndex[i]]);
    }

	$('#parliment-graph').highcharts({
        chart: {
            type: 'bar',
        },
        title: {
            text: 'Global Parlimentary Seats by Gender'
        },
        xAxis: [{
            categories: countries,
            reversed: false

	}, { // mirror axis on right side
	    opposite: true,
	    reversed: false,
	    categories: countries,
	    linkedTo: 0
	}],
	yAxis: {
	    title: {
	        text: null
	    },
	    labels:{
	    	formatter: function () {
	    		return(Math.abs(this.value));
	    	}
	    }

	},

	plotOptions: {
	    series: {
	        stacking: 'normal'
	    }
	},

	tooltip: {
	    formatter: function () {
	        return '<b>' + this.point.category +" "+ this.series.name + '</b><br/>' +
	        'Percentage of Seats: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0) + "%";
	    }
	},

	series: [{
	    name: 'Men',
	    data: men
	}, {
	    name: 'Women',
	    data: women
	}]

	});
};
//default map (no data)
function drawMap(){
	var map = new Datamap({
		scope: 'world',
		element: document.getElementById('world-map'),
		projection: 'mercator',
		geographyConfig: {
			highlightOnHover: true,
			popupOnHover: true,
			borderWidth: 2,
			borderColor: "black",
			popupTemplate: function(geography, data) {
				return '<div class="hoverinfo">' + geography.properties.name
			}
		},
		fills:{
			// defaultFill:"#00D8E5"
			defaultFill:"lightgrey"			
		}

	});
map.legend();
};