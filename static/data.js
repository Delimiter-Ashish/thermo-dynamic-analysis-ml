document.getElementById('csvFileInput').addEventListener('change', function(event) {
    var file = event.target.files[0];
    if (file) {
        var reader = new FileReader();
        reader.onload = function(event) {
            var csvData = event.target.result;
            displayCSV(csvData);
        };
        reader.readAsText(file);
    }
});

function displayCSV(csvData) {
    var lines = csvData.split('\n');
    var headers = lines[0].split(',');
    var html = '<table><thead><tr>';
    for (var i = 0; i < Math.min(8, headers.length); i++) {
        html += '<th>' + headers[i] + '</th>';
    }
    html += '</tr></thead><tbody>';
    for (var i = 1; i < Math.min(6, lines.length); i++) { // Show maximum 5 rows
        var cells = lines[i].split(',');
        html += '<tr>';
        for (var j = 0; j < Math.min(8, cells.length); j++) {
            html += '<td>' + cells[j] + '</td>';
        }
        html += '</tr>';
    }
    html += '</tbody></table>';
    document.getElementById('csvPreview').innerHTML = html;
}
