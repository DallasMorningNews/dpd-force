$(document).ready(function() {

	//custom scripting goes here

	// injecting current year into footer
	// DO NOT DELETE

	var d = new Date();
	var year = d.getFullYear();

	$('.copyright').text(year);


	var map = new mapboxgl.Map({
		container: "map",
		style: 'http://maps.dallasnews.com/styles.json',
		center: [-96.7870228, 32.8255772],
		zoom: 10
	});

	map.on("load", function() {
		map.scrollZoom.disable();
		map.addControl(new mapboxgl.Navigation());

		$.getJSON("js/map_data.json", function(data) {
			processData(data);
			console.log(data);
		});

	});

	function processData(data) {
		forceData = GeoJSON.parse(data, {Point: ["latitude", "longitude"], exclude: []});

		console.log(forceData);

		drawMap(forceData);

	}


	function drawMap(data) {

		map.addSource("dpdForceData", {
			type: "geojson",
			data: data
		});

		map.addLayer({
			"id": "forceIncidents",
			"source": "dpdForceData",
			"type": "circle",
			"layout": {
				"visibility": "visible"
			},
			"paint": {
				"circle-radius": {
					stops:[[8, 2], [11, 4], [15, 8]]
				},
				"circle-color": "#950000"
			}
		});


		map.on("click", function(e) {
			var features = map.queryRenderedFeatures(e.point, {layers: ["forceIncidents"]});

			if (!features.length) {
				return;
			}

			var feature = features[0];




			var id = feature.properties.id;
			var content = "";

			$.each(data.features, function(k,v) {
				if (v.properties.id === id) {
					var totalIncidents = v.properties.force_use.length;

					for (i = 0; i < totalIncidents; i++) {
						content += "<span class='badge' data-badge='"+ v.properties.force_use[i].current_badge_no +"'>" + v.properties.force_use[i].current_badge_no + "</span>";
					}
				}
			});



			$(".badge").click(function() {
				var badge = $(this).attr("data-badge");
				filterBadge(badge);
			});


			console.log(feature);

			var popup = new mapboxgl.Popup()
				.setLngLat(feature.geometry.coordinates)
				.setHTML(content)
				.addTo(map);

			$(".badge").click(function() {
				var badge = $(this).attr("data-badge");
				filterBadge(badge);
			});

			map.flyTo({
				center: feature.geometry.coordinates,
				zoom: Math.max(14, map.getZoom())
			});
		});

		map.on("mousemove", function(e) {
			var features = map.queryRenderedFeatures(e.point, {layers: ["forceIncidents"]});
			map.getCanvas().style.cursor = (features.length) ? "pointer" : "";
		});

	}

	function filterBadge(badge) {
		map.setFilter("forceIncidents", ["==", badge, true]);
	}

	$(".clearMap").click(function() {
		console.log("test");
		map.setFilter("forceIncidents", [">=", "id", 0]);
	});



});
