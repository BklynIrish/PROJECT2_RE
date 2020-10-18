
// var data = [{
//     type: "sunburst",
//     ids: [
//       "Solar", "Wind", "Hydro","Biomass", "Geothermal", "Solar - Football", "Soccer",
//       "Solar - Rugby", "Wind - Football", "Rugby",
//       "Wind - American Football","Hydro - Football", "Association",
//       "Australian Rules", "Hydro - American Football", "Hydro - Rugby",
//       "Rugby League", "Rugby Union"
//     ],
//     labels: [
//       "Solar", "Wind", "Hydro", "Biomass", "Geothermal","Football", "Soccer", "Rugby",
//       "Football", "Rugby", "American<br>Football", "Football", "Association",
//       "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
//       "Rugby<br>Union"
//     ],
//     parents: [
//       "", "", "","", "", "Solar", "Solar", "Solar", "Wind",
//       "Wind", "Wind","Hydro", "Hydro - Football", "Hydro - Football",
//       "Hydro - Football", "Hydro - Football", "Hydro - Rugby",
//       "Hydro - Rugby"
//     ],
//     outsidetextfont: {size: 20, color: "#377eb8"},
//     // leaf: {opacity: 0.4},
//     marker: {line: {width: 2}},
//   }];
  var data = [{
    type: "sunburst",
    ids: [
      "Types of Renewables","Solar", "Wind", "Water","Biomass", "Geothermal", "Solar - Industrial", "Solar - Residential", "Wind - Horizontal", "Wind - Vertical",
      "Water - Hydropower", " Water - Wave_and_tidal","Biomass - Wood and Wood Derived Fuels", "Biomass - Other",
       "Geothermal - Dry ","Geothermal - Flash","Geothermal - Binary Cycle"
    ],
    labels: [
        "Renewables","Solar", "Wind", "Water", "Biomass", "Geothermal","Industrial", "Residential","Horizontal", "Vertical", "Hydropower",
      "Wave<br>and<br>Tidal<br>Energy","Wood<br>and<br>Wood<br>Derived<br>Fuels", "Other",
        "Dry", "Flash", "Binary<br>Cycle"
    ],
    parents: [
      "","Types of Renewables", "Types of Renewables", "Types of Renewables","Types of Renewables",
       "Types of Renewables","Solar","Solar","Wind", "Wind", "Water","Water",
       "Biomass", "Biomass","Geothermal","Geothermal","Geothermal"
    ],
    outsidetextfont: {size: 20, color: "#377eb8"},
    // leaf: {opacity: 0.4},
    marker: {line: {width: 2}},
  }];
  var layout = {
    margin: {l: 0, r: 0, b: 0, t:0},
    sunburstcolorway:["#636efa","#ef553b","#00cc96"],
  };
  
      
    Plotly.newPlot("sunburst", data, layout);

