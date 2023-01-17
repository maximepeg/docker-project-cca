<html>
    <head>
        <title>Poetry</title>
    </head>
 
    <body>
    <form method="post">
    <label>write a poem on:</label> <input type="text" id="poem_prompt" name="poem_prompt" /> 
    <button type="submit">Submit</button>
    <?php
if (!empty($_POST)){
   $poem_prompt = $_POST['poem_prompt'];
   $formatted_prompt = str_replace(" ", "_", $poem_prompt);
   $json = file_get_contents('http://poem-generator/' . $formatted_prompt);

   echo "<p>Your poem: </p> <br/> <p>"    . $json . ".</p>";       
}?>
</body>
</html>