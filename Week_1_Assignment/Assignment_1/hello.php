
<?php
$input = fopen("players.csv", "r");
$lines = [];

// reading the CSV file
if (($input = fopen($input, "r")) !== FALSE) {
    while (($data = fgetcsv($input, 1000, ",")) !== FALSE) {
        $lines[] = $data;
    }
    fclose($input);
}

// writing the CSV file
$fp = fopen('output.tsv', 'w');
foreach ($lines as $line) {
    fputcsv($fp, $line);
}
fclose($fp);



?>
