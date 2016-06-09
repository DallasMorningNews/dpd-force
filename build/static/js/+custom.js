$(document).ready(function() {

	//custom scripting goes here

	// injecting current year into footer
	// DO NOT DELETE

	var d = new Date();
	var year = d.getFullYear();

	$('.copyright').text(year);


	// initial map setup

	var map = new mapboxgl.Map({
		container: "map",
		style: 'http://maps.dallasnews.com/styles.json',
		center: [-96.7870228, 32.8255772],
		zoom: 10
	});


	// disabling scroll zoom, adding zoom and navigation controls
	// getting the data and passing it along to be processed
	map.on("load", function() {
		map.scrollZoom.disable();
		map.addControl(new mapboxgl.Navigation());

		$.getJSON("js/map_data.json", function(data) {
			processData(data);
		});

	});

	// turning our json into geojson using the geojson.js parser.
	// for more info: https://github.com/caseypt/geojson.js
	// once the data is parsed into geojson, we pass it on to drawMap

	function processData(data) {
		forceData = GeoJSON.parse(data, {Point: ["latitude", "longitude"], exclude: []});
		drawMap(forceData);
	}



	function drawMap(data) {

		// adding the data as a source to the map
		map.addSource("dpdForceData", {
			type: "geojson",
			data: data
		});

		// adding a layer of circles tied to the data source added above
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

		// clicking on a feature on the map (i.e., a circle)
		map.on("click", function(e) {
			var features = map.queryRenderedFeatures(e.point, {layers: ["forceIncidents"]});

			if (!features.length) {
				return;
			}

			var feature = features[0];

			// grab the id of the feature we clicked on
			var id = feature.properties.id;

			// set an empty content variable to hold the content of our popup
			var content = "";

			// check through our data for an id that matches the one clicked on
			$.each(data.features, function(k,v) {
				if (v.properties.id === id) {

					// get the lengh of the number of incidents involved with that
					// feature. This corresponds to the number of officer involved
					// in a use of force incident at that particular date/time/location
					var totalIncidents = v.properties.force_use.length;

					// cycle through each one of those officers, and add their badge
					// number to the content variable that will be displayed in the
					// popup
					for (i = 0; i < totalIncidents; i++) {
						content += "<span class='badge' data-badge='"+ v.properties.force_use[i].current_badge_no +"'>" + v.properties.force_use[i].current_badge_no + "</span>";
					}
				}
			});

			// building out and placying the popup that contains the badge numbers
			var popup = new mapboxgl.Popup()
				.setLngLat(feature.geometry.coordinates)
				.setHTML(content)
				.addTo(map);

			// clicking on a bad number filters the map to display only incidents
			// involving that particluar badge number (i.e., officer)
			$(".badge").click(function() {
				var badge = $(this).attr("data-badge");
				filterBadge(badge);
			});

			// centering and zooming the map on that incident that was clicked on
			map.flyTo({
				center: feature.geometry.coordinates,
				zoom: Math.max(14, map.getZoom())
			});
		});


		// setting the cursor to a pointer when hovering over a feature (i.e. circle)
		map.on("mousemove", function(e) {
			var features = map.queryRenderedFeatures(e.point, {layers: ["forceIncidents"]});
			map.getCanvas().style.cursor = (features.length) ? "pointer" : "";
		});

	}

	// function that filters the map based on badge number clicked
	// checks for a key that is the badge number and if it is marked true
	function filterBadge(badge) {
		map.setFilter("forceIncidents", ["==", badge, true]);
	}

	// button that clears the map of any filter set, reseting the map to it's
	// initial state
	$(".clearMap").click(function() {
		console.log("test");
		map.setFilter("forceIncidents", [">=", "id", 0]);
	});



});
